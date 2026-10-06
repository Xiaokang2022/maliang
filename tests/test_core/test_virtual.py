# pylint: disable=C0111

import contextlib
import copy
import doctest
import io
import os.path
import unittest
import warnings

import tests
from maliang.core import containers, virtual


def load_tests(loader: unittest.TestLoader, tests: unittest.TestSuite, pattern: str | None) -> unittest.TestSuite:
    del loader, pattern
    tests.addTests(doctest.DocTestSuite(virtual))
    return tests


class _Element(virtual.Element):
    """A minimal concrete element, so that `virtual.Element` can be tested alone.

    Its ``zoom`` method is therefore the one of ``virtual.Element`` (it does not
    inherit the one of ``virtual.Shape``).
    """

    def display(self) -> None:
        self.items.append(self.widget.master.create_rectangle(
            *self.region(), fill="black", tags=("fill", "bg")))

    def coords(self, size=None, position=None) -> None:
        super().coords(size, position)
        if self.items:
            self.widget.master.coords(self.items[0], *self.region())


class _Rect(_Element, virtual.Shape):
    """A minimal concrete shape, so that a widget really owns a shape."""


class _EmptyText(virtual.Text):
    """A text element that never draws anything (its ``items`` stays empty)."""

    def display(self) -> None:
        pass

    def coords(self, size=None, position=None) -> None:
        super().coords(size, position)


class _EmptyImage(virtual.Image):
    """An image element that never draws anything (its ``items`` stays empty)."""

    def display(self) -> None:
        pass

    def coords(self, size=None, position=None) -> None:
        super().coords(size, position)


class _Style(virtual.Style):
    """A style with data, used to test the style of a widget that has elements."""

    light: dict[str, dict[str, dict[str, str]]] = {
        "_Rect": {"normal": {"bg": "#FFFFFF", "outline": "#000000"}},
    }
    dark: dict[str, dict[str, dict[str, str]]] = {
        "_Rect": {"normal": {"bg": "#000000", "outline": "#FFFFFF"}},
    }


class CanvasTestCase(unittest.TestCase):
    """Base case that provides a canvas whose size has been initialized."""

    def setUp(self) -> None:
        self.tk = tests.window()
        self.cv = containers.Canvas(self.tk)
        self.cv.place(width=200, height=200)
        self.cv.update()
        self.cv._initialization()  # needed by `containers.Canvas.ratios`

    def tearDown(self) -> None:
        self.tk.destroy()

    def make_widget(self, position=(0, 0), size=(50, 50), **kwargs) -> virtual.Widget:
        # Animations are disabled unless a test asks for them: a gradient
        # animation keeps running on the shared root window, so a widget that is
        # destroyed before the animation ends makes the output noisy.
        kwargs.setdefault("gradient_animation", False)
        return virtual.Widget(self.cv, position, size, **kwargs)

    def item_coords(self, item) -> tuple[int, ...]:
        return tuple(round(value) for value in self.cv.coords(item))


class TestFeature(CanvasTestCase):

    def test_parse_method_name(self) -> None:
        for name, method in (
            ("<Motion>", "_motion"),
            ("<Button-1>", "_button_1"),
            ("<ButtonRelease-1>", "_button_release_1"),
            ("<B1-Motion>", "_b_1_motion"),
            ("<MouseWheel>", "_mouse_wheel"),
            ("<<Copy>>", "_copy"),
        ):
            self.assertEqual(virtual.Feature._parse_method_name(name), method)

    def test_get_method_falls_back_to_a_no_op(self) -> None:
        # `virtual.Feature` itself implements no event method at all
        feature = virtual.Feature(self.make_widget())
        self.assertFalse(feature.get_method("<Motion>")(None))
        self.assertFalse(feature.get_method("<Button-1>")(None))

    def test_get_method_runs_extra_commands(self) -> None:
        feature = virtual.Feature(self.make_widget())
        called = []
        feature.extra_commands["<Motion>"] = [called.append]

        self.assertFalse(feature.get_method("<Motion>")(None))
        self.assertEqual(called, [None])

    def test_get_method_reports_a_failing_extra_command(self) -> None:
        feature = virtual.Feature(self.make_widget())

        def broken(_event) -> None:
            raise RuntimeError("an extra command must not break the event")

        feature.extra_commands["<Motion>"] = [broken]

        with contextlib.redirect_stderr(io.StringIO()) as captured:
            feature.get_method("<Motion>")(None)

        # The failure is reported instead of being raised
        self.assertIn("RuntimeError", captured.getvalue())
        self.assertIn("must not break the event", captured.getvalue())


