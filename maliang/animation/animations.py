# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""Base and standard animation classes.

The animation base class can be inherited or called directly. Other standard
animation classes are best used by direct calls, rather than inheritance.
"""

from __future__ import annotations as _

__all__ = (
    "Animation",
    "MoveWindow",
    "MoveTkWidget",
    "MoveWidget",
    "MoveElement",
    "MoveItem",
    "GradientTkWidget",
    "GradientItem",
    "ScaleFontSize",
)

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any, overload

from ..color import convert, rgb
from ..core import configs, containers
from . import controllers

if TYPE_CHECKING:
    import tkinter

    from ..core import virtual


class Animation:
    """Base animation class.

    Attributes:
        command: callback function, which will be called once per frame.
        controller: a function that controls the animation process.
        end: end function, which is called once at the end of the animation.
        repeat: number of repetitions of the animation.
        repeat_delay: length of the delay before the animation repeats.
        derivation: whether the callback function is derivative.
    """

    def __init__(
        self,
        duration: int,
        command: Callable[[float], Any],
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None:
        """
        Args:
            duration: duration of the animation, in milliseconds.
            command: callback function, which will be called once per frame.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
            derivation: whether the callback function is derivative.
        """
        self.command = command
        self.controller = controller
        self.end = end
        self.repeat = repeat
        self.repeat_delay = repeat_delay
        self.derivation = derivation

        self._delay: int = 1000 // fps
        self._tasks: list[str] = []
        self._count: int = repeat

        if self._delay <= duration:
            self._total_frames, self._leave_ms = divmod(duration, self._delay)
        else:
            self._delay, self._total_frames, self._leave_ms = duration, 1, 0

    @property
    def active(self) -> bool:
        """The active state of the animation."""
        return bool(self._tasks)

    @property
    def count(self) -> int:
        """The number of loops remaining."""
        return self._count

    @overload
    def start(self) -> None: ...

    @overload
    def start(self, *, delay: int) -> str: ...

    def start(self, *, delay: int = 0) -> str | None:
        """Start the animation.

        Args:
            delay: length of the delay before the animation starts.

        Returns:
            If ``delay`` is greater than ``0``, returns the identifier of the
                scheduled task. Otherwise, returns ``None``.
        """
        if delay > 0:
            return configs.Env.root.after(delay, self.start)

        delay, last_percentage = 0, 0

        for i in range(1, self._total_frames + 1):
            delay += self._delay + (i < self._leave_ms)
            percentage = self.controller(i / self._total_frames)
            self._tasks.append(configs.Env.root.after(
                delay, self.command, percentage - last_percentage))

            if self.derivation:
                last_percentage = percentage

        if self.end is not None:
            self._tasks.append(configs.Env.root.after(delay, self.end))

        self._tasks.append(configs.Env.root.after(delay, self._repeat))

        return None

    @overload
    def stop(self) -> None: ...

    @overload
    def stop(self, *, delay: int) -> str: ...

    def stop(self, *, delay: int = 0) -> str | None:
        """Stop the animation.

        Args:
            delay: length of the delay before the animation stops.

        Returns:
            If ``delay`` is greater than ``0``, returns the identifier of the
                scheduled task. Otherwise, returns ``None``.
        """
        if delay > 0:
            return configs.Env.root.after(delay, self.stop)

        while self._tasks:
            configs.Env.root.after_cancel(self._tasks.pop())

        self._count = self.repeat

        return None

    def skip(self, count: int = 1) -> None:
        """Skip some loops.

        Args:
            count: count of skipping.
        """
        self._count = max(self._count-count, 0)

    def _repeat(self) -> None:
        """Processing of the number of repetitions."""
        self._tasks.clear()

        if self._count != 0:
            self._count -= 1
            if task := self.start(delay=self.repeat_delay):
                self._tasks.append(task)
        else:
            self._count = self.repeat


class MoveWindow(Animation):
    """Animation of moving the window."""

    def __init__(
        self,
        window: tkinter.Tk | tkinter.Toplevel | containers.Tk | containers.Toplevel,
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None:
        """
        Args:
            window: the window to be moved.
            offset: relative offset of the coordinates.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
        """
        window.update()
        x0, y0, dx, dy = window.winfo_x(), window.winfo_y(), *offset

        if isinstance(window, (containers.Tk, containers.Toplevel)):
            def callback(p) -> None:
                window.geometry(position=(round(x0+dx*p), round(y0+dy*p)))
        else:
            def callback(p) -> None:
                window.wm_geometry(f"+{round(x0+dx*p)}+{round(y0+dy*p)}")

        super().__init__(
            duration, callback, controller=controller, end=end, fps=fps,
            repeat=repeat, repeat_delay=repeat_delay,
        )


class MoveTkWidget(Animation):
    """Animation of moving ``tkinter.Widget``."""

    def __init__(
        self,
        widget: tkinter.Widget,
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None:
        """
        Args:
            widget: the ``tkinter.Widget`` to be moved.
            offset: relative offset of the coordinates.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.

        Raises:
            RuntimeError: if the widget is not laid out by Place.
        """
        widget.update()

        if info := widget.place_info():
            x0, y0, dx, dy = int(info["x"]), int(info["y"]), *offset
            anchor = info["anchor"]

            super().__init__(
                duration, lambda p: widget.place(
                    x=x0+dx*p, y=y0+dy*p, anchor=anchor),
                controller=controller, end=end, fps=fps, repeat=repeat,
                repeat_delay=repeat_delay,
            )
        else:
            raise RuntimeError("The tkinter widget is not laid out by Place.")


class MoveWidget(Animation):
    """Animation of moving ``virtual.Widget``."""

    @overload
    def __init__(
        self,
        widget: virtual.Widget,
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None: ...

    @overload
    def __init__(
        self,
        widget: Sequence[virtual.Widget],
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None: ...

    def __init__(
        self,
        widget: virtual.Widget | Sequence[virtual.Widget],
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None:
        """
        Args:
            widget: the ``virtual.Widget`` to be moved.
            offset: relative offset of the coordinates.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
        """
        if isinstance(widget, Sequence):
            def command(p: float) -> None:
                dx, dy = offset[0]*p, offset[1]*p
                for w in widget:
                    w.move(dx, dy)
        else:
            def command(p: float) -> None:
                widget.move(offset[0]*p, offset[1]*p)

        super().__init__(
            duration, command, controller=controller, end=end, fps=fps,
            repeat=repeat, repeat_delay=repeat_delay, derivation=True,
        )


class MoveElement(Animation):
    """Animation of moving ``virtual.Element``."""

    @overload
    def __init__(
        self,
        element: virtual.Element,
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None: ...

    @overload
    def __init__(
        self,
        element: Sequence[virtual.Element],
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None: ...

    def __init__(
        self,
        element: virtual.Element | Sequence[virtual.Element],
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None:
        """
        Args:
            element: the ``virtual.Element`` to be moved.
            offset: relative offset of the coordinates.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
        """
        if isinstance(element, Sequence):
            def command(p: float) -> None:
                dx, dy = offset[0]*p, offset[1]*p
                for e in element:
                    e.move(dx, dy)
        else:
            def command(p: float) -> None:
                element.move(offset[0]*p, offset[1]*p)

        super().__init__(
            duration, command, controller=controller, end=end, fps=fps,
            repeat=repeat, repeat_delay=repeat_delay, derivation=True,
        )


class MoveItem(Animation):
    """Animation of moving a item of ``tkinter.Canvas``."""

    @overload
    def __init__(
        self,
        canvas: tkinter.Canvas | containers.Canvas,
        item: int,
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None: ...

    @overload
    def __init__(
        self,
        canvas: tkinter.Canvas | containers.Canvas,
        item: Sequence[int],
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None: ...

    def __init__(
        self,
        canvas: tkinter.Canvas | containers.Canvas,
        item: int | Sequence[int],
        offset: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
    ) -> None:
        """
        Args:
            canvas: an instance of ``tkinter.Canvas`` that contains the item.
            item: the item to be moved.
            offset: relative offset of the coordinates.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
        """
        if isinstance(item, Sequence):
            def command(p: float) -> None:
                dx, dy = offset[0]*p, offset[1]*p
                for i in item:
                    canvas.move(i, dx, dy)
        else:
            def command(p: float) -> None:
                canvas.move(item, offset[0]*p, offset[1]*p)

        super().__init__(
            duration, command, controller=controller, end=end, fps=fps,
            repeat=repeat, repeat_delay=repeat_delay, derivation=True,
        )


class GradientTkWidget(Animation):
    """Animation of making the color of ``tkinter.Widget`` to be gradient."""

    @overload
    def __init__(
        self,
        widget: tkinter.Widget,
        parameter: str,
        colors: tuple[str, str],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        widget: Sequence[tkinter.Widget],
        parameter: str,
        colors: tuple[str, str],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None: ...

    def __init__(
        self,
        widget: tkinter.Widget | Sequence[tkinter.Widget],
        parameter: str,
        colors: tuple[str, str],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None:
        """
        Args:
            widget: the ``tkinter.Widget`` whose color is to be gradient.
            parameter: parameter name of widget that is to be modified in color.
            colors: a tuple of the initial and ending colors.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
            derivation: whether the callback function is derivative.

        Raises:
            ValueError: if any color in ``colors`` is an empty string.
        """
        if not all(colors):
            raise ValueError(f"Null characters ({colors}) cannot be parsed!")

        c1, c2 = convert.str_to_rgb(colors[0]), convert.str_to_rgb(colors[1])

        if isinstance(widget, Sequence):
            def command(p: float) -> None:
                value = convert.rgb_to_hex(rgb.transition(c1, c2, p))
                for w in widget:
                    w.configure({parameter: value})
        else:
            def command(p: float) -> None:
                widget.configure(
                    {parameter: convert.rgb_to_hex(rgb.transition(c1, c2, p))})

        super().__init__(
            duration, command, controller=controller, end=end, fps=fps,
            repeat=repeat, repeat_delay=repeat_delay, derivation=derivation,
        )


class GradientItem(Animation):
    """Animation of making the color of canvas item to be gradient."""

    @overload
    def __init__(
        self,
        canvas: tkinter.Canvas | containers.Canvas,
        item: int,
        parameter: str,
        colors: tuple[str, str],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        canvas: tkinter.Canvas | containers.Canvas,
        item: Sequence[int],
        parameter: str,
        colors: tuple[str, str],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None: ...

    def __init__(
        self,
        canvas: tkinter.Canvas | containers.Canvas,
        item: int | Sequence[int],
        parameter: str,
        colors: tuple[str, str],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None:
        """
        Args:
            canvas: an instance of ``tkinter.Canvas`` that contains the item.
            item: item whose color is to be gradient.
            parameter: parameter name of item that is to be modified in color.
            colors: a tuple of the initial and ending colors.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
            derivation: whether the callback function is derivative.

        Raises:
            ValueError: if any color in ``colors`` is an empty string.
        """
        if not all(colors):
            raise ValueError(f"Null characters ({colors}) cannot be parsed!")

        c1, c2 = convert.str_to_rgb(colors[0]), convert.str_to_rgb(colors[1])

        if isinstance(item, Sequence):
            def command(p: float) -> None:
                value = convert.rgb_to_hex(rgb.transition(c1, c2, p))
                for i in item:
                    canvas.itemconfigure(i, {parameter: value})
        else:
            def command(p: float) -> None:
                canvas.itemconfigure(
                    item, {parameter: convert.rgb_to_hex(rgb.transition(c1, c2, p))})

        super().__init__(
            duration, command, controller=controller, end=end, fps=fps,
            repeat=repeat, repeat_delay=repeat_delay, derivation=derivation,
        )


class ScaleFontSize(Animation):
    """Animation of scaling the font size of ``virtual.Text``."""

    @overload
    def __init__(
        self,
        text: virtual.Text,
        sizes: float,
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        text: virtual.Text,
        sizes: tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None: ...

    def __init__(
        self,
        text: virtual.Text,
        sizes: float | tuple[float, float],
        duration: int,
        *,
        controller: Callable[[float], float] = controllers.linear,
        end: Callable[[], Any] | None = None,
        fps: int = 30,
        repeat: int = 0,
        repeat_delay: int = 0,
        derivation: bool = False,
    ) -> None:
        """
        Args:
            text: an instance of ``virtual.Text`` that needs to be scaled.
            sizes: a tuple of the initial and ending sizes or target font size.
            duration: duration of the animation, in milliseconds.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            fps: frame rate of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
            derivation: whether the callback function is derivative.
        """
        if isinstance(sizes, (int, float)):
            sizes = -abs(sizes)
            sizes = text.font.cget("size"), sizes - text.font.cget("size")
        else:
            sizes = -abs(sizes[0]), -abs(sizes[1])
            sizes = sizes[0], sizes[1] - sizes[0]

        super().__init__(
            duration, lambda p: (
                text.font.config(size=round(sizes[0] + sizes[1]*p)),
                text.update()),
            controller=controller, end=end, fps=fps, repeat=repeat,
            repeat_delay=repeat_delay, derivation=derivation,
        )
