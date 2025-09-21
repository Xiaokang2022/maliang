# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""All standard ``Widget`` classes."""

from __future__ import annotations as _

__all__ = (
    "Text",
    "Image",
    "Label",
    "Button",
    "Switch",
    "InputBox",
    "ToggleButton",
    "CheckBox",
    "RadioBox",
    "ProgressBar",
    "UnderlineButton",
    "HighlightButton",
    "IconButton",
    "Slider",
    "SegmentedButton",
    "SpinBox",
    "OptionButton",
    "ComboBox",
    "Spinner",
    "Tooltip",
)

import contextlib
import decimal
import itertools
import math
import warnings
from typing import TYPE_CHECKING

from typing_extensions import override

from ..animation import animations, controllers
from ..core import configs, virtual
from ..toolbox import utility
from . import features, images, shapes, styles, texts

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any, Literal

    from ..core import containers
    from ..toolbox import enhanced


class Text(virtual.Widget):
    """Text widget, generally used to display plain text."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        text: str = "",
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        wrap_length: int | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            wrap_length: limit the length of text, beyond which it will
                automatically wrap.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if auto_resize := size is None:
            size = utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant,
                wrap_length=wrap_length, master=master)
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_resize=auto_resize, auto_update=auto_update, style=style)
        # The above parameter `anchor` has no practical effect and is only used
        # to query the data of the widget.
        if style is None:
            self.style = styles.TextStyle(self)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight,
            slant=slant, underline=underline, overstrike=overstrike,
            justify=justify, width=wrap_length)
        self.feature = features.TextFeature(self)

    def get(self) -> str:
        """Get the text of the widget."""
        return self.texts[0].get()

    def set(self, text: str) -> None:
        """Set the text of the widget."""
        self.texts[0].set(text)
        if self.auto_resize:
            self.resize(utility.get_text_size(
                text, font=self.texts[0].font, master=self.master))


class Image(virtual.Widget):
    """Image widget, generally used to display normal still image."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None and image is not None:
            size = image.width(), image.height()
        super().__init__(
            master, position, size if size else (0, 0), anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        # The above parameter `anchor` has no practical effect and is only used
        # to query the data of the widget.
        if image is not None and size is not None:
            images.StillImage(self, image=image.scale(
                size[0]/image.width(), size[1]/image.height()))
        else:
            images.StillImage(self, image=image)
        self.feature = features.ImageFeature(self)

    def get(self) -> enhanced.PhotoImage:
        """Get the image of the widget."""
        if (image := self.images[0].image) is not None:
            return image
        return self.images[0].initial_image

    def set(self, image: enhanced.PhotoImage | None) -> None:
        """Set the image of the widget."""
        self.images[0].initial_image = image
        if image is not None:
            self.master.update()
            image = image.scale(*self.master.ratios)
        self.images[0].image = image
        self.master.itemconfigure(self.images[0].items[0], image=image)


class Label(virtual.Widget):
    """Label widget, which is generally used to display key information."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        text: str = "",
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if auto_resize := size is None:
            size = utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, padding=6, master=master)
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_resize=auto_resize, auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.LabelStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        self.feature = features.LabelFeature(self)

    def get(self) -> str:
        """Get the text of the widget."""
        return self.texts[0].get()

    def set(self, text: str) -> None:
        """Set the text of the widget."""
        self.texts[0].set(text)
        if self.auto_resize:
            self.resize(utility.get_text_size(
                text, font=self.texts[0].font, padding=6, master=self.master))


class Button(virtual.Widget):
    """Button widget, typically used to trigger a function."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        text: str = "",
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        command: Callable | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            command: a function that is triggered when the button is pressed.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if auto_resize := size is None:
            size = utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, padding=6, master=master)
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_resize=auto_resize, auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.ButtonStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        self.feature = features.ButtonFeature(self, command=command)

    def get(self) -> str:
        """Get the text of the widget."""
        return self.texts[0].get()

    def set(self, text: str) -> None:
        """Set the text of the widget."""
        self.texts[0].set(text)
        if self.auto_resize:
            self.resize(utility.get_text_size(
                text, font=self.texts[0].font, padding=6, master=self.master))


