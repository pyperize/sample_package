from __future__ import annotations
import src.pipe as pipe
import packages.sample_package.sample_pipe_two as sample_pipe_two
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.manager import Manager
    from src.ui.common import ConfigPage

class SamplePipeTwoPipe(pipe.Pipe):
    cls_name: str = "Sample Pipe Two"
    cls_config: type[pipe.Config] = sample_pipe_two.SamplePipeTwoConfig
    cls_function: type[pipe.Function] = sample_pipe_two.SamplePipeTwoFunction

    def __init__(self, name: str, manager: Manager, config: sample_pipe_two.SamplePipeTwoConfig) -> None:
        super().__init__(name, manager, config)
        self.config: sample_pipe_two.SamplePipeTwoConfig = config

    def config_ui(self, manager: Manager, config_page: ConfigPage) -> sample_pipe_two.SamplePipeTwoConfigUI:
        return sample_pipe_two.SamplePipeTwoConfigUI(self, manager, config_page)

    def play(self, manager: Manager) -> None:
        if self.playing:
            return
        self.playing = True
        # do preparatory work before pipe execution

    def stop(self, manager: Manager, result: sample_pipe_two.SamplePipeTwoOutput) -> None:
        if not self.playing:
            return
        self.playing = False
        # do cleanup work after pipe execution
