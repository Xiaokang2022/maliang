# pylint: disable=C0111

"""Tests of the standard dialogs.

The dialogs of Tk are blocking: they open a native window and wait for the user
to close it. So a unit test cannot use a real dialog, and `tkinter` is the only
thing that can be replaced here. These tests therefore mock the calls of Tk and
check the arguments that the wrappers pass to it (that is the behaviour of the
wrappers), not the values that the mocked calls return.
"""

import os.path
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import unittest
import unittest.mock
import warnings

import tests
from maliang.standard import dialogs


class _FakeMaster:
    """A stand-in for a Tk window that records the Tcl calls instead of running them."""

    def __init__(self, title: str = "Fake", result: str = "ok") -> None:
        self._title = title
        self._result = result
        self.calls: list[tuple] = []
        self.registered: list = []

    def title(self) -> str:
        return self._title

    def register(self, command) -> str:
        self.registered.append(command)
        return f"registered{len(self.registered)}"

    def call(self, *args):
        self.calls.append(args)
        return self._result


class TestGetTempRoot(unittest.TestCase):

    def test_returns_the_default_root(self) -> None:
        # The root window of the test session is the first `Tk` that is created,
        # so `tkinter` itself uses it as the default root
        tests.root()

        self.assertIs(dialogs._get_temp_root(), tkinter._default_root)
        self.assertIsInstance(dialogs._get_temp_root(), tkinter.Tk)


class TestTkMessage(unittest.TestCase):

    def test_default_arguments(self) -> None:
        master = _FakeMaster(title="Parent")

        dialogs.TkMessage(master=master)

        # Without a title, the title of the parent window is used
        self.assertEqual(master.calls, [(
            "tk_messageBox", "-parent", master,
            "-icon", "info", "-title", "Parent", "-type", "ok",
        )])

    def test_all_the_arguments(self) -> None:
        master = _FakeMaster()
        results = []

        dialogs.TkMessage(
            "hello", "the detail", title="Title", icon="warning", option="yesno",
            default="yes", master=master, command=results.append)

        self.assertEqual(master.calls, [(
            "tk_messageBox", "-parent", master,
            "-icon", "warning", "-title", "Title",
            "-message", "hello", "-detail", "the detail",
            "-type", "yesno", "-default", "yes",
        )])
        # The result of the dialog is given to the callback
        self.assertEqual(results, ["ok"])

    def test_without_an_option(self) -> None:
        master = _FakeMaster()

        dialogs.TkMessage(option=None, master=master)

        self.assertNotIn("-type", master.calls[0])

    def test_without_a_command(self) -> None:
        master = _FakeMaster()

        dialogs.TkMessage("hello", master=master)

        self.assertIn("-message", master.calls[0])


class TestTkColorChooser(unittest.TestCase):

    def test_the_arguments_of_the_chooser(self) -> None:
        results = []
        with unittest.mock.patch.object(
            tkinter.colorchooser, "askcolor",
            return_value=((255, 0, 0), "#ff0000"),
        ) as askcolor:
            dialogs.TkColorChooser(
                title="Title", color="#123456", command=results.append)

        askcolor.assert_called_once_with(
            initialcolor="#123456", parent=None, title="Title")
        self.assertEqual(results, ["#ff0000"])

    def test_cancelling_does_not_call_the_command(self) -> None:
        results = []
        with unittest.mock.patch.object(
            tkinter.colorchooser, "askcolor", return_value=(None, None),
        ):
            dialogs.TkColorChooser(command=results.append)

        self.assertEqual(results, [])


class TestTkFontChooser(unittest.TestCase):

    def test_all_the_arguments(self) -> None:
        master = _FakeMaster()

        def command() -> None:
            pass

        dialogs.TkFontChooser(
            title="Title", font="TkDefaultFont", master=master, command=command)

        self.assertEqual(master.calls, [
            ("tk", "fontchooser", "configure", "-parent", master,
             "-title", "Title", "-font", "TkDefaultFont",
             "-command", "registered1"),
            ("tk", "fontchooser", "show"),
        ])
        self.assertEqual(master.registered, [command])

    def test_default_arguments(self) -> None:
        master = _FakeMaster()

        dialogs.TkFontChooser(master=master)

        self.assertEqual(master.calls, [
            ("tk", "fontchooser", "configure", "-parent", master),
            ("tk", "fontchooser", "show"),
        ])
        self.assertEqual(master.registered, [])