class Switch(virtual.Widget):
    """Switch widget, typically used to control the turning of a function on
    and off."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        length: int = 60,
        *,
        default: bool | None = None,
        command: Callable[[bool], Any] | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            length: length of the widget.
            default: default value of the widget.
            command: a function that is triggered when the switch is changed.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        super().__init__(
            master, position, (length, length / 2),
            anchor=anchor, capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        self.state = "normal-off"
        if style is None:
            self.style = styles.SwitchStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self, name=".out")
            shapes.Rectangle(
                self, name=".in", position=(length/10, length/10),
                size=(length*3/10, length*3/10), gradient_animation=False)
        else:
            shapes.SemicircularRectangle(self)
            shapes.Oval(self, position=(length/10, length/10),
                        size=(length*3/10, length*3/10), gradient_animation=False)
        if image is not None:
            images.StillImage(self, image=image)
        self.feature = features.SwitchFeature(self, command=command)
        if default is not None:
            self.set(default)

    def get(self) -> bool:
        """Get the state of the switch."""
        return self.state.endswith("on")

    def set(self, value: bool, *, callback: bool = False) -> None:
        """Set the state of the switch."""
        if callback and self.feature.command is not None:
            self.feature.command(value)
        if self.get() == bool(value):
            return
        self.update(f"{self.state.split('-', maxsplit=1)[0]}-{'on' if value else 'off'}")
        dx = self.shapes[0].size[0]/2 if value else -self.shapes[0].size[0]/2
        animations.MoveElement(
            self.shapes[1], (dx, 0), 250, controller=controllers.smooth, fps=60).start()


class InputBox(virtual.Widget):
    """Input box widget, generally used to enter certain information on a single
    line."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        align: Literal["left", "right", "center"] = "left",
        placeholder: str = "",
        show: str | None = None,
        ignore: tuple[str, ...] = ("\n", "\r"),
        limit: int = -1,
        limit_width: int = 0,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            align: align mode of the text.
            show: display a value that obscures the original content.
            ignore: ignore the input of some characters.
            placeholder: a placeholder for the prompt.
            limit: limit on the number of characters.
            limit_width: limit on the width of characters.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None:
            size = 200, utility.get_text_size(
                "", fontsize, family, weight=weight, slant=slant, padding=6, master=master)[1]
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.InputBoxStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self, name=".out")
            shapes.RoundedRectangle(self, name=".in", size=(self.size[0], self.size[1]-3))
        if image is not None:
            images.StillImage(self, image=image)
        texts.SingleLineText(
            self, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, align=align,
            ignore=ignore, limit=limit, limit_width=limit_width, show=show,
            placeholder=placeholder)
        self.feature = features.InputBoxFeature(self)

    def get(self) -> str:
        """Get the value of the Entry."""
        return self.texts[0].get()

    def set(self, value: str) -> bool:
        """Set the text value of the Entry."""
        return self.texts[0].set(value)

    def insert(self, index: int, value: str) -> bool:
        """Insert."""
        return self.texts[0].insert(index, value)

    def append(self, value: str) -> bool:
        """Append text to Entry."""
        return self.texts[0].append(value)

    def remove(self, start: int, end: int | None = None) -> int:
        """Remove."""
        self.texts[0].remove(start, end)

    def pop(self, index: int = -1) -> str:
        """Delete a specified amount of text."""
        return self.texts[0].pop(index)

    def clear(self) -> None:
        """Clear the text value of the Entry."""
        self.texts[0].clear()

    @override
    def update(
        self,
        state: str | None = None,
        *,
        gradient_animation: bool | None = None,
        nested: bool = True,
    ) -> None:
        """Update the widget.

        Args:
            state: state of the widget.
            gradient_animation: whether use gradient animation.
            nested: whether nested.
        """
        super().update(
            state, gradient_animation=gradient_animation, nested=nested)

        if state == "disabled" and self.master.focus() == self.texts[0].items[0]:
            self.master.focus("")


