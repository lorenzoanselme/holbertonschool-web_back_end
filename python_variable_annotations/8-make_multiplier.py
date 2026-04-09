#!/usr/bin/env python3
"""Module that provides a multiplier factory function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): multiplier value

    Returns:
        Callable[[float], float]: function that multiplies a float
    """
    def multiply(n: float) -> float:
        """Multiply a float by the outer multiplier."""
        return n * multiplier

    return multiply
