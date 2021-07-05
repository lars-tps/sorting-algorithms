#!/usr/bin/env python

"""
Module containing bubble sort algorithm
"""

from typing import TypeVar, Generic
import unittest

__author__ = "Pei Sheng Tan"
__copyright__ = "Copyright (C) 2021 Pei Sheng Tan"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "larstanps@gmail.com"
__status__ = "Production"

T = TypeVar('T')


def swap(seq: Generic[T], i: int, j: int) -> None:
    """
    Swaps the places of two elements in a sequence object

    time complexity: O(1)

    :param seq: a sequence object of generic elements
    :param i: index of an element
    :param j: index of an element
    """
    seq[i], seq[j] = seq[j], seq[i]


def bubble_sort(seq: Generic[T], ascending: bool) -> None:
    """
    Sorts a sequence of ordered elements with bubble sort.

    time complexity:
        outer loop runs n - 1 times, inner loop runs (n-1)+(n-2)+(n-3)...+1 times.
        factoring out n, inner loop runs n*(0-1-2-3...+1/n)

        worst case occurs when sequence is sorted in reverse order so swap happens in every outer iteration.
        considering most significant growth factors, this algorithm has a O(n^2) worst case time complexity.

        best case occurs when sequence is sorted in correct order, nothing is swapped and so the outer-loop only
        runs once. Inner loop still runs n - 1 times in the first iteration of the outer-loop.
        O(n) best case time complexity

    stability: Bubble sort is stable due to the use of strict '>' and '<' operators

    incremental: Bubble Sort is incremental if new elements are added to the front (at index 0) of sequence,
                 not incremental if added at the rear of the sequence.

    :param seq: a sequence object of generic elements
    :param ascending: boolean to indicate if sorting in ascending order. True for ascending, False for descending.
    """
    n = len(seq)

    for mark in range(n - 1, 0, -1):  # go from n-1 to 1
        swap_happened = False
        for i in range(mark):
            if ascending and seq[i] > seq[i + 1]:
                swap(seq, i, i + 1)
                swap_happened = True
            elif not ascending and seq[i] < seq[i + 1]:
                swap(seq, i, i + 1)
                swap_happened = True
        if not swap_happened:
            break


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        ls = [1, 4, 3, 2, 6, 5, 7, 9, 10, 8]

        # ascending test
        bubble_sort(ls, True)
        sorted_ls = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(ls, sorted_ls)

        # descending test
        bubble_sort(ls, False)
        reverse_list = [10,9,8,7,6,5,4,3,2,1]
        self.assertEqual(ls, reverse_list)


if __name__ == "__main__":
    unittest.main()