class CheckBox(virtual.Widget):
    """Checkbox button widget, generally used to check some options."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        length: int = 30,
        *,
        default: bool | None = None,
        command: Callable[[bool], Any] | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            length: length of the widget.
            default: default state of the widget.
            command: a function that is triggered when the state of check button
                is on.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        super().__init__(
            master, position, (length, length), anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        self.state = "normal-off"
        if style is None:
            self.style = styles.CheckBoxStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(self, text="✔")
        self.feature = features.CheckBoxFeature(self, command=command)
        if default is not None:
            self.set(default)

    def get(self) -> bool:
        """Get the state of the check button."""
        return self.state.endswith("on")

    def set(self, value: bool, *, callback: bool = False) -> None:
        """Set the state of the check button."""
        if callback and self.feature.command is not None:
            self.feature.command(value)
        if self.get() == bool(value):
            return
        self.update(f"{self.state.split('-', maxsplit=1)[0]}-{'on' if value else 'off'}")


class ToggleButton(virtual.Widget):
    """A button that can display information and switch statuses."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        text: str = "",
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        default: bool | None = None,
        command: Callable[[bool], Any] | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            default: default state of the widget.
            command: a function that is triggered when the state of check button
                is on.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None:
            size = utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, padding=6, master=master)
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        self.state = "normal-off"
        if style is None:
            self.style = styles.ToggleButtonStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        self.feature = features.ToggleButtonFeature(self, command=command)
        if default is not None:
            self.set(default)

    def get(self) -> bool:
        """Get the state of the check button."""
        return self.state.endswith("on")

    def set(self, value: bool, *, callback: bool = False) -> None:
        """Set the state of the switch."""
        if callback and self.feature.command is not None:
            self.feature.command(value)
        if self.get() == bool(value):
            return
        self.update(f"{self.state.split('-', maxsplit=1)[0]}-{'on' if value else 'off'}")


class RadioBox(virtual.Widget):
    """Radio button widget, generally used to select one of several options."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        length: int = 30,
        *,
        default: bool | None = None,
        command: Callable[[int], Any] | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            length: length of the widget.
            default: default state of the widget.
            command: a function that is triggered when the state of radio button
                is on.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        self.groups: list[RadioBox] = [self]
        super().__init__(
            master, position, (length, length), anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.RadioBoxStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self, name=".out")
            shapes.Rectangle(
                self, name=".in",
                position=(self.size[0]/4, self.size[1]/4),
                size=(self.size[0]/2, self.size[1]/2)).forget()
        else:
            shapes.Oval(self, name=".out")
            shapes.Oval(
                self, name=".in",
                position=(self.size[0]/4, self.size[1]/4),
                size=(self.size[0]/2, self.size[1]/2)).forget()
        if image is not None:
            images.StillImage(self, image=image)
        self.feature = features.RadioBoxFeature(self, command=command)
        if default is not None:
            self.set(default)

    def get(self) -> bool:
        """Get the state of the radio button."""
        return self.shapes[1].visible

    def set(self, value: bool, *, callback: bool = False) -> None:
        """Set the state of the radio button."""
        if callback and self.feature.command is not None:
            self.feature.command(value)
        if self.get() == bool(value):
            return None
        if value:
            return self.shapes[1].forget(False)
        return self.shapes[1].forget()

    def group(self, *radio_boxes: RadioBox) -> None:
        """Combine other radio boxes.

        Args:
            radio_boxes: other radio boxes.
        """
        for radio_box in radio_boxes:
            if radio_box in self.groups:
                continue

            self.groups.append(radio_box)
            radio_box.groups = self.groups


class ProgressBar(virtual.Widget):
    """Progress bar widget, typically used to show the progress of an event."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] = (400, 20),
        *,
        default: float | None = None,
        command: Callable[[float], Any] | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            default: default value of the widget
            command: a function that is triggered when the progress of progress
                bar is 100%.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        self.value: float = 0
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.ProgressBarStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self, name=".out")
            shapes.Rectangle(
                self, name=".in", size=(0, self.size[1]*0.8),
                position=(self.size[1]*0.1, self.size[1]*0.1))
        else:
            shapes.SemicircularRectangle(self, name=".out")
            shapes.SemicircularRectangle(
                self, name=".in", size=(self.size[1]*0.7, self.size[1]*0.7),
                position=(self.size[1]*0.15, self.size[1]*0.15))
        if image is not None:
            images.StillImage(self, image=image)
        self.feature = features.ProgressBarFeature(self)
        self.shapes[1].forget()
        self.command = command
        if default is not None:
            self.set(default)

    def get(self) -> float:
        """Get the progress of the progress bar."""
        return self.value

    def set(self, value: float, *, callback: bool = False) -> None:
        """Set the progress of the progress bar."""
        self.value = 0 if value < 0 else 1 if value > 1 else value
        if callback and self.command is not None:
            self.command(value)
        if self.value == 0:
            return self.shapes[1].forget()
        if not self.shapes[1].visible:
            self.shapes[1].forget(False)

        if isinstance(self.shapes[1], shapes.Rectangle):
            self.shapes[1].coords(
                ((self.size[0]-self.size[1]*0.2) * self.value, self.shapes[1].size[1]))
        else:
            self.shapes[1].coords(
                (self.size[1]*0.7 + (self.size[0]-self.size[1] * 0.3-self.shapes[1].size[1])
                 * self.value, self.shapes[1].size[1]))

        return None


