# pylint: disable=C0111

import math
import os.path
import unittest
import warnings

import tests
from maliang.core import containers, virtual
from maliang.standard import shapes


class TestLine(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (10, 10), (100, 60))
                line = shapes.Line(widget, points=[(0, 0), (10, 20)])

                self.assertEqual(line.name, "Line")
                self.assertEqual(line.center(), (60.0, 40.0))
                self.assertEqual(line.region(), (10, 10, 110, 70))
                self.assertTrue(line.detect(20, 20))
                self.assertFalse(line.detect(1000, 1000))

                line.move(5, 5)
                line.moveto(0, 0)
                line.zoom((2, 2))
                line.forget()
                line.forget(False)
                line.destroy()

                named = shapes.Line(widget, points=[(0, 0), (1, 1)], name=".n")
                self.assertEqual(named.name, "Line.n")


class TestRectangle(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                rect = shapes.Rectangle(widget)
                rect.coords((20, 30), (5, 5))
                self.assertEqual(rect.size, (20, 30))
                self.assertEqual(rect.position, (5, 5))
                rect.zoom((2, 2), zoom_position=False)
                rect.zoom((2, 2), zoom_size=False)
                rect.destroy()


class TestOval(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                oval = shapes.Oval(widget)
                self.assertTrue(oval.detect(50, 30))
                self.assertFalse(oval.detect(0, 0))
                self.assertFalse(oval.detect(-1, -1))
                oval.destroy()


class TestArc(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                arc = shapes.Arc(widget, style="arc")
                self.assertEqual(len(arc.items), 1)
                self.assertEqual(cv.itemcget(arc.items[0], "style"), "arc")
                arc.coords((40, 40), (0, 0))
                self.assertEqual(arc.region(), (0, 0, 40, 40))
                arc.destroy()


class TestRegularPolygon(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                for side in (3, 5, 6):
                    polygon = shapes.RegularPolygon(widget, side=side, angle=math.pi / 4)
                    self.assertEqual(len(polygon.items), 1)
                    polygon.coords((40, 40), (0, 0))
                    # Each vertex is a pair of coordinates
                    self.assertEqual(len(cv.coords(polygon.items[0])), side * 2)
                    polygon.destroy()

    def test_warning(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    polygon = shapes.RegularPolygon(widget, side=2)
                    polygon.coords((40, 40), (0, 0))
                    self.assertTrue(caught)


class TestRoundedRectangle(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                rect = shapes.RoundedRectangle(widget, radius=5)
                # 2 rectangles + 4 lines + 4 fill arcs + 4 outline arcs
                self.assertEqual(len(rect.items), 14)
                rect.coords((100, 60), (0, 0))
                self.assertEqual(rect.region(), (0, 0, 100, 60))
                self.assertEqual(cv.coords(rect.items[6]), [0, 0, 10, 10])
                rect.destroy()

    def test_warnings(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    # radius * 2 > width, radius * 2 > height
                    too_big = shapes.RoundedRectangle(widget, radius=100)
                    too_big.coords((20, 20), (0, 0))
                    self.assertTrue(caught)

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    # radius == 0 -> d == 0
                    zero = shapes.RoundedRectangle(widget, radius=0)
                    zero.coords((20, 20), (0, 0))
                    self.assertTrue(caught)


class TestHalfRoundedRectangle(unittest.TestCase):

    def test_left(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                rect = shapes.HalfRoundedRectangle(widget, radius=5, ignore="left")
                # 2 rectangles + 4 lines + 4 arcs
                self.assertEqual(len(rect.items), 10)
                rect.coords((100, 60), (0, 0))
                # The rounded corners are on the right side
                self.assertEqual(cv.coords(rect.items[6]), [90, 0, 100, 10])
                rect.destroy()

    def test_right(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                rect = shapes.HalfRoundedRectangle(widget, radius=5, ignore="right")
                self.assertEqual(len(rect.items), 10)
                rect.coords((100, 60), (0, 0))
                # The rounded corners are on the left side
                self.assertEqual(cv.coords(rect.items[6]), [0, 0, 10, 10])
                rect.destroy()

    def test_warnings(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    shapes.HalfRoundedRectangle(widget, radius=100).coords((20, 20), (0, 0))
                    self.assertTrue(caught)

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    shapes.HalfRoundedRectangle(widget, radius=0).coords((20, 20), (0, 0))
                    self.assertTrue(caught)


class TestSemicircularRectangle(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                rect = shapes.SemicircularRectangle(widget)
                rect.coords((100, 60), (0, 0))

                # Middle region
                self.assertTrue(rect.detect(50, 30))
                # Left circle region
                self.assertTrue(rect.detect(30, 30))
                # Right circle region
                self.assertTrue(rect.detect(70, 30))
                # Outside
                self.assertFalse(rect.detect(0, 0))
                rect.destroy()

    def test_warnings(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    shapes.SemicircularRectangle(widget).coords((100, 0), (0, 0))
                    self.assertTrue(caught)

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    shapes.SemicircularRectangle(widget).coords((100, -10), (0, 0))
                    self.assertTrue(caught)


class TestSharpRectangle(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                rect = shapes.SharpRectangle(widget, theta=math.pi / 6, ratio=(0.5, 0.5))
                self.assertEqual(len(rect.items), 1)
                rect.coords((100, 60), (0, 0))
                # 6 sharp corners -> 12 coordinates
                self.assertEqual(len(cv.coords(rect.items[0])), 12)
                self.assertEqual(rect.region(), (0, 0, 100, 60))
                rect.destroy()

    def test_init_warnings(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    shapes.SharpRectangle(widget, theta=math.pi)
                    self.assertTrue(caught)

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    shapes.SharpRectangle(widget, ratio=(0.5, 1.5))
                    self.assertTrue(caught)

    def test_coords_warnings(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    # width < height
                    shapes.SharpRectangle(widget).coords((10, 100), (0, 0))
                    self.assertTrue(caught)

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    # sum(dx) > width
                    shapes.SharpRectangle(widget, theta=math.pi / 3).coords((100, 100), (0, 0))
                    self.assertTrue(caught)


class TestParallelogram(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))
                rect = shapes.Parallelogram(widget, theta=math.pi / 6)
                self.assertEqual(len(rect.items), 1)
                rect.coords((100, 60), (0, 0))
                # 4 corners -> 8 coordinates
                self.assertEqual(len(cv.coords(rect.items[0])), 8)
                # The top and bottom edges are slanted by the same amount
                x1, _, x2, _, x3, _, x4, _ = cv.coords(rect.items[0])
                self.assertAlmostEqual(x2 - x1, x3 - x4)
                self.assertGreater(x1, x4)
                rect.destroy()

    def test_warnings(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (100, 60))

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    shapes.Parallelogram(widget, theta=math.pi)
                    self.assertTrue(caught)

                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    # dx >= width
                    shapes.Parallelogram(widget, theta=math.pi / 3).coords((10, 100), (0, 0))
                    self.assertTrue(caught)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
