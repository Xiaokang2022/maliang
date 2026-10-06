# pylint: disable=C0111

import os.path
import unittest

import tests
from maliang.core import containers, virtual
from maliang.standard import images
from maliang.toolbox import enhanced

IMAGE = "tests/assets/images/logo.png"


class TestStillImage(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (50, 50))
                image = images.StillImage(widget, size=(50, 50))
                self.assertIsNone(image.image)
                image.coords((60, 60), (1, 1))
                image.move(1, 1)
                image.moveto(0, 0)
                image.forget()
                image.forget(False)
                image.destroy()

    def test_with_image(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                photo = enhanced.PhotoImage(file=IMAGE, master=cv)
                widget = virtual.Widget(cv, (0, 0), (50, 50))
                image = images.StillImage(widget, size=(50, 50), image=photo)
                self.assertIs(image.image, photo)
                self.assertIsInstance(image.detect(25, 25), bool)
                self.assertIsInstance(image.region()[0], int)


class TestSmoke(unittest.TestCase):

    def test_basic(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                cv.place(width=200, height=200)
                cv.update()
                cv._initialization()
                widget = virtual.Widget(cv, (0, 0), (50, 50))
                smoke = images.Smoke(widget, size=(50, 50))
                self.assertIsNotNone(smoke.image)
                self.assertIs(smoke.image, smoke.initial_image)

                smoke.coords((60, 60), (1, 1))
                smoke.zoom((2, 2))
                smoke.forget()
                smoke.forget(False)
                smoke.destroy()

    def test_named(self) -> None:
        with tests.window() as tk:
            with containers.Canvas(tk) as cv:
                widget = virtual.Widget(cv, (0, 0), (50, 50))
                smoke = images.Smoke(widget, size=(50, 50), name=".n", animation=False)
                self.assertEqual(smoke.name, "Smoke.n")


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