class TkFileChooserTestCase(unittest.TestCase):
    """Base case of the tests of the (private) file chooser."""

    def choose(self, method: str, is_dir: bool, mode: str, result, **kwargs):
        """Run `_TkFileChooser` with the given `tkinter.filedialog` function mocked."""
        kwargs.setdefault("master", _FakeMaster())
        results: list = []
        kwargs["command"] = results.append

        with unittest.mock.patch.object(
                tkinter.filedialog, method, return_value=result) as mocked:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")  # the class warns that it is unfinished
                dialogs._TkFileChooser(is_dir, mode, **kwargs)

        return mocked, results


class TestTkFileChooser(TkFileChooserTestCase):

    def test_it_warns_that_it_is_unfinished(self) -> None:
        master = _FakeMaster()
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            with unittest.mock.patch.object(
                    tkinter.filedialog, "askopenfilename", return_value=""):
                dialogs._TkFileChooser(False, "open", master=master)

        self.assertEqual(len(caught), 1)
        self.assertIs(caught[0].category, FutureWarning)

    def test_open_a_file(self) -> None:
        master = _FakeMaster()

        mocked, results = self.choose(
            "askopenfilename", False, "open", "/tmp/a.txt",
            title="T", initialdir="/tmp", initialfile="a.txt",
            filetypes=[("Text", "*.txt")], defaultextension=".txt", master=master)

        mocked.assert_called_once_with(
            initialfile="a.txt", filetypes=[("Text", "*.txt")],
            defaultextension=".txt", title="T", initialdir="/tmp", parent=master)
        self.assertEqual(results, ["/tmp/a.txt"])

    def test_open_a_file_without_choosing_anything(self) -> None:
        mocked, results = self.choose("askopenfilename", False, "open", "")

        self.assertEqual(mocked.call_args.kwargs["filetypes"], [])
        # The user cancelled the dialog, so there is nothing to report
        self.assertEqual(results, [])

    def test_open_multiple_files(self) -> None:
        mocked, results = self.choose(
            "askopenfilenames", False, "open", ("/tmp/a.txt", "/tmp/b.txt"),
            multiple=True)

        self.assertTrue(mocked.called)
        self.assertEqual(results, [("/tmp/a.txt", "/tmp/b.txt")])

    def test_save_a_file(self) -> None:
        mocked, results = self.choose(
            "asksaveasfilename", False, "save", "/tmp/a.txt", initialfile="a.txt")

        self.assertEqual(mocked.call_args.kwargs["initialfile"], "a.txt")
        self.assertEqual(results, ["/tmp/a.txt"])

    def test_select_a_directory(self) -> None:
        master = _FakeMaster()

        # `is_dir` overrides the mode, and the directory chooser takes less arguments
        mocked, results = self.choose(
            "askdirectory", True, "open", "/tmp", title="T", initialdir="/tmp",
            initialfile="a.txt", filetypes=[("Text", "*.txt")], master=master)

        mocked.assert_called_once_with(title="T", initialdir="/tmp", parent=master)
        self.assertEqual(results, ["/tmp"])

    def test_an_unknown_mode_does_nothing(self) -> None:
        results: list = []
        master = _FakeMaster()

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            with unittest.mock.patch.object(tkinter.filedialog, "askopenfilename") as open_1:
                with unittest.mock.patch.object(tkinter.filedialog, "askopenfilenames") as open_n:
                    with unittest.mock.patch.object(tkinter.filedialog, "asksaveasfilename") as save:
                        with unittest.mock.patch.object(tkinter.filedialog, "askdirectory") as directory:
                            dialogs._TkFileChooser(
                                False, "unknown", master=master, command=results.append)

        self.assertFalse(open_1.called)
        self.assertFalse(open_n.called)
        self.assertFalse(save.called)
        self.assertFalse(directory.called)
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().discover(os.path.dirname(__file__)))
