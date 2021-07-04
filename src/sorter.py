#!/usr/bin/env python

"""
Module with Sorter class to run some sorting algorithms on sequence objects

Included algorithms:
1) Bubble sort
2) Quick sort
3) Selection sort
4) Insertion sort
5) Merge sort
"""

from typing import TypeVar, Generic
from src.algorithms.bubble_sort import bubble_sort

__author__ = "Pei Sheng Tan"
__copyright__ = "Copyright (C) 2021 Pei Sheng Tan"
__license__ = "GPL"
__version__ = "0.1"
__email__ = "larstanps@gmail.com"
__status__ = "Prototype"


T = TypeVar('T')


class Sorter:
    """
    Sorter to hold a sequence object and call available sorting algorithms
    """

    def __init__(self, collection: Generic[T]):
        self.collection = collection

    def bubble_sort(self, ascending: bool) -> None:
        """
        Sorts a sequence of ordered elements with bubble sort.

        :param ascending: boolean to indicate if sorting in ascending order. True for ascending, False for descending.
        """
        bubble_sort(self.collection, ascending)

    def quick_sort(self, ascending: bool) -> None:
        # TODO: implementation
        pass

    def selection_sort(self, ascending: bool) -> None:
        # TODO: implementation
        pass

    def insertion_sort(self, ascending: bool) -> None:
        # TODO: implementation
        pass

    def merge_sort(self, ascending: bool) -> None:
        # TODO: implementation
        pass