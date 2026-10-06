# pylint: disable=C0111

import contextlib
import os.path
import time
import tkinter
import unittest

import tests
from maliang.core import containers
from maliang.standard import features, widgets


def event(**kwargs) -> tkinter.Event:
    """Create a fake event whose attributes are the given keyword arguments."""
    ev = tkinter.Event()
    ev.x = kwargs.pop("x", 0)
    ev.y = kwargs.pop("y", 0)
    ev.char = kwargs.pop("char", "")
    ev.keysym = kwargs.pop("keysym", "")
    ev.delta = kwargs.pop("delta", 0)
    for key, value in kwargs.items():
        setattr(ev, key, value)
    return ev


@contextlib.contextmanager
def canvas(size=(200, 200)):
    with tests.window() as tk:
        with containers.Canvas(tk) as cv:
            cv.place(width=size[0], height=size[1])
            cv.update()
            cv._initialization()
            yield tk, cv


def new_widget(cls, cv, position=(0, 0), size=(100, 30), **kwargs):
    """Create a widget without gradient animations.

    A gradient animation is scheduled on the shared root window and keeps
    running after the window of the test case has been destroyed.

    ``size=None`` is for the widgets whose third positional argument is not a
    size: `Switch`, `CheckBox` and `RadioBox` take a length, and
    `UnderlineButton` and `HighlightButton` have no size at all.
    """
    kwargs.setdefault("gradient_animation", False)
    if size is None:
        return cls(cv, position, **kwargs)
    return cls(cv, position, size, **kwargs)


class TestFeatureBinding(unittest.TestCase):

    def test_every_widget_uses_the_expected_feature(self) -> None:
        with canvas() as (_, cv):
            cases = (
                (new_widget(widgets.Text, cv, text="t"), features.TextFeature),
                (new_widget(widgets.Image, cv, size=None), features.ImageFeature),
                (new_widget(widgets.Label, cv, text="l"), features.LabelFeature),
                (new_widget(widgets.Button, cv, text="b"), features.ButtonFeature),
                (new_widget(widgets.Switch, cv, size=None), features.SwitchFeature),
                (new_widget(widgets.CheckBox, cv, size=None, length=30), features.CheckBoxFeature),
                (new_widget(widgets.ToggleButton, cv, text="t"), features.ToggleButtonFeature),
                (new_widget(widgets.RadioBox, cv, size=None, length=30), features.RadioBoxFeature),
                (new_widget(widgets.ProgressBar, cv, size=None), features.ProgressBarFeature),
                (new_widget(widgets.InputBox, cv, size=(100, 30)), features.InputBoxFeature),
                (new_widget(widgets.UnderlineButton, cv, size=None, text="u"), features.Underline),
                (new_widget(widgets.HighlightButton, cv, size=None, text="h"), features.Highlight),
                (new_widget(widgets.Slider, cv, size=(100, 30)), features.SliderFeature),
                (new_widget(widgets.SegmentedButton, cv, size=None, text=("a", "b")), features.SegmentedButtonFeature),
                (new_widget(widgets.SpinBox, cv, size=None), features.SpinBoxFeature),
            )

            for widget, cls in cases:
                with self.subTest(widget=type(widget).__name__):
                    self.assertIsInstance(widget.feature, cls)


class TestButtonFeature(unittest.TestCase):

    def test_motion_outside_resets_the_state(self) -> None:
        with canvas() as (_, cv):
            widget = new_widget(widgets.Button, cv, text="b", size=(60, 30))

            self.assertTrue(widget.feature._motion(event(x=5, y=5)))
            self.assertEqual(widget.state, "hover")

            self.assertFalse(widget.feature._motion(event(x=9999, y=9999)))
            self.assertEqual(widget.state, "normal")

    def test_motion_during_a_button_press(self) -> None:
        with canvas() as (_, cv):
            widget = new_widget(widgets.Button, cv, text="b", size=(60, 30))

            for method in ("_b_1_motion", "_b_2_motion", "_b_3_motion"):
                widget.update("normal")
                with self.subTest(method=method):
                    self.assertTrue(getattr(widget.feature, method)(event(x=5, y=5)))
                    self.assertEqual(widget.state, "hover")

    def test_command_receives_the_arguments(self) -> None:
        with canvas() as (_, cv):
            widget = new_widget(widgets.Button, cv, text="b", size=(60, 30))
            calls = []
            widget.feature = features.ButtonFeature(
                widget, command=lambda *args: calls.append(args), args=(1, 2))

            widget.update("hover")
            widget.generate_event("<Button-1>", x=5, y=5)
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)

            self.assertEqual(calls, [(1, 2)])


