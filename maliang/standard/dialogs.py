"""All standard dialog classes"""

from __future__ import annotations

__all__ = [
    "TkMessage",
    "TkColorChooser",
    "TkFontChooser",
    "TkFileChooser",
]

import collections.abc
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import typing


class TkMessage:
    """Message pop-up"""

    def __init__(
        self,
        message: str | None = None,
        detail: str | None = None,
        *,
        title: str | None = None,
        icon: typing.Literal["error", "info", "question", "warning"] = "info",
        option: typing.Literal["abortretryignore", "ok", "okcancel", "retrycancel", "yesno", "yesnocancel"] = "ok",
        default: typing.Literal["abort", "retry", "ignore", "ok", "cancel", "yes", "no"] | None = None,
        master: tkinter.Tk | None = None,
        command: collections.abc.Callable[[typing.Literal["abort", "retry", "ignore", "ok", "cancel", "yes", "no"]], typing.Any] | None = None,
    ) -> None:
        """
        * `message`: message
        * `detail`: detail message
        * `title`: title of the window
        * `icon`: icon
        * `option`: type of the message pop-up
        * `default`: button where the focus is, default is the leftmost one
        * `master`: parent widget of the window
        * `command`: callback function
        """
        if master is None:
            master = tkinter._get_temp_root()

        args = ["-icon", icon]

        if title is not None:
            args += ["-title", title]
        elif master is not None:
            args += ["-title", master.title()]

        if message is not None:
            args += ["-message", message]
        if detail is not None:
            args += ["-detail", detail]
        if option is not None:
            args += ["-type", option]
        if default is not None:
            args += ["-default", default]

        value = master.call("tk_messageBox", "-parent", master, *args)

        if command is not None:
            command(value)


class TkColorChooser:
    """Color chooser pop-up"""

    def __init__(
        self,
        *,
        title: str | None = None,
        color: str | None = None,
        master: tkinter.Tk | None = None,
        command: collections.abc.Callable[[str], typing.Any] | None = None,
    ) -> None:
        """
        * `title`: title of the window
        * `color`: default color
        * `master`: parent widget of the window
        * `command`: callback function
        """
        colors = tkinter.colorchooser.askcolor(
            initialcolor=color, parent=master, title=title)

        if command is not None and colors[0] is not None:
            command(colors[1])


class TkFontChooser:
    """Font chooser pop-up"""

    def __init__(
        self,
        *,
        title: str | None = None,
        font: str | None = None,
        master: tkinter.Tk | None = None,
        command: collections.abc.Callable[[str], typing.Any] | None = None,
    ) -> None:
        """
        * `title`: title of the window
        * `font`: default font
        * `master`: parent widget of the window
        * `command`: callback function
        """
        if master is None:
            master = tkinter._get_temp_root()

        args = []
        if title is not None:
            args += ["-title", title]
        if font is not None:
            args += ["-font", font]
        if command is not None:
            args += ["-command", master.register(command)]

        master.call("tk", "fontchooser", "configure", "-parent", master, *args)
        master.call("tk", "fontchooser", "show")


class TkFileChooser:
    """File chooser pop-up"""

    def __init__(
        self,
        *,
        title: str | None = None,
        initialdir: str | None = None,
        initialfile: str | None = None,
        filetypes: collections.abc.Sequence[tuple[str, str]] | None = None,
        defaultextension: str | None = None,
        multiple: bool = False,
        mode: typing.Literal["open", "save", "dir"] = "open",
        master: tkinter.Tk | None = None,
        command: collections.abc.Callable[[str | tuple[str, ...]], typing.Any] | None = None,
    ) -> None:
        """
        * `title`: title of the window
        * `initialdir`: initial directory
        * `initialfile`: initial file
        * `filetypes`: file types to filter (e.g., [("Text Files", "*.txt"), ("All Files", "*.*")])
        * `defaultextension`: default file extension
        * `multiple`: whether to allow multiple file selection
        * `mode`: mode of the file chooser ("open", "save", or "dir")
        * `master`: parent widget of the window
        * `command`: callback function
        """
        if master is None:
            master = tkinter._get_temp_root()

        match mode:
            case "open":
                if multiple:
                    file_paths = tkinter.filedialog.askopenfilenames(
                        title=title,
                        initialdir=initialdir,
                        initialfile=initialfile,
                        filetypes=filetypes,
                        defaultextension=defaultextension,
                        parent=master,
                    )
                else:
                    file_path = tkinter.filedialog.askopenfilename(
                        title=title,
                        initialdir=initialdir,
                        initialfile=initialfile,
                        filetypes=filetypes,
                        defaultextension=defaultextension,
                        parent=master,
                    )
                    file_paths = file_path if file_path else None
            case "save":
                file_paths = tkinter.filedialog.asksaveasfilename(
                    title=title,
                    initialdir=initialdir,
                    initialfile=initialfile,
                    filetypes=filetypes,
                    defaultextension=defaultextension,
                    parent=master,
                )
            case "dir":
                file_paths = tkinter.filedialog.askdirectory(
                    title=title,
                    initialdir=initialdir,
                    parent=master,
                )
            case _:
                file_paths = None

        if command is not None and file_paths:
            command(file_paths)
