from __future__ import annotations
from src.pipe.function import IO, Function
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from packages.sample_package.sample_pipe_two import SamplePipeTwoConfig

class SamplePipeTwoOutput(IO):
    name: str = "Sample Pipe Two Output"

class SamplePipeTwoFunction(Function):
    cls_output: type[SamplePipeTwoOutput] = SamplePipeTwoOutput

    def __init__(self, config: SamplePipeTwoConfig) -> None:
        # do preparatory work when initialized during pipe execution
        self.config: SamplePipeTwoConfig = config

    def __call__(self, input: IO = IO()) -> SamplePipeTwoOutput:
        # pipe execution body, do work and return an output
        return SamplePipeTwoOutput(
            name=self.config.name,
        )