class UnderlineButton(virtual.Widget):
    """Underline button, generally used to display web links."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        *,
        text: str = "",
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        command: Callable | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool = False,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            command: a function that is triggered when the underline button is
                pressed.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        super().__init__(
            master, position, utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, master=master),
            anchor=anchor, capture_events=capture_events,
            gradient_animation=gradient_animation, auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.UnderlineButtonStyle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        self.feature = features.Underline(self, command=command)


class HighlightButton(virtual.Widget):
    """Highlight button, no outline, which added a highlight effect."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        *,
        text: str = "",
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        command: Callable | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            command: a function that is triggered when the hightlight button is pressed.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        super().__init__(
            master, position, utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, master=master),
            anchor=anchor, capture_events=capture_events,
            gradient_animation=gradient_animation, auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.HighlightButtonStyle(self)
        if image is not None:
            images.StillImage(self, image=image)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        self.feature = features.Highlight(self, command=command)


class IconButton(virtual.Widget):
    """A button with an icon on the left side."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        text: str = "",
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        command: Callable | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            command: a function that is triggered when the button is pressed.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None:
            size = utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, padding=6, master=master)
            size = size[0] + size[1] - 6, size[1]
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.IconButtonStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        if image is not None:
            images.StillImage(self, ((size[1]-size[0]) / 2, 0), image=image)
        texts.Information(
            self, (size[1] - size[0]/2, 0), text=text, family=family, fontsize=fontsize,
            weight=weight, slant=slant, underline=underline, overstrike=overstrike,
            justify=justify, anchor="w")
        self.feature = features.ButtonFeature(self, command=command)

    def get(self) -> str:
        """Get the text of the widget."""
        return self.texts[0].get()

    def set(self, text: str) -> None:
        """Set the text of the widget."""
        return self.texts[0].set(text)


class Slider(virtual.Widget):
    """A slider for visually resizing values."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] = (400, 30),
        *,
        default: float | None = None,
        command: Callable[[float], Any] | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            default: default value of the widget.
            command: a function that is triggered when the button is pressed.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        self.value: float = 0
        self.command = command
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.SliderStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self, (0, size[1]*5/11), (size[0], size[1]/11), name=".out")
            shapes.Rectangle(self, (0, size[1]*5/11), (size[1]/5, size[1]/11), name=".in")
            shapes.Rectangle(self, size=(size[1]*2/5, size[1]))
        else:
            shapes.SemicircularRectangle(self, (0, size[1]*2/5), (size[0], size[1]/5), name=".out")
            shapes.SemicircularRectangle(self, (0, size[1]*2/5), (size[1]/2, size[1]/5), name=".in")
            shapes.Oval(self, size=(size[1], size[1]), name=".out")
            shapes.Oval(self, (size[1]/4, size[1]/4), (size[1]/2, size[1]/2), name=".in")
        self.feature = features.SliderFeature(self)
        if default is not None:
            self.set(default)

    def get(self) -> float:
        """Get the value of the slider."""
        return self.value

    def set(self, value: float, *, callback: bool = False) -> None:
        """Set the value of the slider."""
        value = 1 if value > 1 else 0 if value < 0 else value
        if callback and self.command is not None:
            self.command(value)
        if self.get() == value:
            return
        if isinstance(self.shapes[-1], shapes.Oval):
            delta = (value-self.value) * (self.size[0]-self.size[1])
        else:
            delta = (value-self.value) * (self.size[0]-self.size[1]*2/5)
        self.value = value
        for shape in self.shapes[2:]:
            shape.move(delta, 0)
        if isinstance(self.shapes[-1], shapes.Oval):
            self.shapes[1].coords(
                (self.size[1]/2 + (self.size[0]-self.size[1]) * self.value, self.shapes[1].size[1]))
        else:
            self.shapes[1].coords(
                (self.size[1]/5 + (self.size[0]-self.size[1]*2/5)
                 * self.value, self.shapes[1].size[1]))


