# Copyright (c) 2023-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""All standard dialog classes."""

from __future__ import annotations as _

__all__ = (
    "TkMessage",
    "TkColorChooser",
    "TkFontChooser",
    # "TkFileChooser",
)

import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import warnings
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from typing import Any, Literal


def _get_temp_root() -> tkinter.Tk:
    """Get temporary root."""
    if default_root := tkinter._default_root:
        return default_root
    return tkinter._get_temp_root()


class TkMessage:
    """Message pop-up."""

    def __init__(
        self,
        message: str | None = None,
        detail: str | None = None,
        *,
        title: str | None = None,
        icon: Literal["error", "info", "question", "warning"] = "info",
        option: Literal["abortretryignore", "ok", "okcancel", "retrycancel", "yesno", "yesnocancel"] = "ok",
        default: Literal["abort", "retry", "ignore", "ok", "cancel", "yes", "no"] | None = None,
        master: tkinter.Tk | None = None,
        command: Callable[[Literal["abort", "retry", "ignore", "ok", "cancel", "yes", "no"]], Any] | None = None,
    ) -> None:
        """
        Args:
            message: message.
            detail: detail message.
            title: title of the window.
            icon: icon.
            option: type of the message pop-up.
            default: button where the focus is, default is the leftmost one.
            master: parent widget.
            command: callback function.
        """
        if master is None:
            master = _get_temp_root()

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
    """Color chooser pop-up."""

    def __init__(
        self,
        *,
        title: str | None = None,
        color: str | None = None,
        master: tkinter.Tk | None = None,
        command: Callable[[str], Any] | None = None,
    ) -> None:
        """
        Args:
            title: title of the window.
            color: default color.
            master: parent widget of the window.
            command: callback function.
        """
        colors = tkinter.colorchooser.askcolor(
            initialcolor=color, parent=master, title=title)

        if command is not None and colors[0] is not None:
            command(colors[1])


class TkFontChooser:
    """Font chooser pop-up."""

    def __init__(
        self,
        *,
        title: str | None = None,
        font: str | None = None,
        master: tkinter.Tk | None = None,
        command: Callable[[str], Any] | None = None,
    ) -> None:
        """
        Args:
            title: title of the window.
            font: default font.
            master: parent widget of the window.
            command: callback function.
        """
        if master is None:
            master = _get_temp_root()

        args = []
        if title is not None:
            args += ["-title", title]
        if font is not None:
            args += ["-font", font]
        if command is not None:
            args += ["-command", master.register(command)]

        master.call("tk", "fontchooser", "configure", "-parent", master, *args)
        master.call("tk", "fontchooser", "show")


# XXX: The code below is bad and needs to be improved in the future
# Consider converting individual modes into methods


class _TkFileChooser:
    """File chooser pop-up."""

    def __init__(
        self,
        is_dir: bool,
        mode: Literal["save", "open"],
        *,
        title: str | None = None,
        initialdir: str | None = None,
        initialfile: str | None = None,
        filetypes: Sequence[tuple[str, str]] | None = None,
        defaultextension: str | None = None,
        multiple: bool = False,
        master: tkinter.Tk | None = None,
        command: Callable[[str | tuple[str, ...]], Any] | None = None,
    ) -> None:
        """
        Args:
            is_dir: whether to select a directory.
            mode: whether to save or open a file.
            title: title of the window.
            initialdir: initial directory.
            initialfile: initial file.
            filetypes: file types to filter.
                (e.g., ``[("Text Files", "*.txt"), ("All Files", "*.*")]``)
            defaultextension: default file extension.
            multiple: whether to allow multiple file selection.
            master: parent widget of the window.
            command: callback function.
        """
        warnings.warn(
            "This class is not fully implemented yet.", FutureWarning, 2)

        if master is None:
            master = tkinter._get_temp_root()

        if filetypes is None:
            filetypes = []

        if is_dir:
            mode = "dir"

        common_args = {
            "title": title,
            "initialdir": initialdir,
            "parent": master,
        }
        common_args2 = {
            "initialfile": initialfile,
            "filetypes": filetypes,
            "defaultextension": defaultextension,
        }

        match mode:
            case "open":
                if multiple:
                    file_paths = tkinter.filedialog.askopenfilenames(
                        **common_args2,
                        **common_args,
                    )
                else:
                    file_path = tkinter.filedialog.askopenfilename(
                        **common_args2,
                        **common_args,
                    )
                    file_paths = file_path if file_path else None
            case "save":
                file_paths = tkinter.filedialog.asksaveasfilename(
                    **common_args2,
                    **common_args,
                )
            case "dir":
                file_paths = tkinter.filedialog.askdirectory(
                    **common_args,
                )
            case _:
                file_paths = None

        if command is not None and file_paths:
            command(file_paths)
