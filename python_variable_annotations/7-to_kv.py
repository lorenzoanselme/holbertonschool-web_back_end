#!/usr/bin/env python3
"""Module that provides a function to return a key-value tuple."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number.

    Args:
        k (str): key
        v (Union[int, float]): value to square

    Returns:
        Tuple[str, float]: tuple containing k and v squared
    """
    return (k, float(v ** 2))
