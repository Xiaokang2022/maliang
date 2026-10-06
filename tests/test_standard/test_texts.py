# pylint: disable=C0111

import os.path
import unittest
import warnings

import tests
from maliang.core import containers, virtual
from maliang.standard import texts, widgets


class TestInformation(unittest.TestCase):

    def test_via_text_widget(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = widgets.Text(cv, (0, 0), text="hello")
                self.assertEqual(widget.get(), "hello")
                widget.set("world")
                self.assertEqual(widget.get(), "world")
                self.assertTrue(widget.auto_resize)

    def test_direct(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (200, 30))
                info = texts.Information(widget, text="abc", limit=5)

                self.assertEqual(info.get(), "abc")
                info.set("abcdefg")  # truncated by limit
                self.assertEqual(info.get(), "abcde")

                info.append("XYZ")  # truncated by limit
                self.assertEqual(info.get(), "abcde")

                info.delete(2)
                self.assertEqual(info.get(), "abc")
                info.delete(100)
                self.assertEqual(info.get(), "")

                info.clear()
                self.assertEqual(info.get(), "")

                info.set("no limit")
                info.destroy()

    def test_no_limit(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (200, 30))
                info = texts.Information(widget, text="a")
                info.set("a very long text that is not limited")
                self.assertEqual(info.get(), "a very long text that is not limited")
                info.append("!")
                self.assertEqual(info.get(), "a very long text that is not limited!")


class TestCanvasTextProxy(unittest.TestCase):

    def setUp(self) -> None:
        self.tk = tests.window()
        self.cv = containers.Canvas(self.tk)
        self.widget = virtual.Widget(self.cv, (0, 0), (200, 30))

    def tearDown(self) -> None:
        self.tk.destroy()

    def _make(self, **kwargs) -> texts.SingleLineText:
        return texts.SingleLineText(self.widget, size=(200, 30), **kwargs)

    def test_basic(self) -> None:
        text = self._make(text="hello")
        proxy = text.text_proxy

        self.assertEqual(proxy.length(), 5)
        self.assertEqual(proxy.get(), "hello")

        proxy.set("world")
        self.assertEqual(proxy.get(), "world")

        proxy.insert(0, "X")
        self.assertEqual(proxy.get(), "Xworld")

        proxy.append("Y")
        self.assertEqual(proxy.get(), "XworldY")

        proxy.remove(0)
        self.assertEqual(proxy.get(), "worldY")

        proxy.remove(0, 2)
        self.assertEqual(proxy.get(), "rldY")

        self.assertEqual(proxy.pop(), "Y")
        self.assertEqual(proxy.get(), "rld")

        proxy.clear()
        self.assertEqual(proxy.get(), "")

    def test_index_errors(self) -> None:
        text = self._make(text="hello")
        proxy = text.text_proxy
        self.assertRaises(IndexError, proxy._get_index, 100)
        self.assertRaises(IndexError, proxy._get_index, -100)
        self.assertEqual(proxy._get_index(-1), 4)

    def test_show(self) -> None:
        text = self._make(text="secret", show="*")
        proxy = text.text_proxy
        self.assertEqual(proxy.get(), "secret")
        proxy.set("abcd", show="*")
        self.assertEqual(proxy.get(), "****")
        proxy.insert(0, "xy", show="*")
        self.assertEqual(proxy.get(), "******")

    def test_select(self) -> None:
        text = self._make(text="hello world")
        proxy = text.text_proxy

        self.assertIsNone(proxy.select_get())
        proxy.select_set(0, 5)
        self.assertEqual(proxy.select_get(), (0, 5))
        proxy.select_clear()
        self.assertIsNone(proxy.select_get())

        proxy.select_all()
        self.assertEqual(proxy.select_get(), (0, 11))
        proxy.select_clear()

        proxy.select_set(2)
        self.assertEqual(proxy.select_get(), (2, 3))

    def test_cursor(self) -> None:
        text = self._make(text="hello world")
        proxy = text.text_proxy

        proxy.cursor_set(3)
        self.assertEqual(proxy.cursor_get(), 3)

        self.assertIsInstance(proxy.cursor_find(0), int)
        self.assertIsInstance(proxy.cursor_find(1000), int)

    def test_cursor_find_end(self) -> None:
        text = self._make(text="abc")
        proxy = text.text_proxy
        self.assertEqual(proxy.cursor_find(10000), 3)


class TestSingleLineText(unittest.TestCase):

    def setUp(self) -> None:
        self.tk = tests.window()
        self.cv = containers.Canvas(self.tk)
        self.widget = virtual.Widget(self.cv, (0, 0), (200, 30))

    def tearDown(self) -> None:
        self.tk.destroy()

    def make(self, **kwargs) -> texts.SingleLineText:
        return texts.SingleLineText(self.widget, size=(200, 30), **kwargs)

    def test_get_set(self) -> None:
        text = self.make()
        self.assertTrue(text.set("hello"))
        self.assertEqual(text.get(), "hello")
        self.assertTrue(text.append(" world"))
        self.assertEqual(text.get(), "hello world")
        self.assertTrue(text.insert(0, ">> "))
        self.assertEqual(text.get(), ">> hello world")

    def test_ignore(self) -> None:
        text = self.make(ignore="\n\r")
        text.set("line1\nline2\rline3")
        self.assertEqual(text.get(), "line1line2line3")

    def test_limit(self) -> None:
        text = self.make(limit=5)
        self.assertTrue(text.set("abc"))
        self.assertFalse(text.append("defgh"))
        self.assertEqual(text.get(), "abc")

    def test_remove(self) -> None:
        text = self.make()
        text.set("hello world")
        text.remove(0)
        self.assertEqual(text.text_proxy.get(), "ello world")
        text.remove(0, 3)
        self.assertEqual(text.text_proxy.get(), "o world")
        text.remove(3, 0)
        self.assertEqual(text.text_proxy.get(), "orld")
        text.remove(0, 4)
        self.assertEqual(text.text_proxy.get(), "")

    def test_remove_empty(self) -> None:
        text = self.make()
        self.assertIsNone(text.remove(0))

    def test_pop(self) -> None:
        text = self.make()
        text.set("hello")
        self.assertEqual(text.pop(), "o")
        self.assertEqual(text.get(), "hell")
        self.assertEqual(text.pop(0), "h")

    def test_clear(self) -> None:
        text = self.make()
        text.set("hello")
        text.clear()
        self.assertEqual(text.get(), "")
        self.assertEqual(text.text_proxy.length(), 0)

    def test_placeholder(self) -> None:
        text = self.make(placeholder="type here")
        self.assertEqual(self.cv.itemcget(text.items[1], "text"), "type here")
        text.set("x")
        self.assertEqual(self.cv.itemcget(text.items[1], "fill"), "")
        text.remove(0)
        self.assertEqual(self.cv.itemcget(text.items[1], "fill"), "#787878")
        text.clear()

    def test_align(self) -> None:
        for align, anchor in (("left", "w"), ("right", "e"), ("center", "center")):
            text = self.make(align=align)
            self.assertEqual(text.anchor, anchor)
            text.coords((200, 30), (0, 0))

    def test_overflow_end(self) -> None:
        widget = virtual.Widget(self.cv, (0, 0), (60, 20))
        text = texts.SingleLineText(widget, size=(60, 20))
        text.append("a" * 50)
        self.assertLess(text.text_proxy.length(), 50)

    def test_overflow_middle(self) -> None:
        widget = virtual.Widget(self.cv, (0, 0), (60, 20))
        text = texts.SingleLineText(widget, size=(60, 20))
        text.append("a" * 20 + "b" * 20)
        text.insert(0, "Z")
        self.assertGreater(text.text_proxy.length(), 0)

    def test_limit_width(self) -> None:
        widget = virtual.Widget(self.cv, (0, 0), (200, 20))
        text = texts.SingleLineText(widget, size=(200, 20), limit_width=10)
        text.append("a" * 30)
        self.assertLess(text.text_proxy.length(), 30)

    def test_remove_reveal(self) -> None:
        widget = virtual.Widget(self.cv, (0, 0), (60, 20))
        text = texts.SingleLineText(widget, size=(60, 20))
        text.append("a" * 40)
        text.insert(0, "bbbbbbbbbb")
        self.assertGreater(text.left, 0)
        text.remove(0, 1)
        self.assertGreaterEqual(text.left, 0)

    def test_cursor_move(self) -> None:
        text = self.make()
        text.set("hello world")

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            text.cursor_move(1)  # no cursor
            self.assertTrue(caught)

        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            text.cursor_move_to(3)  # no cursor
            self.assertTrue(caught)

        text.text_proxy.cursor_set(5)
        text.cursor_move(1)
        self.assertEqual(text.text_proxy.cursor_get(), 6)
        text.cursor_move(-1)
        self.assertEqual(text.text_proxy.cursor_get(), 5)
        text.cursor_move_to(0)
        self.assertEqual(text.text_proxy.cursor_get(), 0)
        text.cursor_move(-1)  # at the start -> _move_right
        text.cursor_move_to(text.text_proxy.length())
        self.assertEqual(text.text_proxy.cursor_get(), text.text_proxy.length())

    def test_move_left_right(self) -> None:
        widget = virtual.Widget(self.cv, (0, 0), (60, 20))
        text = texts.SingleLineText(widget, size=(60, 20))
        text.append("a" * 40)

        # Everything was appended at the tail, so nothing is left to reveal
        self.assertEqual(text.right, len(text.text))
        self.assertEqual(text.left, len(text.text) - text.text_proxy.length())
        text._move_left()
        self.assertEqual(text.right, len(text.text))

        # Moving right hides the tail character and reveals a head character
        left, right = text.left, text.right
        text._move_right()
        self.assertEqual(text.left, left - 1)
        self.assertEqual(text.right, right - 1)

        # Moving left undoes exactly that
        text._move_left()
        self.assertEqual(text.left, left)
        self.assertEqual(text.right, right)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