class SegmentedButton(virtual.Widget):
    """A segmented button that can be used to toggle between multiple states."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        sizes: tuple[tuple[int, int], ...] = (),
        *,
        text: tuple[str, ...] = (),
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        default: int | None = None,
        command: Callable[[int | None], Any] | None = None,
        image: tuple[enhanced.PhotoImage | None, ...] = (),
        layout: Literal["horizontal", "vertical"] = "horizontal",
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            sizes: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            default: default value of the widget.
            command: a function that is triggered when the button is pressed.
            image: image of the widget.
            layout: layout mode of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        self.value: int | None = None
        if not sizes:
            if text:
                sizes = tuple(utility.get_text_size(
                    text, fontsize, family, weight=weight, slant=slant, padding=6, master=master
                ) for text in text)
            else:
                sizes = (utility.get_text_size(
                    "", fontsize, family, weight=weight, slant=slant, padding=6, master=master),)
        widths, heights, length = *zip(*sizes), len(sizes)
        if not text:
            sizes, length = (), 0
        if layout == "horizontal":
            total_size = sum(widths) + length*5 + 5, max(heights) + 10
        else:
            total_size = max(widths) + 10, sum(heights) + length*5 + 5
        super().__init__(
            master, position, total_size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.SegmentedButtonStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        total_side_length = 5
        for i, (size, text, image) in enumerate(itertools.zip_longest(sizes, text, image)):
            position = (total_side_length, 5) if layout == "horizontal" else (5, total_side_length)
            position = tuple(i - j for i, j in zip(position, self.offset))
            ToggleButton(
                self, position, size, text=text, family=family, fontsize=fontsize, weight=weight,
                slant=slant, underline=underline, overstrike=overstrike, justify=justify,
                gradient_animation=gradient_animation, image=image,
                command=lambda _, i=i: (self.set(i), command(i) if command else None),
                style=styles.ToggleButtonStyle4SB)
            total_side_length += size[layout == "vertical"] + 5
        self.command = command
        if default is not None:
            self.set(default)
        self.feature = features.SegmentedButtonFeature(self)

    def get(self) -> int | None:
        """Get the index of the child toggle button with a value of True. If
        not, None is returned."""
        return self.value

    def set(self, value: int | None, *, callback: bool = False) -> None:
        """Activate the child toggle button for the specified index."""
        if callback and self.command:
            self.command(value)
        for i, widget in enumerate(self.children):
            widget.set(i == value)
        self.value = value


class SpinBox(virtual.Widget):
    """A widget that makes it easy to enter numeric type data."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        format_spec: str = "d",
        step: float = 1,
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        align: Literal["left", "right", "center"] = "left",
        placeholder: str = "",
        show: str | None = None,
        limit: int = math.inf,
        default: str | None = None,
        command: Callable[[bool], Any] | None = None,
        image: enhanced.PhotoImage | None = None,
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            format_spec: format of value.
            step: value of each change.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            align: align mode of the text.
            show: display a value that obscures the original content.
            placeholder: a placeholder for the prompt.
            limit: limit on the number of characters.
            default: default value of the widget.
            command: a function that is triggered when the button is pressed.
            image: image of the widget.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None:
            size = 200, utility.get_text_size(
                "", fontsize, family, weight=weight, slant=slant, padding=6, master=master)[1]
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        h = size[1]/2 - 6
        w = h/configs.Constant.GOLDEN_RATIO if configs.Env.system == "Windows10" else 2*h
        limit_width = - w
        InputBox(
            self, (0, 0), size, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, align=align, placeholder=placeholder,
            show=show, limit=limit, image=image, gradient_animation=gradient_animation, limit_width=limit_width,
            anchor=anchor)
        Button(self, (size[0]-w-4-self.offset[0], 4-self.offset[1]), (w, h), text="▲", fontsize=14,
               command=lambda: command(True) if command is not None else self.change(True))
        Button(self, (size[0]-w-4-self.offset[0], size[1]/2+2-self.offset[1]), (w, h), text="▼",
               fontsize=14,
               command=lambda: command(False) if command is not None else self.change(False))
        self.format = format_spec
        self.step = decimal.Decimal(str(step))
        self.feature = features.SpinBoxFeature(self, command=command)
        if default is not None:
            self.set(default)

    def change(self, up: bool) -> None:
        """Try change the current value."""
        if value := self.children[0].get():
            with contextlib.suppress(decimal.DecimalException):
                value = decimal.Decimal(value) + (self.step if up else -self.step)
                self.children[0].set(("%"+self.format) % value)
        else:
            self.children[0].set(("%"+self.format) % 0)

    def get(self) -> str:
        """Get the value of the Entry."""
        return self.children[0].get()

    def set(self, value: str) -> None:
        """Set the text value of the Entry."""
        self.children[0].set(value)

    def append(self, value: str) -> None:
        """Append text to Entry."""
        self.children[0].append(value)

    def delete(self, count: int) -> None:
        """Delete a specified amount of text."""
        self.children[0].delete(count)

    def clear(self) -> None:
        """Clear the text value of the Entry."""
        self.children[0].clear()


