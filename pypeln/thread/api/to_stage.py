import typing as tp

from pypeln.utils import A

from ..stage import Stage
from .from_iterable import from_iterable


def to_stage(obj: tp.Union[Stage[A], tp.Iterable[A]], maxsize: int) -> Stage[A]:

    return obj if isinstance(obj, Stage) else from_iterable(obj, maxsize=maxsize)
