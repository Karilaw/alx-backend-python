#!/usr/bin/env python3
"""
This module provides a function to calculate the sum.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]):

    Returns:
    float: The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
