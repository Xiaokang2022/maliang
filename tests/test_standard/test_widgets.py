# pylint: disable=C0111

import contextlib
import io
import os.path
import tkinter
import unittest
import warnings

import tests
from maliang.core import containers
from maliang.standard import widgets
from maliang.toolbox import enhanced

IMAGE = "tests/assets/images/logo.png"


def event(**kwargs) -> tkinter.Event:
    """Create a fake tkinter event with the given attributes."""
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


def photo(master) -> enhanced.PhotoImage:
    return enhanced.PhotoImage(file=IMAGE, master=master)


class TestBasicWidgets(unittest.TestCase):

    def test_text(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.Text(cv, (0, 0), text="hello")
            self.assertEqual(widget.get(), "hello")
            widget.set("hello world")
            self.assertEqual(widget.get(), "hello world")
            widget.set("hi")
            self.assertEqual(widget.get(), "hi")

            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "normal")

            # A fixed size disables auto resize
            fixed = widgets.Text(cv, (0, 0), (100, 30), text="a")
            self.assertFalse(fixed.auto_resize)
            fixed.set("a much longer text")

    def test_image(self) -> None:
        with canvas() as (_, cv):
            image = photo(cv)
            widget = widgets.Image(cv, (0, 0), image=image)
            self.assertIs(widget.get(), widget.images[0].initial_image)

            widget.set(image)
            self.assertIsNotNone(widget.get())

            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "normal")

            # No image -> size falls back to zero
            empty = widgets.Image(cv, (0, 0))
            self.assertEqual(empty.size, (0, 0))

            widget.set(None)

    def test_image_resize(self) -> None:
        with canvas() as (_, cv):
            image = photo(cv)
            widget = widgets.Image(cv, (0, 0), (60, 45), image=image)
            self.assertEqual(widget.images[0].initial_image.width(), 60)

    def test_label(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.Label(cv, (0, 0), text="label")
            self.assertEqual(widget.get(), "label")
            widget.set("longer label")
            self.assertEqual(widget.get(), "longer label")

            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "normal")

            with_image = widgets.Label(cv, (100, 100), text="x", image=photo(cv))
            self.assertEqual(with_image.get(), "x")

    def test_button(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.Button(cv, (0, 0), text="ok", command=lambda: calls.append(1))
            self.assertEqual(widget.get(), "ok")
            widget.set("done")
            self.assertEqual(widget.get(), "done")

            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Button-1>", x=5, y=5)
            self.assertEqual(widget.state, "active")
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            self.assertEqual(calls, [1])

            widget.generate_event("<B1-Motion>", x=5, y=5)
            widget.generate_event("<B2-Motion>", x=5, y=5)
            widget.generate_event("<B3-Motion>", x=5, y=5)
            # Dragging with any button keeps the hover state on this widget
            self.assertEqual(widget.state, "hover")

            with_image = widgets.Button(cv, (100, 100), text="x", image=photo(cv))
            self.assertEqual(with_image.get(), "x")

    def test_button_disabled_motion(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.Button(cv, (0, 0), text="ok")
            widget.disable()
            self.assertEqual(widget.state, "disabled")
            # A disabled widget must not switch to hover
            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "disabled")
            widget.disable(False)
            self.assertEqual(widget.state, "normal")


class TestToggleWidgets(unittest.TestCase):

    def test_switch(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.Switch(cv, (0, 0), 60, command=calls.append)
            self.assertFalse(widget.get())

            widget.set(True)
            self.assertTrue(widget.get())
            widget.set(True)
            self.assertTrue(widget.get())
            widget.set(False, callback=True)
            self.assertEqual(calls, [False])

            widget.generate_event("<Motion>", x=5, y=5)
            self.assertTrue(widget.state.startswith("hover"))
            widget.generate_event("<Button-1>", x=5, y=5)
            self.assertTrue(widget.state.startswith("active"))
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertTrue(widget.get())
            self.assertEqual(calls[-1], True)
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertTrue(widget.state.startswith("normal"))

            with_image = widgets.Switch(cv, (100, 100), image=photo(cv))
            self.assertFalse(with_image.get())

    def test_switch_disabled(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.Switch(cv, (0, 0), 60, default=True)
            self.assertTrue(widget.get())
            widget.disable()
            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Motion>", x=9999, y=9999)

    def test_checkbox(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.CheckBox(cv, (0, 0), command=calls.append)
            self.assertFalse(widget.get())
            widget.set(True)
            self.assertTrue(widget.get())
            widget.set(True)
            widget.set(False, callback=True)
            self.assertEqual(calls, [False])

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertTrue(widget.get())

            default = widgets.CheckBox(cv, (50, 50), default=True)
            self.assertTrue(default.get())
            with_image = widgets.CheckBox(cv, (100, 100), image=photo(cv))
            self.assertFalse(with_image.get())

    def test_toggle_button(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.ToggleButton(cv, (0, 0), text="t", command=calls.append)
            self.assertFalse(widget.get())
            widget.set(True)
            self.assertTrue(widget.get())
            widget.set(False, callback=True)
            self.assertEqual(calls, [False])

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertTrue(widget.get())

            default = widgets.ToggleButton(cv, (100, 100), text="t", default=True)
            self.assertTrue(default.get())
            with_image = widgets.ToggleButton(cv, (150, 150), text="t", image=photo(cv))
            self.assertFalse(with_image.get())

    def test_radiobox(self) -> None:
        with canvas() as (_, cv):
            calls = []
            first = widgets.RadioBox(cv, (0, 0), command=calls.append)
            second = widgets.RadioBox(cv, (50, 0))
            third = widgets.RadioBox(cv, (100, 0))

            first.group(second, third)
            self.assertIn(first, second.groups)
            first.group(second)  # already in group

            self.assertFalse(first.get())
            first.set(True)
            self.assertTrue(first.get())
            first.set(True)
            first.set(False, callback=True)
            self.assertEqual(calls, [False])

            # Selecting `second` unselects `first`
            first.set(True)
            second.generate_event("<Motion>", x=55, y=5)
            second.generate_event("<Button-1>", x=55, y=5)
            second.generate_event("<ButtonRelease-1>", x=55, y=5)
            self.assertTrue(second.get())
            self.assertFalse(first.get())

            # Clicking an already selected radio box does nothing
            second.generate_event("<Motion>", x=55, y=5)
            second.generate_event("<Button-1>", x=55, y=5)
            second.generate_event("<ButtonRelease-1>", x=55, y=5)
            self.assertTrue(second.get())

            with_image = widgets.RadioBox(cv, (150, 0), image=photo(cv))
            self.assertFalse(with_image.get())
            default = widgets.RadioBox(cv, (200, 0), default=True)
            self.assertTrue(default.get())


class TestBarWidgets(unittest.TestCase):

    def test_progressbar(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.ProgressBar(cv, (0, 0), (200, 20), command=calls.append)
            self.assertEqual(widget.get(), 0)
            widget.set(0.5)
            self.assertEqual(widget.get(), 0.5)
            widget.set(-1)
            self.assertEqual(widget.get(), 0)
            widget.set(2)
            self.assertEqual(widget.get(), 1)
            widget.set(0.5, callback=True)
            self.assertEqual(calls, [0.5])
            widget.set(0)

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Motion>", x=9999, y=9999)

            default = widgets.ProgressBar(cv, (0, 50), (200, 20), default=0.5)
            self.assertEqual(default.get(), 0.5)
            with_image = widgets.ProgressBar(cv, (0, 100), (200, 20), image=photo(cv))
            self.assertEqual(with_image.get(), 0)

    def test_slider(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.Slider(cv, (0, 0), (200, 30), command=calls.append)
            self.assertEqual(widget.get(), 0)

            widget.generate_event("<Motion>", x=15, y=15)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Button-1>", x=15, y=15)
            self.assertEqual(widget.state, "active")
            widget.generate_event("<B1-Motion>", x=100, y=15)
            widget.generate_event("<ButtonRelease-1>", x=100, y=15)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "normal")

            widget.set(0.5, callback=True)
            self.assertEqual(widget.get(), 0.5)
            self.assertEqual(calls[-1], 0.5)
            widget.set(0.5)
            widget.set(-1)
            self.assertEqual(widget.get(), 0)
            widget.set(2)
            self.assertEqual(widget.get(), 1)

            default = widgets.Slider(cv, (0, 50), (200, 30), default=0.3)
            self.assertAlmostEqual(default.get(), 0.3)


class TestTextWidgets(unittest.TestCase):

    def test_inputbox(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.InputBox(cv, (0, 0), (200, 30))
            self.assertEqual(widget.get(), "")
            self.assertTrue(widget.set("hello"))
            self.assertEqual(widget.get(), "hello")
            self.assertTrue(widget.insert(0, ">> "))
            self.assertTrue(widget.append("!"))
            widget.remove(0, 3)
            self.assertEqual(widget.pop(), "!")
            widget.clear()
            self.assertEqual(widget.get(), "")

            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "normal")

            # Clicking activates and sets the cursor
            widget.set("hello world")
            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            self.assertEqual(widget.state, "active")
            widget.generate_event("<B1-Motion>", x=100, y=5)
            widget.generate_event("<ButtonRelease-1>", x=100, y=5)
            # The cursor moved with the drag and a selection was made
            self.assertIsNotNone(widget.texts[0].text_proxy.cursor_get())
            self.assertIsNotNone(widget.texts[0].text_proxy.select_get())

            with_image = widgets.InputBox(cv, (0, 50), (200, 30), image=photo(cv))
            self.assertEqual(with_image.get(), "")

            fixed = widgets.InputBox(cv, (0, 100), (200, 30), limit=5)
            fixed.set("abc")
            self.assertFalse(fixed.append("defgh"))
            self.assertEqual(fixed.get(), "abc")

            shown = widgets.InputBox(cv, (0, 150), (200, 30), show="*", ignore="x")
            self.assertTrue(shown.append("abc"))
            self.assertEqual(shown.get(), "abc")
            shown.append("x")
            self.assertEqual(shown.get(), "abc")

    def test_inputbox_keys(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.InputBox(cv, (0, 0), (200, 30))
            widget.set("hello world")
            proxy = widget.texts[0].text_proxy

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            proxy.cursor_set(0)

            widget.generate_event("<KeyPress>", keysym="Right", char="")
            self.assertEqual(proxy.cursor_get(), 1)
            widget.generate_event("<KeyPress>", keysym="Left", char="")
            self.assertEqual(proxy.cursor_get(), 0)
            widget.generate_event("<KeyPress>", keysym="Delete", char="")
            self.assertEqual(widget.get(), "ello world")
            widget.generate_event("<KeyPress>", keysym="BackSpace", char="")
            self.assertEqual(widget.get(), "ello world")
            widget.generate_event("<KeyPress>", keysym="A", char="A")
            self.assertEqual(widget.get(), "Aello world")

            # With a selection, arrows clear it and move to its edge
            proxy.select_set(0, 3)
            widget.generate_event("<KeyPress>", keysym="Right", char="")
            self.assertIsNone(proxy.select_get())
            self.assertEqual(proxy.cursor_get(), 3)
            proxy.select_set(0, 3)
            widget.generate_event("<KeyPress>", keysym="Left", char="")
            self.assertIsNone(proxy.select_get())
            self.assertEqual(proxy.cursor_get(), 0)

            # Delete and typing replace the selected range
            proxy.select_set(0, 3)
            before = widget.get()
            widget.generate_event("<KeyPress>", keysym="Delete", char="")
            self.assertIsNone(proxy.select_get())
            self.assertEqual(len(widget.get()), len(before) - 3)
            proxy.select_set(0, 2)
            before = widget.get()
            widget.generate_event("<KeyPress>", keysym="A", char="Z")
            self.assertEqual(len(widget.get()), len(before) - 2 + 1)
            self.assertIn("Z", widget.get())

            # Backspace at the very beginning and Delete at the very end do nothing
            proxy.cursor_set(0)
            before = widget.get()
            widget.generate_event("<KeyPress>", keysym="BackSpace", char="")
            self.assertEqual(widget.get(), before)
            proxy.cursor_set(proxy.length())
            before = widget.get()
            widget.generate_event("<KeyPress>", keysym="Delete", char="")
            self.assertEqual(widget.get(), before)

    def test_inputbox_clipboard(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.InputBox(cv, (0, 0), (200, 30))
            widget.set("hello world")
            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)

            feature = widget.feature
            widget.texts[0].text_proxy.select_set(0, 5)

            self.assertTrue(feature._copy(event()))
            self.assertEqual(cv.clipboard_get(), "hello")

            self.assertTrue(feature._cut(event()))
            self.assertEqual(widget.get(), " world")

            cv.clipboard_clear()
            cv.clipboard_append("XYZ")
            self.assertTrue(feature._paste(event()))
            self.assertIn("XYZ", widget.get())

            self.assertTrue(feature._select_all(event()))
            self.assertEqual(
                widget.texts[0].text_proxy.select_get(),
                (0, widget.texts[0].text_proxy.length()))

    def test_inputbox_unfocused(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.InputBox(cv, (0, 0), (200, 30))
            feature = widget.feature
            self.assertFalse(feature._copy(event()))
            self.assertFalse(feature._paste(event()))
            self.assertFalse(feature._select_all(event()))


class TestIconButton(unittest.TestCase):

    def test_basic(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.IconButton(cv, (0, 0), text="hi", command=lambda: calls.append(1))
            self.assertEqual(widget.get(), "hi")
            widget.set("hello")
            self.assertEqual(widget.get(), "hello")

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertEqual(calls, [1])

            sized = widgets.IconButton(cv, (100, 100), (80, 30), text="x")
            self.assertEqual(sized.get(), "x")
            with_image = widgets.IconButton(
                cv, (200, 0), (80, 30), text="x", image=photo(cv))
            self.assertEqual(with_image.get(), "x")


class TestTextButtons(unittest.TestCase):

    def test_underline(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.UnderlineButton(cv, (0, 0), text="link", command=lambda: calls.append(1))
            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Button-1>", x=5, y=5)
            self.assertEqual(widget.state, "active")
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertEqual(calls, [1])
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "normal")

            with_image = widgets.UnderlineButton(cv, (100, 0), text="x", image=photo(cv))
            self.assertIsNotNone(with_image)

    def test_highlight(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.HighlightButton(cv, (0, 0), text="hi", command=lambda: calls.append(1))
            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "hover")
            widget.generate_event("<Button-1>", x=5, y=5)
            self.assertEqual(widget.state, "active")
            widget.generate_event("<ButtonRelease-1>", x=5, y=5)
            self.assertEqual(calls, [1])
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "normal")

            with_image = widgets.HighlightButton(cv, (100, 0), text="x", image=photo(cv))
            self.assertIsNotNone(with_image)

    def test_underline_disabled(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.UnderlineButton(cv, (0, 0), text="link")
            widget.disable()
            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "disabled")
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "disabled")

    def test_highlight_disabled(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.HighlightButton(cv, (0, 0), text="hi")
            widget.disable()
            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.state, "disabled")
            widget.generate_event("<Motion>", x=9999, y=9999)
            self.assertEqual(widget.state, "disabled")


class TestSegmentedButton(unittest.TestCase):

    def test_horizontal(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.SegmentedButton(
                cv, (0, 0), text=("a", "b", "c"), command=calls.append)
            self.assertIsNone(widget.get())

            widget.set(1, callback=True)
            self.assertEqual(widget.get(), 1)
            self.assertEqual(calls, [1])

            widget.generate_event("<Motion>", x=5, y=5)
            self.assertEqual(widget.generate_event("<Motion>", x=9999, y=9999), None)

            sized = widgets.SegmentedButton(
                cv, (0, 100), ((30, 30), (30, 30)), text=("x", "y"))
            self.assertIsNone(sized.get())

            default = widgets.SegmentedButton(
                cv, (0, 150), text=("a", "b"), default=0)
            self.assertEqual(default.get(), 0)

            images = widgets.SegmentedButton(
                cv, (0, 200), ((30, 30), (30, 30)), text=("x", "y"),
                image=(photo(cv), photo(cv)))
            self.assertIsNone(images.get())

    def test_vertical_and_empty(self) -> None:
        with canvas() as (_, cv):
            vertical = widgets.SegmentedButton(
                cv, (0, 0), text=("a", "b"), layout="vertical")
            self.assertIsNone(vertical.get())

            empty = widgets.SegmentedButton(cv, (100, 0))
            self.assertIsNone(empty.get())

            callback = []
            no_text = widgets.SegmentedButton(
                cv, (200, 0), command=lambda i: callback.append(i))
            no_text.set(None)
            self.assertIsNone(no_text.get())


class TestSpinBox(unittest.TestCase):

    def test_basic(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.SpinBox(
                cv, (0, 0), (200, 30), command=lambda up: calls.append(up))
            self.assertEqual(widget.get(), "")
            widget.set("5")
            self.assertEqual(widget.get(), "5")
            widget.append("0")
            widget.clear()
            self.assertEqual(widget.get(), "")

            # Empty value -> set to zero
            widget.change(True)
            self.assertEqual(widget.get(), "0")
            widget.change(True)
            self.assertEqual(widget.get(), "1")
            widget.change(False)
            self.assertEqual(widget.get(), "0")

            widget.generate_event("<Motion>", x=5, y=5)
            widget.generate_event("<Button-1>", x=5, y=5)
            widget.children[0].update("active")
            widget.generate_event("<MouseWheel>", delta=120)
            self.assertEqual(calls, [True])
            widget.generate_event("<MouseWheel>", delta=-120)
            self.assertEqual(calls, [True, False])

            default = widgets.SpinBox(cv, (0, 50), (200, 30), default="3")
            self.assertEqual(default.get(), "3")
            with_image = widgets.SpinBox(cv, (0, 100), (200, 30), image=photo(cv))
            self.assertEqual(with_image.get(), "")

    def test_float_and_invalid(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.SpinBox(cv, (0, 0), (200, 30), format_spec=".2f", step=0.5)
            widget.set("1.00")
            widget.change(True)
            self.assertEqual(widget.get(), "1.50")

            # A value that cannot be parsed is kept as-is
            widget.set("abc")
            widget.change(True)
            self.assertEqual(widget.get(), "abc")

    def test_auto_command(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.SpinBox(cv, (0, 0), (200, 30))
            widget.set("1")
            widget.children[0].update("active")
            widget.feature._mouse_wheel(event(delta=120))
            self.assertEqual(widget.get(), "2")
            widget.feature._mouse_wheel(event(delta=-120))
            self.assertEqual(widget.get(), "1")
            widget.children[0].update("normal")
            self.assertFalse(widget.feature._mouse_wheel(event(delta=120)))


class TestOptionWidgets(unittest.TestCase):

    def test_option_button(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.OptionButton(
                cv, (0, 0), (100, 30), text=("a", "b"), command=calls.append)
            self.assertIsNone(widget.get())

            widget._open_options()
            widget._segmented_button.children[1].set(True, callback=True)
            self.assertEqual(widget.get(), 1)
            self.assertEqual(calls, [1])

            widget.set(0, callback=True)
            self.assertEqual(widget.get(), 0)
            self.assertEqual(calls[-1], 0)

            widget._extra_bind(event(x=9999, y=9999))
            widget._extra_bind(event(x=5, y=5))

            for align in ("up", "center", "down"):
                self.assertIsInstance(widget._get_position(align), tuple)

            default = widgets.OptionButton(cv, (200, 0), (100, 30), text=("a", "b"), default=0)
            self.assertEqual(default.get(), 0)

            auto = widgets.OptionButton(cv, (0, 100), text=("a", "b"))
            self.assertEqual(auto._button.get(), "")
            self.assertIsNotNone(auto.size)

    def test_option_button_up(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.OptionButton(cv, (100, 100), (100, 30), text=("a", "b"), align="up")
            widget._open_options()
            widget._segmented_button.children[0].set(True, callback=True)
            self.assertEqual(widget.get(), 0)
            widget._close_options(0)
            self.assertEqual(widget.get(), 0)

    def test_combobox(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.ComboBox(
                cv, (0, 0), (100, 30), text=("a", "b"), command=calls.append)
            self.assertIsNone(widget.get())

            widget._open_options()
            widget._segmented_button.children[1].set(True, callback=True)
            self.assertEqual(widget.get(), 1)
            self.assertEqual(calls, [1])

            widget.set(0, callback=True)
            self.assertEqual(widget.get(), 0)

            widget._extra_bind(event(x=9999, y=9999))
            widget._extra_bind(event(x=5, y=5))

            for align in ("up", "down"):
                self.assertIsInstance(widget._get_position(align), tuple)

            default = widgets.ComboBox(cv, (200, 0), (100, 30), text=("a", "b"), default=0)
            self.assertEqual(default.get(), 0)

            auto = widgets.ComboBox(cv, (0, 100), text=("a", "b"))
            self.assertIsNotNone(auto.size)

    def test_combobox_toggle_button(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.ComboBox(cv, (0, 0), (100, 30), text=("a", "b"))
            widget._button.generate_event("<Motion>", x=85, y=15)
            widget._button.generate_event("<Button-1>", x=85, y=15)
            widget._button.generate_event("<ButtonRelease-1>", x=85, y=15)
            self.assertFalse(widget._segmented_button.disappeared)
            widget._button.generate_event("<Motion>", x=85, y=15)
            widget._button.generate_event("<Button-1>", x=85, y=15)
            widget._button.generate_event("<ButtonRelease-1>", x=85, y=15)
            self.assertTrue(widget._segmented_button.disappeared)


class TestSpinner(unittest.TestCase):

    def test_determinate(self) -> None:
        with canvas() as (_, cv):
            calls = []
            widget = widgets.Spinner(cv, (0, 0), (30, 30), command=calls.append)
            self.assertEqual(widget.get(), 0)
            widget.set(0.5, callback=True)
            self.assertEqual(widget.get(), 0.5)
            self.assertEqual(calls, [0.5])
            widget.set(-1)
            self.assertEqual(widget.get(), 0)
            widget.set(2)
            self.assertEqual(widget.get(), 1)

            default = widgets.Spinner(cv, (50, 0), (30, 30), default=0.5)
            self.assertEqual(default.get(), 0.5)
            widget.destroy()

    def test_indeterminate(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.Spinner(cv, (0, 0), (30, 30), mode="indeterminate")

            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                widget.get()
                widget.set(0.5)
                self.assertTrue(caught)

            widget.destroy()


class TestTooltip(unittest.TestCase):

    def test_basic(self) -> None:
        with canvas() as (_, cv):
            for align in ("up", "down", "left", "right", "center"):
                button = widgets.Button(cv, (50, 50), text="b")
                tooltip = widgets.Tooltip(button, text="tip", align=align)
                self.assertEqual(tooltip.get(), "tip")
                tooltip.set("tip2")
                self.assertEqual(tooltip.get(), "tip2")

                tooltip._display(None, False)
                tooltip._display("hover", False)
                self.assertFalse(tooltip.disappeared)
                tooltip._display("normal", False)
                self.assertTrue(tooltip.disappeared)

            sized = widgets.Tooltip(widgets.Button(cv, (0, 0), text="b"),
                                    (40, 20), text="t", padding=5)
            self.assertEqual(sized.get(), "t")


class TestWidgetLifecycle(unittest.TestCase):

    def test_common_methods(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.Button(cv, (10, 10), (60, 30), text="b")
            self.assertTrue(widget.exists())

            widget.disable()
            self.assertTrue(widget.state_before_disabled)
            widget.disable(False)

            widget.forget()
            self.assertTrue(widget.disappeared)
            widget.forget(False)
            self.assertFalse(widget.disappeared)

            widget.lift()
            self.assertIs(cv.widgets[-1], widget)

            x, y = widget.position
            widget.move(5, 5)
            self.assertEqual(widget.position, (x + 5, y + 5))
            widget.moveto(x, y)
            self.assertEqual(widget.position, (x, y))

            width, height = widget.size
            widget.zoom((1.5, 1.5))
            self.assertEqual(widget.size, (width * 1.5, height * 1.5))
            widget.resize((60, 30))
            self.assertEqual(widget.size, (60, 30))
            widget.resize()
            self.assertEqual(widget.size, (60, 30))

            region = widget.region()
            self.assertEqual(region[2] - region[0], round(widget.size[0]))
            self.assertEqual(region[3] - region[1], round(widget.size[1]))
            self.assertEqual(
                widget.center(),
                ((region[0] + region[2]) >> 1, (region[1] + region[3]) >> 1))
            self.assertTrue(widget.detect(*widget.center()))
            self.assertFalse(widget.detect(region[0] - 1000, region[1]))

            with warnings.catch_warnings(record=True) as caught:
                warnings.simplefilter("always")
                widget.zoom((1, 1), zoom_position=False, zoom_size=False)
                self.assertTrue(caught)

            hook_called = []
            widget.bind_on_update(lambda state, anim: hook_called.append(state))
            widget.update()
            widget.unbind_on_update(widget._update_hooks[0])
            self.assertTrue(hook_called)

            widget.bind("<<Custom>>", lambda e: None)
            self.assertIn("<<Custom>>", widget.feature.extra_commands)
            widget.unbind("<<Custom>>", widget.feature.extra_commands["<<Custom>>"][0])
            self.assertEqual(widget.feature.extra_commands["<<Custom>>"], [])

            widget.destroy()
            self.assertFalse(widget.exists())

            extra = widgets.Button(cv, (0, 0), text="b")
            extra.bind("<<Custom>>", lambda e: None, auto_detect=False)
            self.assertIn("<<Custom>>", extra.feature.extra_commands)
            extra.generate_event("<<Custom>>")

    def test_nested_widget(self) -> None:
        with canvas() as (_, cv):
            parent = widgets.Button(cv, (0, 0), (100, 100), text="p")
            child = widgets.Button(parent, (10, 10), (30, 30), text="c")
            self.assertTrue(child.nested)
            self.assertIs(child.widget, parent)
            self.assertIn(child, parent.children)
            parent.destroy()

    def test_bind_on_update_error(self) -> None:
        with canvas() as (_, cv):
            widget = widgets.Button(cv, (0, 0), text="b")

            def broken(state, anim) -> None:
                raise RuntimeError

            widget.bind_on_update(broken)
            with io.StringIO() as captured:
                with contextlib.redirect_stderr(captured):
                    widget.update()
                # The failure is reported instead of breaking the update
                self.assertIn("RuntimeError", captured.getvalue())


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
