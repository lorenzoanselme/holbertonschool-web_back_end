#!/usr/bin/env python3
"""Module that provides concurrent coroutine execution."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return sorted delays.

    Args:
        n (int): number of coroutines
        max_delay (int): maximum delay

    Returns:
        List[float]: list of delays in ascending order
    """
    delays = []

    for _ in range(n):
        delay = await wait_random(max_delay)

        # insertion pour garder l'ordre sans sort()
        i = 0
        while i < len(delays) and delays[i] < delay:
            i += 1
        delays.insert(i, delay)

    return delays
