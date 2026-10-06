# pylint: disable=C0111

import os.path
import unittest

import tests
from maliang.core import containers, virtual
from maliang.standard import widgets

COLOR = "#123456"


class StyleTestMixin:

    def setUp(self) -> None:
        self.tk = tests.window()
        self.cv = containers.Canvas(self.tk)

    def tearDown(self) -> None:
        self.tk.destroy()


class TestTextStyles(StyleTestMixin, unittest.TestCase):

    def test_text(self) -> None:
        widget = widgets.Text(self.cv, (0, 0), text="t")
        state, text = widget.style.states[0], widget.elements[-1].name

        widget.style.set("light", fg=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        widget.style.set("dark", fg=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)
        widget.style.set(None, fg=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)

    def test_label(self) -> None:
        widget = widgets.Label(self.cv, (0, 0), text="l")
        state = widget.style.states[0]
        shape, text = widget.elements[0].name, widget.elements[-1].name

        widget.style.set("light", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["outline"], COLOR)
        widget.style.set("dark", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["outline"], COLOR)
        widget.style.set(None, fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["fill"], COLOR)

    def test_button(self) -> None:
        widget = widgets.Button(self.cv, (0, 0), text="b")
        state = widget.style.states[0]
        shape, text = widget.elements[0].name, widget.elements[-1].name

        widget.style.set("light", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["outline"], COLOR)
        widget.style.set("dark", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["outline"], COLOR)

    def test_underline(self) -> None:
        widget = widgets.UnderlineButton(self.cv, (0, 0), text="u")
        state, text = widget.style.states[0], widget.elements[-1].name

        widget.style.set("light", fg=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        widget.style.set("dark", fg=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)

    def test_highlight(self) -> None:
        widget = widgets.HighlightButton(self.cv, (0, 0), text="h")
        state, text = widget.style.states[0], widget.elements[-1].name

        widget.style.set("light", fg=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        widget.style.set("dark", fg=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)

    def test_icon_button(self) -> None:
        widget = widgets.IconButton(self.cv, (0, 0), (60, 30), text="i")
        state = widget.style.states[0]
        shape, text = widget.elements[0].name, widget.elements[-1].name

        widget.style.set("light", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["outline"], COLOR)
        widget.style.set("dark", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["outline"], COLOR)

    def test_toggle(self) -> None:
        widget = widgets.ToggleButton(self.cv, (0, 0), text="t")
        state = widget.style.states[0]
        shape, text = widget.elements[0].name, widget.elements[-1].name

        widget.style.set("light", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["outline"], COLOR)
        widget.style.set("dark", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["outline"], COLOR)

    def test_checkbox(self) -> None:
        widget = widgets.CheckBox(self.cv, (0, 0))
        state = widget.style.states[0]
        shape, text = widget.elements[0].name, widget.elements[-1].name

        widget.style.set("light", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.light[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["outline"], COLOR)
        widget.style.set("dark", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.dark[text][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["outline"], COLOR)


class TestSwitchStyles(StyleTestMixin, unittest.TestCase):

    def test_switch(self) -> None:
        widget = widgets.Switch(self.cv, (0, 0))
        state = widget.style.states[0]

        widget.style.set("light", bg_slot=COLOR, ol_slot=COLOR, bg_dot=COLOR)
        self.assertEqual(widget.style.light["SemicircularRectangle"][state]["fill"], COLOR)
        self.assertEqual(widget.style.light["SemicircularRectangle"][state]["outline"], COLOR)
        self.assertEqual(widget.style.light["Oval"][state]["fill"], COLOR)
        widget.style.set("dark", bg_slot=COLOR, ol_slot=COLOR, bg_dot=COLOR)
        self.assertEqual(widget.style.dark["SemicircularRectangle"][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark["SemicircularRectangle"][state]["outline"], COLOR)
        self.assertEqual(widget.style.dark["Oval"][state]["fill"], COLOR)


class TestInputStyles(StyleTestMixin, unittest.TestCase):

    def test_input_box(self) -> None:
        widget = widgets.InputBox(self.cv, (0, 0), (100, 30))
        state = widget.style.states[0]

        widget.style.set("light", fg=COLOR, bg=COLOR, ol=COLOR, bg_bar=COLOR)
        self.assertEqual(widget.style.light["SingleLineText"][state]["fill"], COLOR)
        self.assertEqual(widget.style.light["RoundedRectangle.in"][state]["fill"], COLOR)
        self.assertEqual(widget.style.light["RoundedRectangle.in"][state]["outline"], COLOR)
        self.assertEqual(widget.style.light["RoundedRectangle.out"][state]["fill"], COLOR)
        self.assertEqual(widget.style.light["RoundedRectangle.out"][state]["outline"], COLOR)
        widget.style.set("dark", fg=COLOR, bg=COLOR, ol=COLOR, bg_bar=COLOR)
        self.assertEqual(widget.style.dark["SingleLineText"][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark["RoundedRectangle.in"][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark["RoundedRectangle.in"][state]["outline"], COLOR)
        self.assertEqual(widget.style.dark["RoundedRectangle.out"][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark["RoundedRectangle.out"][state]["outline"], COLOR)


class TestRadioStyles(StyleTestMixin, unittest.TestCase):

    def test_radio_box(self) -> None:
        widget = widgets.RadioBox(self.cv, (0, 0))
        state = widget.style.states[0]
        box, dot = widget.elements[0].name, widget.elements[1].name

        widget.style.set("light", bg_box=COLOR, ol_box=COLOR, bg_dot=COLOR, ol_dot=COLOR)
        self.assertEqual(widget.style.light[box][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[box][state]["outline"], COLOR)
        self.assertEqual(widget.style.light[dot][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[dot][state]["outline"], COLOR)
        widget.style.set("dark", bg_box=COLOR, ol_box=COLOR, bg_dot=COLOR, ol_dot=COLOR)
        self.assertEqual(widget.style.dark[box][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[box][state]["outline"], COLOR)
        self.assertEqual(widget.style.dark[dot][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[dot][state]["outline"], COLOR)


class TestProgressStyles(StyleTestMixin, unittest.TestCase):

    def test_progress_bar(self) -> None:
        widget = widgets.ProgressBar(self.cv, (0, 0), (100, 20))
        state = widget.style.states[0]
        slot, bar = widget.elements[0].name, widget.elements[1].name

        widget.style.set("light", bg_slot=COLOR, ol_slot=COLOR, bg_bar=COLOR, ol_bar=COLOR)
        self.assertEqual(widget.style.light[slot][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[slot][state]["outline"], COLOR)
        self.assertEqual(widget.style.light[bar][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[bar][state]["outline"], COLOR)
        widget.style.set("dark", bg_slot=COLOR, ol_slot=COLOR, bg_bar=COLOR, ol_bar=COLOR)
        self.assertEqual(widget.style.dark[slot][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[slot][state]["outline"], COLOR)
        self.assertEqual(widget.style.dark[bar][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[bar][state]["outline"], COLOR)


class TestSliderStyles(StyleTestMixin, unittest.TestCase):

    def test_slider(self) -> None:
        widget = widgets.Slider(self.cv, (0, 0), (100, 30))
        state = widget.style.states[0]
        slot, line, pointer = (widget.elements[0].name,
                               widget.elements[1].name,
                               widget.elements[2].name)

        widget.style.set("light", fg_slot=COLOR, bg_slot=COLOR, bg_pnt=COLOR, bg_dot=COLOR)
        self.assertEqual(widget.style.light[slot][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[slot][state]["outline"], COLOR)
        self.assertEqual(widget.style.light[line][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[line][state]["outline"], COLOR)
        self.assertEqual(widget.style.light[pointer][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[pointer][state]["outline"], COLOR)
        self.assertEqual(widget.style.light["Oval.in"][state]["fill"], COLOR)
        self.assertEqual(widget.style.light["Oval.in"][state]["outline"], COLOR)
        widget.style.set("dark", fg_slot=COLOR, bg_slot=COLOR, bg_pnt=COLOR, bg_dot=COLOR)
        self.assertEqual(widget.style.dark[slot][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[slot][state]["outline"], COLOR)
        self.assertEqual(widget.style.dark[line][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[pointer][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark["Oval.in"][state]["fill"], COLOR)


class TestSegmentedStyles(StyleTestMixin, unittest.TestCase):

    def test_segmented(self) -> None:
        widget = widgets.SegmentedButton(self.cv, (0, 0), text=("a", "b"))
        state, shape = widget.style.states[0], widget.elements[0].name

        widget.style.set("light", bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.light[shape][state]["outline"], COLOR)
        widget.style.set("dark", bg=COLOR, ol=COLOR)
        self.assertEqual(widget.style.dark[shape][state]["fill"], COLOR)
        self.assertEqual(widget.style.dark[shape][state]["outline"], COLOR)


class TestSpinnerTooltipStyles(StyleTestMixin, unittest.TestCase):

    def test_spinner(self) -> None:
        widget = widgets.Spinner(self.cv, (0, 0))
        state = widget.style.states[0]
        oval, arc = widget.elements[0].name, widget.elements[1].name

        widget.style.set("light", fg=COLOR, bg=COLOR)
        self.assertEqual(widget.style.light[oval][state]["outline"], COLOR)
        self.assertEqual(widget.style.light[arc][state]["outline"], COLOR)
        widget.style.set("dark", fg=COLOR, bg=COLOR)
        self.assertEqual(widget.style.dark[oval][state]["outline"], COLOR)
        self.assertEqual(widget.style.dark[arc][state]["outline"], COLOR)

    def test_tooltip(self) -> None:
        button = widgets.Button(self.cv, (0, 0), text="b")
        tooltip = widgets.Tooltip(button, text="t")
        state = tooltip.style.states[0]
        shape, text = tooltip.elements[0].name, tooltip.elements[-1].name

        tooltip.style.set("light", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(tooltip.style.light[text][state]["fill"], COLOR)
        self.assertEqual(tooltip.style.light[shape][state]["fill"], COLOR)
        self.assertEqual(tooltip.style.light[shape][state]["outline"], COLOR)
        tooltip.style.set("dark", fg=COLOR, bg=COLOR, ol=COLOR)
        self.assertEqual(tooltip.style.dark[text][state]["fill"], COLOR)
        self.assertEqual(tooltip.style.dark[shape][state]["fill"], COLOR)
        self.assertEqual(tooltip.style.dark[shape][state]["outline"], COLOR)


class TestVirtualStyle(StyleTestMixin, unittest.TestCase):

    def test_init_get_reset(self) -> None:
        widget = widgets.Button(self.cv, (0, 0), text="b")
        style = widget.style

        style.init(0)
        style.init("Information", theme="light")
        style.init("Information", theme="dark")

        self.assertEqual(style[0], style[widget.elements[0].name])
        self.assertIsInstance(style["Information"], dict)

        style.get(theme="light")
        style.get(theme="dark")
        style.get()

        style.detach()
        style.reset(theme="light")
        style.reset(theme="dark")
        style.reset()

    def test_get_disabled_style(self) -> None:
        widget = widgets.Button(self.cv, (0, 0), text="b")
        widget.disable()
        self.assertIn("disabled", widget.style.get()["Information"])
        widget.disable(False)

    def test_multi_state_color(self) -> None:
        widget = widgets.Switch(self.cv, (0, 0))
        colors = ("#111111", "#222222", "#333333", "#444444", "#555555", "#666666")
        widget.style.set(None, bg_slot=colors)

        for color, state in zip(colors, widget.style.states):
            self.assertEqual(widget.style.light["SemicircularRectangle"][state]["fill"], color)
            self.assertEqual(widget.style.dark["SemicircularRectangle"][state]["fill"], color)

    def test_wrap_arg(self) -> None:
        self.assertEqual(virtual.Style._wrap_arg("x"), ("x",))
        self.assertEqual(virtual.Style._wrap_arg(("x", "y")), ("x", "y"))


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
