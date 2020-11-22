from abc import ABCMeta
from typing import Callable, Generic, Iterable, Sized, TypeVar, Union

import numpy as np
from numpy.random import BitGenerator, Generator, SeedSequence


# TODO (alexandre.marty, 20201107): Turn this TypeVar into numpy.typing.ArrayLike when
#  it is released.
ArrayLike = TypeVar("ArrayLike", np.ndarray, list, tuple)
Scalar = TypeVar("Scalar", int, float)
SolutionType = TypeVar("SolutionType", int, float, list, tuple, np.ndarray)

ScoreFunc = Callable[[SolutionType], float]
VectorizedScoreFunc = Callable[[Iterable[SolutionType]], Iterable[float]]
RngSeed = Union[None, int, ArrayLike, SeedSequence, BitGenerator, Generator]


_T = TypeVar("_T")


class SizedIterable(Iterable[_T], Sized, Generic[_T], metaclass=ABCMeta):
    ...
