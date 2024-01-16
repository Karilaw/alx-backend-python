#!/usr/bin/env python3
"""
Module for measuring runtime.
"""

import asyncio
import time
from typing import List
from .1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
        float: The total runtime.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()

    return end_time - start_time
