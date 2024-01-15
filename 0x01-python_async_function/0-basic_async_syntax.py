#!/usr/bin/env python3
"""
This module contains a coroutine that waits
for a random delay and returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for
    a random delay and returns it.

    Parameters:
    max_delay (int): Maximum delay

    Returns:
    float: Random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
