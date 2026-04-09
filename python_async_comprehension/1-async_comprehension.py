#!/usr/bin/env python3
"""Module that defines a coroutine using async comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random floats using async comprehension.

    Returns:
        List[float]: list of 10 random float values
    """
    return [i async for i in async_generator()]
