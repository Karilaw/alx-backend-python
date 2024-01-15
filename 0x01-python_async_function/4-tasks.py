#!/usr/bin/env python3
"""
This module contains a function that returns an asyncio.Task.
"""

import asyncio
from typing import Callable, List
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay and returns it.

    Parameters:
    max_delay (int): Maximum delay

    Returns:
    float: Random delay
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> Callable:
    """
    Function that returns an asyncio.Task.

    Parameters:
    max_delay (int): Maximum delay

    Returns:
    Callable: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous coroutine that spawns task_wait_random n times.

    Parameters:
    n (int): Number of times to spawn task_wait_random
    max_delay (int): Maximum delay

    Returns:
    List[float]: List of delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
