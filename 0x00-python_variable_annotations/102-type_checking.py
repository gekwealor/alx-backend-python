#!/usr/bin/env python3
'''
Copies items in Tuple
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    Creates copies of items in Tuple

    Args:
        lst: Tuple of items
        factor: Number of ints in tuple

    Return: Copies of tuple
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