class TestElement(CanvasTestCase):

    def test_geometry(self) -> None:
        element = _Element(self.make_widget((10, 20), (40, 60)))

        self.assertEqual(element.position, (10, 20))
        self.assertEqual(element.size, (40, 60))
        self.assertEqual(element.region(), (10, 20, 50, 80))
        self.assertEqual(element.center(), (30, 50))

        # The borders belong to the element
        self.assertTrue(element.detect(10, 20))
        self.assertTrue(element.detect(50, 80))
        self.assertFalse(element.detect(9, 20))
        self.assertFalse(element.detect(10, 81))

    def test_move_and_moveto_move_the_canvas_item(self) -> None:
        element = _Element(self.make_widget((10, 20), (40, 60)))
        item = element.items[0]
        self.assertEqual(self.item_coords(item), (10, 20, 50, 80))

        element.move(5, -5)
        self.assertEqual(element.position, (15, 15))
        self.assertEqual(self.item_coords(item), (15, 15, 55, 75))

        element.moveto(10, 20)
        self.assertEqual(element.position, (10, 20))
        self.assertEqual(self.item_coords(item), (10, 20, 50, 80))

    def test_zoom(self) -> None:
        element = _Element(self.make_widget((10, 10), (40, 60)))

        element.zoom((2, 2))

        self.assertEqual(element.size, (80, 120))
        self.assertEqual(element.position, (20, 20))
        self.assertEqual(self.item_coords(element.items[0]), (20, 20, 100, 140))

    def test_zoom_only_the_size(self) -> None:
        element = _Element(self.make_widget((10, 10), (40, 60)))

        element.zoom((2, 2), zoom_position=False)

        self.assertEqual(element.position, (10, 10))
        self.assertEqual(element.size, (80, 120))
        # The item is scaled around the (unchanged) position
        self.assertEqual(self.item_coords(element.items[0]), (10, 10, 90, 130))

    def test_zoom_only_the_position(self) -> None:
        element = _Element(self.make_widget((10, 10), (40, 60)))

        element.zoom((2, 2), zoom_size=False)

        self.assertEqual(element.size, (40, 60))
        self.assertEqual(element.position, (20, 20))
        # The item is moved to the scaled position, and its size is untouched.
        # `Canvas.moveto` may be off by one pixel, it works on the bounding box
        # of the item rather than on the first coordinate pair of it.
        x1, y1, x2, y2 = self.item_coords(element.items[0])
        self.assertAlmostEqual(x1, element.position[0]*2, delta=1)
        self.assertAlmostEqual(y1, element.position[1]*2, delta=1)
        self.assertEqual((x2-x1, y2-y1), (40, 60))

    def test_zoom_nothing_warns(self) -> None:
        element = _Element(self.make_widget((10, 10), (40, 60)))

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            element.zoom((2, 2), zoom_position=False, zoom_size=False)

        self.assertEqual(len(caught), 1)
        self.assertIs(caught[0].category, UserWarning)
        self.assertEqual(element.size, (40, 60))
        self.assertEqual(element.position, (10, 10))

    def test_configure_a_plain_color(self) -> None:
        element = _Element(self.make_widget())

        # The tags of the item are `(key, arg)` pairs, `bg` is the arg here
        element.configure({"bg": "#FF0000"}, gradient_animation=False)
        self.assertEqual(self.cv.itemcget(element.items[0], "fill"), "#FF0000")

        # Only the args that are present in the style are updated
        element.configure({"outline": "#00FF00"}, gradient_animation=False)
        self.assertEqual(self.cv.itemcget(element.items[0], "fill"), "#FF0000")

    def test_configure_blends_an_alpha_color_with_the_background(self) -> None:
        self.cv.configure(bg="#000000")
        element = _Element(self.make_widget())

        # A fully opaque color is used as it is
        element.configure({"bg": "#FF0000FF"}, gradient_animation=False)
        self.assertEqual(self.cv.itemcget(element.items[0], "fill"), "#FF0000")

        # A fully transparent color is the background color
        element.configure({"bg": "#FF000000"}, gradient_animation=False)
        self.assertEqual(self.cv.itemcget(element.items[0], "fill"), "#000000")

    def test_configure_an_empty_value(self) -> None:
        element = _Element(self.make_widget())

        element.configure({"bg": ""}, gradient_animation=False)
        self.assertEqual(self.cv.itemcget(element.items[0], "fill"), "")

    def test_configure_starts_a_gradient_animation(self) -> None:
        element = _Element(self.make_widget(gradient_animation=True))

        # `gradient_animation` defaults to `True`, so the color is transitioned
        # by an animation instead of being set directly
        element.configure({"bg": "#00FF00"})
        self.assertEqual(len(element.gradients), 1)
        self.assertTrue(element.gradients[0].active)
        self.assertEqual(self.cv.itemcget(element.items[0], "fill"), "black")

        # Destroying the element stops the animation
        element.destroy()
        self.assertFalse(element.gradients[0].active)

    def test_forget(self) -> None:
        element = _Element(self.make_widget())

        self.assertTrue(element.visible)
        element.forget()
        self.assertFalse(element.visible)
        element.forget(False)
        self.assertTrue(element.visible)

    def test_destroy_deregisters_and_deletes_the_items(self) -> None:
        widget = self.make_widget()
        element = _Rect(widget)
        item = element.items[0]
        self.assertIn(item, self.cv.find_all())
        self.assertIn(element, widget.shapes)

        element.destroy()

        self.assertNotIn(item, self.cv.find_all())
        self.assertNotIn(element, widget.shapes)