class TestToggleButtonFeature(unittest.TestCase):

    def test_motion_outside_resets_the_state(self) -> None:
        with canvas() as (_, cv):
            widget = new_widget(widgets.ToggleButton, cv, text="t", size=(60, 30))

            self.assertTrue(widget.feature._motion(event(x=5, y=5)))
            self.assertEqual(widget.state, "hover-off")

            self.assertFalse(widget.feature._motion(event(x=9999, y=9999)))
            self.assertEqual(widget.state, "normal-off")

    def test_click_toggles_the_state_and_calls_the_command(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = new_widget(widgets.ToggleButton, cv, text="t", size=(60, 30), command=calls.append)

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            self.assertEqual(widget.state, "active-off")

            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertTrue(widget.get())
            self.assertEqual(widget.state, "hover-on")
            self.assertEqual(calls, [True])

    def test_checkbox_toggles_the_state(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = new_widget(widgets.CheckBox, cv, size=None, length=30, command=calls.append)

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)

            self.assertTrue(widget.get())
            self.assertEqual(widget.state, "hover-on")
            self.assertEqual(calls, [True])


class TestRadioBoxFeature(unittest.TestCase):

    def test_clicking_the_selected_button_does_nothing(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = new_widget(widgets.RadioBox, cv, size=None, length=30, default=True, command=calls.append)
            self.assertTrue(widget.get())

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)

            self.assertTrue(widget.get())
            self.assertEqual(calls, [])

    def test_clicking_another_button_turns_the_selected_one_off(self) -> None:
        with canvas() as (_, cv):
            first_calls, second_calls = [], []
            first = new_widget(widgets.RadioBox, cv, (0, 0), None, length=30,
                               default=True, command=first_calls.append)
            second = new_widget(widgets.RadioBox, cv, (60, 0), None, length=30,
                                command=second_calls.append)
            first.group(second)

            second.generate_event("<Motion>", x=65, y=5)
            second.generate_event("<Button-1>", x=65, y=5)
            second.generate_event("<ButtonRelease-1>", x=65, y=5)

            self.assertFalse(first.get())
            self.assertTrue(second.get())
            self.assertEqual(first_calls, [False])
            self.assertEqual(second_calls, [True])


class InputBoxTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.tk = tests.window()
        self.cv = containers.Canvas(self.tk)
        self.cv.place(width=200, height=200)
        self.cv.update()
        self.cv._initialization()
        self.widget = widgets.InputBox(self.cv, (0, 0), (200, 30), gradient_animation=False)
        self.proxy = self.widget.texts[0].text_proxy

    def tearDown(self) -> None:
        self.tk.destroy()

    def activate(self) -> None:
        """Click the widget to focus it and place the text cursor."""
        self.widget.generate_event("<Button-1>", x=5, y=5)
        self.assertEqual(self.widget.state, "active")


class TestInputBoxFeature(InputBoxTestCase):

    def test_clicking_outside_resets_the_state(self) -> None:
        self.activate()

        self.widget.generate_event("<Button-1>", x=9999, y=9999)

        self.assertEqual(self.widget.state, "normal")

    def test_drag_selects_backwards(self) -> None:
        self.widget.set("hello world")
        self.widget.generate_event("<Button-1>", x=150, y=5)
        start = self.proxy.cursor_get()
        self.assertGreater(start, 0)

        self.widget.generate_event("<B1-Motion>", x=0, y=5)

        # The selection is always stored as `(left, right)`
        self.assertEqual(self.proxy.cursor_get(), 0)
        self.assertEqual(self.proxy.select_get(), (0, start))

    def test_drag_without_moving_clears_the_selection(self) -> None:
        self.widget.set("hello world")
        self.widget.generate_event("<Button-1>", x=50, y=5)
        self.proxy.select_set(0, 5)

        # Dragging to the very same index clears the selection
        self.widget.generate_event("<B1-Motion>", x=50, y=5)

        self.assertIsNone(self.proxy.select_get())

    def test_drag_without_clicking_does_nothing(self) -> None:
        self.assertFalse(self.widget.feature._b_1_motion(event(x=100, y=5)))
        self.assertIsNone(self.proxy.select_get())

    def test_backspace_in_the_middle_removes_the_previous_character(self) -> None:
        self.widget.set("hello")
        self.activate()
        self.proxy.cursor_set(3)

        self.widget.generate_event("<KeyPress>", keysym="BackSpace", char="")

        self.assertEqual(self.widget.get(), "helo")

    def test_paste_replaces_the_selection(self) -> None:
        self.widget.set("hello world")
        self.activate()
        self.cv.clipboard_clear()
        self.cv.clipboard_append("XYZ")
        self.proxy.select_set(0, 5)

        self.assertTrue(self.widget.feature._paste(event()))

        self.assertNotIn("hello", self.widget.get())
        self.assertIn("XYZ", self.widget.get())


class TestSliderFeature(unittest.TestCase):

    def test_clicking_the_track_moves_the_slider(self) -> None:
        with canvas() as (tk, cv):
            widget = new_widget(widgets.Slider, cv, size=(200, 30))

            # Click on the track, but not on the thumb
            track, thumb = widget.shapes[0], widget.shapes[2]
            x = (thumb.region()[2] + track.region()[2]) // 2
            y = (track.region()[1] + track.region()[3]) // 2

            widget.generate_event("<Button-1>", x=x, y=y)
            self.assertEqual(widget.state, "active")
            self.assertEqual(widget.feature._temp_position, (x, y))

            # The value is animated towards the clicked position, let the
            # animation end before the window is destroyed
            time.sleep(0.25)
            tk.update()

            self.assertGreater(widget.get(), 0.5)
            self.assertLess(widget.get(), 1)
            self.assertEqual(widget.feature._temp_position, (x, y))

    def test_drag_moves_the_slider(self) -> None:
        with canvas() as (_, cv):
            widget = new_widget(widgets.Slider, cv, size=(200, 30))

            # The thumb is the only shape that reacts to hovering
            x, y = widget.shapes[2].center()
            x, y = round(x), round(y)
            widget.generate_event("<Motion>", x=x, y=y)
            self.assertEqual(widget.state, "hover")

            widget.generate_event("<Button-1>", x=x, y=y)
            self.assertEqual(widget.state, "active")

            widget.generate_event("<B1-Motion>", x=x + 100, y=y)
            self.assertGreater(widget.get(), 0)

            widget.generate_event("<ButtonRelease-1>", x=x + 100, y=y)
            self.assertEqual(widget.state, "hover")
            self.assertIsNone(widget.feature._temp_position)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
