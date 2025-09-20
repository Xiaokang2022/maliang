# Copyright (c) 2024-2025 Xiaokang2022. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for details.

"""Some functions about RGB codes."""

from __future__ import annotations as _

__all__ = (
    "contrast",
    "transition",
    "blend",
    "gradient",
)

import operator
import statistics
from typing import TYPE_CHECKING

from ..animation import controllers

if TYPE_CHECKING:
    from collections.abc import Callable


def contrast(
    value: tuple[int, int, int],
    /,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[int, int, int]:
    """Get the contrasting color of a RGB code.

    Args:
        value: a RGB code.
        channels: three color channels.

    Returns:
        The contrasting color of the input RGB code.
    """
    return tuple(255-v if c else v for v, c in zip(value, channels))


def transition(
    first: tuple[int, int, int],
    second: tuple[int, int, int],
    rate: float,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
) -> tuple[int, int, int]:
    """Transition one color to another proportionally.

    Args:
        first: the first RGB code.
        second: the second RGB code.
        rate: transition rate.
        channels: three color channels.

    Returns:
        The transitioned RGB code.
    """
    return tuple(first[i] + round((second[i]-first[i]) * rate * v) for i, v in enumerate(channels))


def blend(
    *values: tuple[int, int, int],
    weights: list[float] | None = None,
) -> tuple[int, int, int]:
    """Mix colors by weight.

    Args:
        values: RGB codes.
        weights: weight list, default value indicates the same weights.

    Returns:
        The blended RGB code.
    """
    colors = zip(*values)

    if weights is None:  # Same weights
        return tuple(map(lambda x: round(statistics.fmean(x)), colors))

    total = sum(weights)
    weights = tuple(map(lambda x: x/total, weights))  # Different weights

    return tuple(round(sum(map(operator.mul, c, weights))) for c in colors)


def gradient(
    first: tuple[int, int, int],
    second: tuple[int, int, int],
    count: int,
    rate: float = 1,
    *,
    channels: tuple[bool, bool, bool] = (True, True, True),
    controller: Callable[[float], float] = controllers.linear,
) -> list[tuple[int, int, int]]:
    """Get a list of color gradients from one color to another proportionally.

    Args:
        first: the first RGB code.
        second: the second RGB code.
        count: the number of gradients.
        rate: transition rate.
        channels: three color channels.
        controller: control function, default is linear.

    Returns:
        A list of color gradients from the first RGB code to the second RGB
            code.
    """
    rgb_list: list[tuple[int, int, int]] = []
    delta = tuple(rate * (j-i) * k for i, j, k in zip(first, second, channels))

    for x in (controller(i/count) for i in range(count)):
        rgb_list.append(tuple(c + round(x*r) for c, r in zip(first, delta)))

    return rgb_list
