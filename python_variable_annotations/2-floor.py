#!/usr/bin/env python3
"""Module that provides a function to return the floor of a float."""

import math


def floor(n: float) -> int:
    """Return the floor of a float.

    Args:
        n (float): number to round down

    Returns:
        int: floor of n
    """
    return math.floor(n)
