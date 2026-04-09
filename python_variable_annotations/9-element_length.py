#!/usr/bin/env python3
"""Module that provides a function to get element lengths."""

from typing import Iterable, Sequence, List, Tuple


def element_length(
    lst: Iterable[Sequence]
) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with elements and their lengths.

    Args:
        lst (Iterable[Sequence]): iterable of sequences

    Returns:
        List[Tuple[Sequence, int]]: list of tuples (element, length)
    """
    return [(i, len(i)) for i in lst]
