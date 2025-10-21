# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""Controller generator and standard control functions.

Definition of control function::

    def control_function(t: float, /) -> float:
        '''Control function for animation.

        Args:
            t: the percentage of time.

        Returns:
            a multiple of the cardinality of the animation.
        '''
"""

from __future__ import annotations as _

__all__ = (
    "generate",
    "linear",
    "smooth",
    "rebound",
    "ease_in",
    "ease_out",
)

import functools
import math
import warnings
from collections.abc import Callable
from typing import Literal, overload


def _map_t(start: float, end: float) -> Callable[[float], float]:
    """Map parameters in any range between ``0`` and ``1``.

    Args:
        start: the first value of the parameter of the base function.
        end: the last value of the parameter of the base function.

    Returns:
        A function that maps parameters in any range between ``0`` and ``1``.
    """
    def _mapper(t: float) -> float:
        return start + t * (end-start)

    return _mapper


def _map_y(
    base: Callable[[float], float],
    end: float,
) -> Callable[[float], float]:
    """Map the final return value to ``1``.

    Args:
        base: base function.
        end: the last value of the parameter of the base function.

    Returns:
        A function that maps the final return value to ``1``.
    """
    @functools.wraps(base)
    def _mapper(t: float) -> float:
        return base(t) / base(end)

    return _mapper


@overload
def generate(
    base: Callable[[float], float],
    start: float,
    end: float,
) -> Callable[[float], float]: ...


@overload
def generate(
    base: Callable[[float], float],
    start: float,
    end: float,
    *,
    map_y: Literal[False] = False,
) -> Callable[[float], float]: ...


def generate(
    base: Callable[[float], float],
    start: float,
    end: float,
    *,
    map_y: bool = True,
) -> Callable[[float], float]:
    """Generate a control function from an ordinary mathematical function.

    Args:
        base: base function, an ordinary mathematical function.
        start: the first value of the parameter of the base function.
        end: the last value of the parameter of the base function.
        map_y: whether map the final return value to ``1``.

    Returns:
        A control function.
    """
    if map_y:
        if math.isclose(base(end), 0, abs_tol=1e-9):
            warnings.warn(
                "The end value of the base function is too close to 0, "
                "which may cause the result control function to be "
                "inaccurate or even throw an error.", UserWarning, 2)

        @functools.wraps(base)
        def _mapper(t: float) -> float:
            return _map_y(base, end)(_map_t(start, end)(t))
    else:
        @functools.wraps(base)
        def _mapper(t: float) -> float:
            return base(_map_t(start, end)(t))

    return _mapper


def linear(t: float, /) -> float:
    """Speed remains the same."""
    return t


def smooth(t: float, /) -> float:
    """Speed is slow first, then fast and then slow. (slow -> fast -> slow)"""
    return (1 - math.cos(t*math.pi)) / 2


def rebound(t: float, /) -> float:
    """Before the end, displacement will bounce off a bit."""
    return generate(math.sin, 0, (math.pi+1) / 2)(t)


def ease_in(t: float, /) -> float:
    """Gradually accelerate. (slow -> fast)"""
    return generate((lambda x: math.pow(2, 10*x - 10)), 0, 1)(t)


def ease_out(t: float, /) -> float:
    """Gradually decelerate. (fast -> slow)"""
    return generate((lambda x: 1 - math.pow(2, -10*x)), 0, 1)(t)
