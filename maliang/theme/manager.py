# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""Support for theme.

* ``darkdetect``: https://pypi.org/project/darkdetect/
* ``pywinstyles``: https://pypi.org/project/pywinstyles/
* ``win32material``: https://pypi.org/project/win32material/
* ``hPyT``: https://pypi.org/project/hPyT/
"""

from __future__ import annotations as _

__all__ = (
    "set_color_mode",
    "get_color_mode",
    "register_event",
    "remove_event",
    "apply_file_dnd",
    "apply_theme",
    "customize_window",
)

import ctypes.wintypes
import platform
import sys
import threading
import traceback
import warnings
from typing import TYPE_CHECKING

from ..core import configs
from ..toolbox import utility

try:
    import pywinstyles
except ImportError:
    pywinstyles = None

try:
    import hPyT
except ImportError:
    hPyT = None

try:
    import win32material
except ImportError:
    win32material = None

try:
    if sys.platform == "win32":
        major, _, micro = platform.version().split(".")
        # NOTE: On some Windows platforms, it is not possible to import
        # package `darkdetect` through the regular method
        if int(major) >= 10 and int(micro) >= 14393:
            import darkdetect._windows_detect as darkdetect
        else:
            import darkdetect
    else:
        import darkdetect
except ImportError:
    darkdetect = None

if TYPE_CHECKING:
    import tkinter
    from collections.abc import Callable
    from typing import Any, Literal

_callback_events: dict[Callable[..., Any], tuple] = {}
"""Events that are responded to when the system theme changes."""

_color_mode: Literal["light", "dark", "system"] = "system"
"""The color mode of the current program, ``"system"`` is the following system,
``"light"`` is the light color, and ``"dark"`` is the dark color."""


def set_color_mode(mode: Literal["system", "dark", "light"] = "system") -> None:
    """Set the color mode of the program.

    Args:
        mode: it can be ``"light"``, ``"dark"``, and ``"system"``.

    Tip:
        ``"system"`` is the following system.
    """
    global _color_mode  # pylint: disable=W0603
    _color_mode = mode
    _process_event(configs.Env.theme if mode == "system" else mode)


def get_color_mode() -> Literal["dark", "light"]:
    """Get the color mode of the program."""
    if _color_mode == "system":
        return configs.Env.theme

    return _color_mode


def register_event(func: Callable[..., Any], *args: Any) -> None:
    """Register a function to be called when the system accent color changes.

    When the system accent color changes, the registered function will be
    called, and the parameter is a boolean value indicating whether it is
    currently a dark theme.

    Args:
        func: callback function.
        args: extra arguments.
    """
    _callback_events[func] = args


def remove_event(func: Callable[..., Any]) -> None:
    """Remove a registered function.

    Args:
        func: callback function.
    """
    if _callback_events.get(func) is not None:
        del _callback_events[func]


def apply_file_dnd(
    window: tkinter.Tk,
    *,
    command: Callable[[str], Any],
) -> None:
    """Apply file drag and drop in a widget.

    Args:
        window: the window which being customized.
        command: callback function, accept a parameter that represents the path
            of the file.

    Warning:
        This function is only works on Windows OS!
    """
    if pywinstyles is None:
        warnings.warn("Package 'pywinstyles' is missing.", UserWarning, 2)
        return

    pywinstyles.apply_dnd(utility.get_parent(window), command)


def apply_theme(
    window: tkinter.Tk,
    *,
    theme: Literal["mica", "acrylic", "acrylic2", "aero", "transparent", "optimised", "win7", "inverse", "native", "popup", "dark", "normal"],
) -> None:
    """Apply some Windows themes to the window.

    Args:
        window: the window which being customized.
        theme: different themes for windows.

    Warning:
        This function is only works on Windows OS! And some parameters are
        useless on Windows 7/10!
    """
    if theme in ("mica", "acrylic2"):
        if win32material is None:
            warnings.warn(
                "Package 'win32material' is missing.", UserWarning, 2)
            return

        if theme == "mica":  # NOTE: "mica" of package `pywinstyles` do not work
            win32material.ApplyMica(
                ctypes.wintypes.HWND(utility.get_parent(window)))
        elif theme == "acrylic2":  # Only for titlebar
            win32material.ApplyAcrylic(
                ctypes.wintypes.HWND(utility.get_parent(window)))

        return

    if pywinstyles is None:
        warnings.warn("Package 'pywinstyles' is missing.", UserWarning, 2)
        return

    pywinstyles.apply_style(window, theme)

    # NOTE: This is a flaw in `pywinstyles`, which is fixed here
    if platform.win32_ver()[0] == "10":
        window.withdraw()
        window.deiconify()
        window.update()


def customize_window(
    window: tkinter.Tk,
    *,
    border_color: str | None = None,
    header_color: str | None = None,
    title_color: str | None = None,
    hide_title_bar: bool | None = None,
    hide_button: Literal["all", "maxmin", "none"] | None = None,
    disable_minimize_button: bool | None = None,
    disable_maximize_button: bool | None = None,
    border_type: Literal["rectangular", "smallround", "round"] | None = None,
) -> None:
    """Customize the relevant properties of the window

    Args:
        window: the window which being customized.
        border_color: border color of the window.
        header_color: header color of the window.
        title_color: title color of the window.
        hide_title_bar: whether hide the whole title bar.
        hide_button: whether hide part of buttons on title bar.
        disable_minimize_button: whether disable minimize button.
        disable_maximize_button: whether disable maximize button.
        border_type: border type of the window.

    Warning:
        This function is only works on Windows OS! And some parameters are
        useless on Windows 7/10!
    """
    if pywinstyles is not None:
        if border_color is not None:
            pywinstyles.change_border_color(window, border_color)
        if header_color is not None:
            pywinstyles.change_header_color(window, header_color)
        if title_color is not None:
            pywinstyles.change_title_color(window, title_color)
    elif any((border_color, header_color, title_color)):
        warnings.warn("Package 'pywinstyles' is missing.", UserWarning, 2)

    if hPyT is not None:
        if hide_title_bar is not None:
            if hide_title_bar:
                hPyT.title_bar.hide(window, no_span=True)
            else:
                hPyT.title_bar.unhide(window)
        if hide_button is not None:
            if hide_button == "maxmin":
                hPyT.maximize_minimize_button.hide(window)
            elif hide_button == "all":
                hPyT.all_stuffs.hide(window)
            else:
                hPyT.maximize_minimize_button.unhide(window)
                hPyT.all_stuffs.unhide(window)
        if disable_maximize_button is not None:
            if disable_maximize_button:
                hPyT.maximize_button.disable(window)
            else:
                hPyT.maximize_button.enable(window)
        if disable_minimize_button is not None:
            if disable_minimize_button:
                hPyT.minimize_button.disable(window)
            else:
                hPyT.minimize_button.enable(window)
    elif any(map(lambda x: x is not None, (
            hide_title_bar, hide_button,
            disable_maximize_button, disable_minimize_button))):
        warnings.warn("Package 'hPyT' is missing.", UserWarning, 2)

    if win32material is not None:
        if border_type is not None:
            match border_type:
                case "rectangular": type_ = win32material.BORDERTYPE.RECTANGULAR
                case "smallround": type_ = win32material.BORDERTYPE.SMALLROUND
                case "round": type_ = win32material.BORDERTYPE.ROUND
            win32material.SetWindowBorder(
                ctypes.wintypes.HWND(utility.get_parent(window)), type_)
    elif any((border_type, )):
        warnings.warn("Package 'win32material' is missing.", UserWarning, 2)


def _process_event(theme: Literal["light", "dark"]) -> None:
    """Handle registered callback functions.

    Args:
        theme: theme name
    """
    for func, args in _callback_events.items():
        try:  # Prevent detection thread from crashing
            func(theme, *args)
        except Exception as exc:  # pylint: disable=W0718
            traceback.print_exception(exc)


def _callback(theme: str) -> None:
    """Callback function that is triggered when a system theme is switched.
    Valid only if the theme mode is set to follow system.

    Args:
        theme: theme name.
    """
    configs.Env.theme = "dark" if theme == "Dark" else "light"

    if _color_mode == "system":
        _process_event(configs.Env.theme)


if darkdetect is not None:
    configs.Env.theme = "dark" if darkdetect.isDark() else "light"
    threading.Thread(
        target=darkdetect.listener, args=(_callback,), daemon=True).start()
