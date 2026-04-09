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
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