class OptionButton(virtual.Widget):
    """A button that has many options to choose."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        text: tuple[str, ...] = (),
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        default: int | None = None,
        command: Callable[[int | None], Any] | None = None,
        image: tuple[enhanced.PhotoImage | None, ...] = (),
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        align: Literal["up", "center", "down"] = "center",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            default: default value of the widget.
            command: a function that is triggered when the button is pressed.
            image: image of the widget.
            anchor: anchor of the widget.
            align: align of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None:
            size = sorted(utility.get_text_size(t, fontsize, family, weight=weight,
                          slant=slant, padding=6, master=master) for t in (list(text) + [""]))[-1]
        self.text = text
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.OptionButtonStyle(self)
        self._button = Button(
            self, (0, 0), size, family=family, fontsize=fontsize, weight=weight,
            slant=slant, underline=underline, overstrike=overstrike, justify=justify, anchor=anchor,
            command=self._open_options)
        self._segmented_button = SegmentedButton(
            self, self._get_position(align), (size,)*len(text), text=text, family=family,
            fontsize=fontsize, weight=weight, slant=slant, underline=underline,
            overstrike=overstrike, justify=justify, image=image, layout="vertical",
            capture_events=capture_events, gradient_animation=False, command=self._close_options,
            anchor="s" if align == "up" else "n" if align == "down" else "center")
        self._segmented_button.capture_events = None
        self._segmented_button.forget(True)
        self._segmented_button.bind("<Button-1>", self._extra_bind, add="+")
        self.command = command
        if default is not None:
            self.set(default)

    def _get_position(self, align: Literal["up", "center", "down"]) -> tuple[int, int]:
        """Get the position of "pop-up" SegmentedButton."""
        x, y = self.size[0]/2 - self.offset[0], self.size[1]/2 - self.offset[1]
        match align:
            case "up": y += self.size[1]/2 + 6
            case "down": y -= self.size[1]/2 + 6
        return x, y

    def _extra_bind(self, event) -> None:
        if not self._segmented_button.detect(event.x, event.y):
            self._segmented_button.forget(True)

    def _open_options(self) -> None:
        """Open the options."""
        self.master.widgets.remove(self._segmented_button)
        self.master.widgets.append(self._segmented_button)
        for element in self._segmented_button.elements:
            for item in element.items:
                self.master.lift(item)
        for widget in self._segmented_button.children:
            self.master.widgets.remove(widget)
            self.master.widgets.append(widget)
            for element in widget.elements:
                for item in element.items:
                    self.master.lift(item)

        self._segmented_button.forget(False)

    def _close_options(self, index: int | None = None) -> None:
        """Close the options."""
        self._button.texts[0].set("" if index is None else self.text[index])
        self._segmented_button.forget(True)
        if self.command is not None:
            self.command(index)

    def get(self) -> int | None:
        """Get the index of the child toggle button with a value of True. If
        not, None is returned."""
        return self._segmented_button.value

    def set(self, value: int | None, *, callback: bool = False) -> None:
        """Activate the child toggle button for the specified index."""
        self._segmented_button.set(value, callback=True)
        if callback and self.command is not None:
            self.command(value)


class ComboBox(virtual.Widget):
    """An input box that can provide several options."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] | None = None,
        *,
        text: tuple[str, ...] = (),
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        default: int | None = None,
        command: Callable[[int | None], Any] | None = None,
        image: tuple[enhanced.PhotoImage | None, ...] = (),
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        align: Literal["up", "down"] = "down",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            text: text of the widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            default: default value of the widget.
            command: a function that is triggered when the button is pressed.
            image: image of the widget.
            anchor: anchor of the widget.
            align: align of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None:
            size = sorted(utility.get_text_size(t, fontsize, family, weight=weight,
                          slant=slant, padding=6, master=master) for t in (list(text) + [""]))[-1]
            size = size[0] + size[1] - 10, size[1]
        self.text = text
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        h = size[1] - 10
        self._input_box = InputBox(
            self, (0, 0), size, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, anchor=anchor, limit_width=-h)
        self._button = Button(
            self, (size[0]-h-5-self.offset[0], 5-self.offset[1]), (h, h), text="▼",
            command=lambda: self._open_options() if self._segmented_button.disappeared else self._segmented_button.forget())
        self._segmented_button = SegmentedButton(
            self, self._get_position(align), (size,)*len(text), text=text, family=family,
            fontsize=fontsize, weight=weight, slant=slant, underline=underline,
            overstrike=overstrike, justify=justify, image=image, layout="vertical",
            capture_events=capture_events, gradient_animation=False, command=self._close_options,
            anchor="s" if align == "up" else "n" if align == "down" else "center")
        self._segmented_button.capture_events = None
        self._segmented_button.forget(True)
        self._segmented_button.bind("<Button-1>", self._extra_bind, add="+")
        self.command = command
        if default is not None:
            self.set(default)

    def _get_position(self, align: Literal["up", "center", "down"]) -> tuple[int, int]:
        """Get the position of "pop-up" SegmentedButton."""
        x, y = self.size[0]/2 - self.offset[0], self.size[1]/2 - self.offset[1]
        match align:
            case "up": y -= self.size[1]/2
            case "down": y += self.size[1]/2
        return x, y

    def _extra_bind(self, event) -> None:
        if not self._segmented_button.detect(event.x, event.y):
            self._segmented_button.forget(True)

    def _open_options(self) -> None:
        """Open the options."""
        self.master.widgets.remove(self._segmented_button)
        self.master.widgets.append(self._segmented_button)
        for element in self._segmented_button.elements:
            for item in element.items:
                self.master.lift(item)
        for widget in self._segmented_button.children:
            self.master.widgets.remove(widget)
            self.master.widgets.append(widget)
            for element in widget.elements:
                for item in element.items:
                    self.master.lift(item)

        self._segmented_button.forget(False)

    def _close_options(self, index: int | None = None) -> None:
        """Close the options."""
        self._input_box.texts[0].set("" if index is None else self.text[index])
        self._segmented_button.forget(True)
        if self.command is not None:
            self.command(index)

    def get(self) -> int | None:
        """Get the index of the child toggle button with a value of True. If
        not, None is returned."""
        return self._segmented_button.value

    def set(self, value: int | None, *, callback: bool = False) -> None:
        """Activate the child toggle button for the specified index."""
        self._segmented_button.set(value, callback=True)
        if callback and self.command is not None:
            self.command(value)


