# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""All global configuration options.

Some options are read-only, but most of them can be changed, and once changed,
they will take effect globally for the program. Some changes take effect
immediately, but some need to take effect when the relevant option is invoked.
"""

from __future__ import annotations as _

__all__ = (
    "Env",
    "Font",
    "Constant",
    "reset",
)

import ctypes
import math
import platform
import sys
import tkinter
from typing import Any, Final, Literal


class _DefaultRootDescriptor:
    """A simple descriptor for ``tkinter._default_root``."""

    def __get__(self, *args: Any, **kwargs: Any) -> tkinter.Tk:
        """Returns the current default root.

        In some cases, the method also returns ``tkinter.Tk`` and ``None``, but
        this can happen if the usage is not recommended.
        """
        del args, kwargs
        return tkinter._get_default_root()


class Env:
    """Configurations for default environment values.

    Attributes:
        system (str): The system of environment, such as ``"Windows10"``,
            ``"Windows11"``, ``"Linux"``, ``"Darwin"`` (macOS).
        theme (Literal["light", "dark"]): The theme of the application.
        gradient_animation (bool): Whether to enable gradient animation for
            widgets that support it by default.
        auto_update (bool): Whether to check for updates automatically on
            startup.
        root (tkinter.Tk): The current default root window. It is READ-ONLY.
    """

    # Global configurations
    system: str
    theme: Literal["light", "dark"]

    # Default parameters for widgets
    gradient_animation: bool
    auto_update: bool

    # Dynamic value
    root = _DefaultRootDescriptor()

    @classmethod
    def reset(cls) -> None:
        """Reset all configuration options."""
        cls.system = cls.get_default_system()
        cls.theme = "light"
        cls.gradient_animation = True
        cls.auto_update = True

    @staticmethod
    def get_default_system() -> str:
        """Get the system of environment."""
        if sys.platform == "win32":
            if sys.version_info.minor >= 12:
                return f"Windows{platform.win32_ver()[0]}"
            # If Python version < 3.12, the value above gets an error result
            if int(platform.win32_ver()[1].rsplit(".", maxsplit=1)[1]) >= 22000:
                return "Windows11"
            return "Windows10"
        return platform.system()


class Font:
    """Configurations for default font.

    Attributes:
        family (str): The default font family.
        size (int): The default font size, negative value means size in pixels.
    """

    family: str
    size: int

    @classmethod
    def reset(cls) -> None:
        """Reset all configuration options."""
        cls.family = cls.get_default_family()
        cls.size = -20

    @staticmethod
    def get_default_family() -> str:
        """Get the default font family."""
        if sys.platform == "win32":
            return "Microsoft YaHei"
        if sys.platform == "darwin":
            return "SF Pro"
        return "Noto Sans"


class Constant:
    """All Constants."""

    GOLDEN_RATIO: Final[float] = (math.sqrt(5)-1) / 2
    """The golden ratio, which is needed to automatically calculate the color
    of widget on ``"disabled"`` state. It is READ-ONLY."""

    PREDEFINED_EVENTS: Final[tuple[str, ...]] = (
        "<KeyPress>",
        "<KeyRelease>",
        "<Button-1>",
        "<Button-2>",
        "<Button-3>",
        "<Button-4>",
        "<Button-5>",
        "<ButtonRelease-1>",
        "<ButtonRelease-2>",
        "<ButtonRelease-3>",
        "<MouseWheel>",
        "<Motion>",
        "<B1-Motion>",
        "<B2-Motion>",
        "<B3-Motion>",
        "<Configure>",
    )
    """Predefined events that can be used directly without registration. It is
    READ-ONLY."""

    PREDEFINED_VIRTUAL_EVENTS: Final[tuple[str, ...]] = (
        "<<Copy>>",
        "<<Paste>>",
        "<<Cut>>",
        "<<SelectAll>>",
        "<<Redo>>",
        "<<Undo>>",
    )
    """Predefined virtual events that can be used directly without
    registration. It is READ-ONLY."""


def reset() -> None:
    """Reset all configuration options."""
    Env.reset()
    Font.reset()


reset()

if Env.system.startswith("Windows"):
    ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Set Windows DPI awareness