class TestTextAndImage(CanvasTestCase):

    def test_text_region_falls_back_to_the_geometric_region(self) -> None:
        text = _EmptyText(self.make_widget((5, 6), (40, 60)))

        self.assertEqual(text.items, [])
        self.assertEqual(text.region(), (5, 6, 45, 66))

    def test_image_region_falls_back_to_the_geometric_region(self) -> None:
        image = _EmptyImage(self.make_widget((5, 6), (40, 60)))

        self.assertEqual(image.items, [])
        self.assertEqual(image.region(), (5, 6, 45, 66))

    def test_zoom_an_empty_image(self) -> None:
        image = _EmptyImage(self.make_widget())

        with self.assertRaises(RuntimeError):
            image.zoom((2, 2))


class TestStyle(CanvasTestCase):

    def prepare(self) -> tuple[virtual.Widget, virtual.Style, virtual.Element]:
        """Detach the style of a widget and give an element of it every state."""
        widget = self.make_widget()
        style = widget.style.detach()
        element = _Rect(widget, name=".a")
        style.init(element)
        for data in (style.light, style.dark):
            for state in style.states:
                data[element.name].setdefault(state, {})
        return widget, style, element

    def test_auto_update_follows_the_widget_unless_it_is_given(self) -> None:
        widget = self.make_widget(auto_update=False)
        self.assertFalse(widget.auto_update)
        self.assertIs(virtual.Style(widget).auto_update, widget.auto_update)

        # An explicit value is used as it is
        self.assertTrue(virtual.Style(widget, auto_update=True).auto_update)
        self.assertFalse(virtual.Style(widget, auto_update=False).auto_update)

    def test_init_only_the_requested_theme(self) -> None:
        widget = self.make_widget()
        style = widget.style.detach()
        element = _Rect(widget, name=".a")

        style.init(element, theme="light")
        self.assertIn(element.name, style.light)
        self.assertNotIn(element.name, style.dark)

        style.init(element, theme="dark")
        self.assertIn(element.name, style.dark)

    def test_getitem_by_element_name_and_index(self) -> None:
        widget = self.make_widget()
        element = _Rect(widget, name=".a")
        data = {element.name: {"normal": {"bg": "#123456"}}}
        widget.style.light = copy.deepcopy(data)
        widget.style.dark = copy.deepcopy(data)

        self.assertEqual(widget.style[element], {"normal": {"bg": "#123456"}})
        self.assertEqual(widget.style[element.name], {"normal": {"bg": "#123456"}})
        self.assertEqual(widget.style[0], {"normal": {"bg": "#123456"}})
        self.assertEqual(widget.style["NotExisting"], {})

    def test_set_the_colors_of_one_theme(self) -> None:
        _, style, element = self.prepare()

        style._set("light", "#112233", bg=element)
        self.assertEqual(style.light[element.name]["normal"]["bg"], "#112233")
        self.assertEqual(style.dark[element.name]["normal"], {})

        style._set("dark", "#445566", bg=element)
        self.assertEqual(style.dark[element.name]["normal"]["bg"], "#445566")

        style._set(None, "#778899", bg=element)
        self.assertEqual(style.light[element.name]["normal"]["bg"], "#778899")
        self.assertEqual(style.dark[element.name]["normal"]["bg"], "#778899")

    def test_set_the_colors_of_several_states(self) -> None:
        _, style, element = self.prepare()

        # `Ellipsis` skips the state at the same position
        style._set(None, (Ellipsis, "#00FF00"), bg=element)
        self.assertNotIn("bg", style.light[element.name]["normal"])
        self.assertEqual(
            style.light[element.name][style.states[1]]["bg"], "#00FF00")

    def test_set_without_data_does_nothing(self) -> None:
        _, style, element = self.prepare()

        style._set(None, None, bg=element)

        for data in (style.light, style.dark):
            for state in style.states:
                self.assertEqual(data[element.name][state], {})

    def test_reset_detaches_the_style_from_the_class_data(self) -> None:
        widget = self.make_widget()
        style = widget.style.detach()

        self.assertIsNot(style.light, virtual.Style.light)
        self.assertIsNot(style.dark, virtual.Style.dark)

        style.reset()

        self.assertIs(style.light, virtual.Style.light)
        self.assertIs(style.dark, virtual.Style.dark)

    def test_get_disabled_style(self) -> None:
        _, style, element = self.prepare()
        style._set(None, "#00FF00", bg=element)

        disabled = style.get_disabled_style(element=element)

        self.assertNotEqual(disabled["bg"], "#00FF00")
        # The result is cached into the style data
        self.assertEqual(style[element]["disabled"], disabled)
        self.assertIs(style.get_disabled_style(element=element), disabled)

    def test_get_disabled_style_keeps_empty_values(self) -> None:
        _, style, element = self.prepare()
        for data in (style.light, style.dark):
            data[element.name]["normal"] = {"bg": "", "outline": "#00FF00"}

        disabled = style.get_disabled_style(element=element)

        # An empty color is not a color, it must not be transitioned
        self.assertEqual(disabled["bg"], "")
        self.assertNotEqual(disabled["outline"], "#00FF00")


