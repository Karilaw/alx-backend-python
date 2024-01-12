#!/usr/bin/env python3
"""
This module provides a function to calculate.
"""

from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculates the length of elements in a list.

    Parameters:
    lst (Iterable[Sequence]): The list of elements to calculate.

    Returns:
    List[Tuple[Sequence, int]]:
    """
    return [(i, len(i)) for i in lst]
