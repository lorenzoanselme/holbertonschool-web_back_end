#!/usr/bin/env python3
"""Module that provides an asynchronous generator."""

import asyncio
import random


async def async_generator():
    """Yield random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
