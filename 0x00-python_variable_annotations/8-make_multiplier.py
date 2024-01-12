#!/usr/bin/env python3
"""
This module provides a function to create a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by.

    Parameters:
    multiplier (float): The multiplier to use.

    Returns:
    Callable[[float], float]: The created multiplier function.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier

    return multiplier_func
