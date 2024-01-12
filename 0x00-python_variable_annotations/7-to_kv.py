#!/usr/bin/env python3
"""
This module provides a function to create a tuple.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and the square of an int or float.

    Parameters:
    k (str): The string to include in the tuple.
    v (Union[int, float]): The int or float to square.

    Returns:
    Tuple[str, float]: The created tuple.
    """
    return k, v**2
