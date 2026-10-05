# pylint: disable=C0111

import os.path
import unittest

from maliang.core import containers

_root: containers.Tk | None = None


def root() -> containers.Tk:
    """Get the root window shared by all test cases.

    The root window is created on the first call of this function and is never
    destroyed.

    Note:
        The windows of the test cases are `containers.Toplevel` objects of this
        root window instead of new `containers.Tk` objects, because creating and
        destroying many root windows in one process makes Tk crash on macOS: Tk
        Aqua keeps a reference to the Tcl interpreter of a destroyed root window
        (the menu bar of that interpreter stays installed in the
        `NSApplication`), so freeing that interpreter (the `Tk` object is
        collected by the cyclic garbage collector) leaves Tk Aqua with a
        dangling reference, and a later `update()` of any window then crashes
        with a `Tcl_Panic` (abort) under Tk 8.6 or a segfault under Tk 9.0. See
        <https://github.com/python/cpython/issues/123204>.
    """
    global _root  # pylint: disable=W0603
    if _root is None:
        # NOTE: The size of the window must be small enough to fit the small
        # virtual screen of some CI runners (the macOS runner only has about
        # 1176x694).
        _root = containers.Tk((200, 200))
    return _root


def window(
    size: tuple[int, int] = (200, 200),
    position: tuple[int, int] | None = None,
    **kwargs,
) -> containers.Toplevel:
    """Create a window for a test case.

    See `tests.root` for the reason why it is a `containers.Toplevel` of the
    shared root window.

    Args:
        size: size of the window.
        position: position of the window.
        kwargs: additional keyword arguments for `containers.Toplevel`.
    """
    return containers.Toplevel(root(), size, position, **kwargs)


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
