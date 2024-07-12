from __future__ import annotations
from packages.sample_package.sample_pipe_one import SamplePipeOnePipe
from packages.sample_package.sample_pipe_two import SamplePipeTwoPipe
from src.package.package import Package
from typing import TYPE_CHECKING, Iterable
if TYPE_CHECKING:
    from src.pipe import Pipe

class SamplePipeOnePackage(Package):
    name: str = "Sample Package"
    _pipes: Iterable[type[Pipe]] = [SamplePipeOnePipe, SamplePipeTwoPipe]
    dependencies: dict[str, Package] = {}
