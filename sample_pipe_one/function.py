from __future__ import annotations
from src.pipe.function import IO, Function
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from packages.sample_package.sample_pipe_one import SamplePipeOneConfig

class SamplePipeOneOutput(IO):
    name: str = "Sample Pipe One Output"

class SamplePipeOneFunction(Function):
    cls_output: type[SamplePipeOneOutput] = SamplePipeOneOutput

    def __init__(self, config: SamplePipeOneConfig) -> None:
        # do preparatory work when initialized during pipe execution
        self.config: SamplePipeOneConfig = config

    def __call__(self, input: IO = IO()) -> SamplePipeOneOutput:
        # pipe execution body, do work and return an output
        return SamplePipeOneOutput(
            name=self.config.name,
        )
