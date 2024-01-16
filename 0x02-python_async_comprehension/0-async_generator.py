#!/usr/bin/env python3
"""
Module for generating random numbers asynchronously.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator yielding a random number
    between 0 and 10 every second for 10 seconds.

    Returns:
        AsyncGenerator[float, None]: The random number generator.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
