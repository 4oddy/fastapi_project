from typing import Generic, TypeVar

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')


class UseCase(Generic[InputType, OutputType]):
    """Base class for all use cases"""
    def __call__(self, *args, **kwargs) -> OutputType:
        raise NotImplementedError