class TestWidget(CanvasTestCase):

    def test_hierarchy(self) -> None:
        parent = self.make_widget((10, 10), (100, 100))
        child = virtual.Widget(parent, (5, 5), (20, 20))

        self.assertTrue(child.nested)
        self.assertIs(child.widget, parent)
        self.assertIs(child.master, self.cv)
        self.assertIn(child, parent.children)
        self.assertIn(child, self.cv.widgets)
        # The position of a nested widget is relative to its parent
        self.assertEqual(child.position, (15, 15))
        self.assertEqual(child.size, (20, 20))

    def test_region_and_center_depend_on_the_anchor(self) -> None:
        widget = self.make_widget((100, 100), (40, 20), anchor="center")

        self.assertEqual(widget.offset, (20, 10))
        self.assertEqual(widget.region(), (80, 90, 120, 110))
        self.assertEqual(widget.center(), (100, 100))
        self.assertTrue(widget.detect(80, 90))
        self.assertTrue(widget.detect(120, 110))
        self.assertFalse(widget.detect(79, 90))
        self.assertFalse(widget.detect(100, 111))

    def test_update_nested(self) -> None:
        parent = self.make_widget()
        child = virtual.Widget(parent, (0, 0), (10, 10))

        parent.update("hover", nested=True)

        self.assertEqual(parent.state, "hover")
        self.assertEqual(child.state, "hover")

    def test_bind_with_and_without_auto_detect(self) -> None:
        widget = self.make_widget((10, 10), (50, 50))
        detected, undetected = [], []

        widget.bind("<Motion>", detected.append)
        widget.bind("<Motion>", undetected.append, auto_detect=False)
        self.assertEqual(len(widget.feature.extra_commands["<Motion>"]), 2)

        widget.generate_event("<Motion>", x=20, y=20)
        self.assertEqual(len(detected), 1)
        self.assertEqual(len(undetected), 1)

        # `auto_detect=True` drops the events that are outside of the widget
        widget.generate_event("<Motion>", x=9999, y=9999)
        self.assertEqual(len(detected), 1)
        self.assertEqual(len(undetected), 2)

    def test_unbind(self) -> None:
        widget = self.make_widget()

        widget.bind("<Motion>", lambda _event: None, auto_detect=False)
        command = widget.feature.extra_commands["<Motion>"][0]
        widget.unbind("<Motion>", command)

        self.assertEqual(widget.feature.extra_commands["<Motion>"], [])

    def test_disable_propagates_and_skips_images(self) -> None:
        parent = self.make_widget(style=_Style)
        child = virtual.Widget(parent, (0, 0), (10, 10), style=_Style)
        shape = _Rect(parent)
        image = _EmptyImage(parent)

        parent.disable()
        self.assertEqual(parent.state, "disabled")
        self.assertEqual(child.state, "disabled")
        self.assertEqual(parent.state_before_disabled, "normal")
        # An `Image` has no style, so no disabled style is computed for it
        self.assertIn("disabled", parent.style[shape])
        self.assertEqual(parent.style[image.name], {})

        parent.disable(False)
        self.assertEqual(parent.state, "normal")
        self.assertEqual(child.state, "normal")
        self.assertEqual(parent.state_before_disabled, "")
        self.assertTrue(image.visible)

    def test_forget_propagates_to_the_children(self) -> None:
        parent = self.make_widget()
        child = virtual.Widget(parent, (0, 0), (10, 10))
        shape = _Rect(parent)
        element = _Rect(child)

        parent.forget()
        self.assertTrue(parent.disappeared)
        self.assertTrue(child.disappeared)
        self.assertFalse(shape.visible)
        self.assertFalse(element.visible)

        parent.forget(False)
        self.assertFalse(parent.disappeared)
        self.assertTrue(shape.visible)
        self.assertTrue(element.visible)

    def test_lift_raises_the_items_and_the_children(self) -> None:
        first = self.make_widget((0, 0), (10, 10))
        second = self.make_widget((20, 20), (10, 10))
        first_shape = _Rect(first)
        _Rect(second)
        virtual.Widget(second, (0, 0), (5, 5))
        other_child = virtual.Widget(second, (0, 0), (5, 5))

        self.assertIsNone(first.lift())
        self.assertEqual(self.cv.find_all()[-1], first_shape.items[0])
        self.assertIs(self.cv.widgets[-1], first)

        # The children of a lifted widget are lifted too
        second.lift()
        self.assertIs(self.cv.widgets[-1], other_child)

    def test_move_and_moveto_propagate_to_the_children(self) -> None:
        parent = self.make_widget((10, 10), (100, 100))
        child = virtual.Widget(parent, (10, 10), (20, 20))
        shape = _Rect(child)
        self.assertEqual(self.item_coords(shape.items[0]), (20, 20, 40, 40))

        parent.move(5, 7)
        self.assertEqual(parent.position, (15, 17))
        self.assertEqual(child.position, (25, 27))
        self.assertEqual(self.item_coords(shape.items[0]), (25, 27, 45, 47))

        parent.moveto(0, 0)
        self.assertEqual(parent.position, (0, 0))
        self.assertEqual(child.position, (10, 10))
        self.assertEqual(self.item_coords(shape.items[0]), (10, 10, 30, 30))

    def test_zoom_uses_the_canvas_ratios_by_default(self) -> None:
        self.cv._size = 400, 400
        self.cv.__dict__.pop("ratios", None)  # `ratios` is a cached property
        self.assertEqual(self.cv.ratios, (2.0, 2.0))

        parent = self.make_widget((10, 10), (100, 100))
        child = virtual.Widget(parent, (10, 10), (20, 20))
        shape = _Rect(child)

        parent.zoom()

        self.assertEqual(parent.size, (200, 200))
        self.assertEqual(parent.position, (20, 20))
        self.assertEqual(child.size, (40, 40))
        self.assertEqual(child.position, (40, 40))
        self.assertEqual(shape.size, (40, 40))

    def test_destroy(self) -> None:
        widget = self.make_widget()
        element = _Rect(widget)

        self.assertTrue(widget.exists())
        widget.destroy()

        self.assertFalse(widget.exists())
        self.assertNotIn(widget, self.cv.widgets)
        self.assertNotIn(element.items[0], self.cv.find_all())


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
