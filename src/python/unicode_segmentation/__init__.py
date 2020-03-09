import itertools
from typing import List
from unicode_segmentation._unicode_segmentation import ffi, lib


__all__ = ["graphemes"]


class Error(Exception):
    pass


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def _pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def graphemes(s: bytes) -> List[int]:
    output = ffi.new("unsigned long[]", [0] * len(s))
    output_length = ffi.new("unsigned long[]", [len(s)])
    c_str = ffi.new("char[]", s)
    result = lib.graphemes(c_str, output, output_length)
    if not result:
        raise Error("Failed to segment string into graphemes")
    indices = (output[i] for i in range(output_length[0]))
    for start, end in _pairwise(itertools.chain(indices, [len(s)])):
        yield s[start:end]