class Spinner(virtual.Widget):
    """Spinners visually communicate that something is processing."""

    def __init__(
        self,
        master: containers.Canvas | virtual.Widget,
        position: tuple[int, int],
        size: tuple[int, int] = (30, 30),
        *,
        default: float | None = None,
        command: Callable[[float], Any] | None = None,
        widths: tuple[int, int] | None = None,
        mode: Literal["determinate", "indeterminate"] = "determinate",
        anchor: Literal["n", "e", "w", "s", "nw", "ne", "sw", "se", "center"] = "nw",
        capture_events: bool | None = None,
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            master: parent canvas.
            position: position of the widget.
            size: size of the widget.
            default: default value of the widget.
            command: a function that is triggered when the progress of progress
                bar is 100%.
            widths: width of the outside ring and inside ring.
            mode: mode of the Spinner.
            anchor: anchor of the widget.
            capture_events: whether detect another widget under the widget.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        self.value: float = 0.
        super().__init__(
            master, position, size, anchor=anchor,
            capture_events=capture_events, gradient_animation=gradient_animation,
            auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.SpinnerStyle(self)
        if widths is None:
            widths = 4, 3
        shapes.Oval(self, width=widths[0])
        shapes.Arc(self, width=widths[1], style="arc")
        self.master.itemconfigure(self.shapes[1].items[0], extent=0, start=90)
        self.command = command
        self.mode = mode
        if mode == "indeterminate":
            self._spin = animations.Animation(
                1200, lambda p: self.master.itemconfigure(
                    self.shapes[1].items[0], start=-p*360, extent=math.cos(p*math.tau)*60+120),
                controller=controllers.linear, repeat=-1, fps=60,
            )
            self._spin.start()

        if default is not None:
            self.set(default)

    def get(self) -> float:
        """Get the progress of the Spinner."""
        if self.mode == "indeterminate":
            warnings.warn(
                "The mode of Spinner is 'indeterminate',"
                "so the method may not get the correct result.",
                UserWarning, 2)
        return self.value

    def set(self, value: float, *, callback: bool = False) -> None:
        """Set the progress of the Spinner."""
        if self.mode == "indeterminate":
            warnings.warn(
                "The mode of Spinner is 'indeterminate', so the method may not have an effect.",
                UserWarning, 2)
        self.value = 0 if value < 0 else 1 if value > 1 else value
        if callback and self.command is not None:
            self.command(value)
        self.master.itemconfigure(self.shapes[1].items[0], extent=-value*359)

    @override
    def destroy(self) -> None:
        """Destroy the widget."""
        if self.mode == "indeterminate":
            self._spin.stop()
        return super().destroy()


class Tooltip(virtual.Widget):
    """A tooltip that can display additional information."""

    def __init__(
        self,
        widget: virtual.Widget,
        size: tuple[int, int] | None = None,
        *,
        text: str = "",
        align: Literal["up", "down", "right", "left", "center"] = "down",
        padding: int = 3,
        family: str | None = None,
        fontsize: int | None = None,
        weight: Literal['normal', 'bold'] = "normal",
        slant: Literal['roman', 'italic'] = "roman",
        underline: bool = False,
        overstrike: bool = False,
        justify: Literal["left", "center", "right"] = "left",
        gradient_animation: bool | None = None,
        auto_update: bool | None = None,
        style: type[virtual.Style] | None = None,
    ) -> None:
        """
        Args:
            widget: the associated widget.
            size: size of the widget.
            text: text of the widget.
            align: align mode of the tooltip.
            padding: extra padding between tooltip and the associated widget.
            family: font family.
            fontsize: font size.
            weight: weight of the text.
            slant: slant of the text.
            underline: whether the text is underline.
            overstrike: whether the text is overstrike.
            justify: justify mode of the text.
            gradient_animation: whether enable gradient_animation.
            auto_update: whether the theme manager update it automatically.
            style: style of the widget.
        """
        if size is None:
            size = utility.get_text_size(
                text, fontsize, family, weight=weight, slant=slant, padding=6, master=widget.master)
        position = [widget.position[0] + widget.size[0]/2 - widget.offset[0],
                    widget.position[1] + widget.size[1]/2 - widget.offset[1]]
        match align:
            case "up":    position[1] -= widget.size[1]/2 + size[1]/2 + padding
            case "down":  position[1] += widget.size[1]/2 + size[1]/2 + padding
            case "right": position[0] += widget.size[0]/2 + size[0]/2 + padding
            case "left":  position[0] -= widget.size[0]/2 + size[0]/2 + padding
        super().__init__(
            widget.master, position, size,
            capture_events=False, gradient_animation=gradient_animation,
            anchor="center", auto_update=auto_update, style=style)
        if style is None:
            self.style = styles.TooltipStyle(self)
        if configs.Env.system == "Windows10":
            shapes.Rectangle(self)
        else:
            shapes.RoundedRectangle(self)
        texts.Information(
            self, text=text, family=family, fontsize=fontsize, weight=weight, slant=slant,
            underline=underline, overstrike=overstrike, justify=justify)
        widget._update_hooks.append(self._display)
        self.forget()

    def get(self) -> str:
        """Get the text of the widget."""
        return self.texts[0].get()

    def set(self, text: str) -> None:
        """Set the text of the widget."""
        return self.texts[0].set(text)

    def _display(self, state: str | None, _: bool) -> None:
        """Show or hide the tooltip."""
        if state is None:
            return
        if state.startswith("hover"):
            self.forget(False)
        elif state.startswith("normal"):
            self.forget()
