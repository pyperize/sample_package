from __future__ import annotations
import src.pipe as pipe
import packages.sample_package.sample_pipe_one as sample_pipe_one
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.manager import Manager
    from src.ui.common import ConfigPage

class SamplePipeOnePipe(pipe.Pipe):
    cls_name: str = "Sample Pipe One"
    cls_config: type[pipe.Config] = sample_pipe_one.SamplePipeOneConfig
    cls_function: type[pipe.Function] = sample_pipe_one.SamplePipeOneFunction

    def __init__(self, name: str, manager: Manager, config: sample_pipe_one.SamplePipeOneConfig) -> None:
        super().__init__(name, manager, config)
        self.config: sample_pipe_one.SamplePipeOneConfig = config

    def config_ui(self, manager: Manager, config_page: ConfigPage) -> sample_pipe_one.SamplePipeOneConfigUI:
        return sample_pipe_one.SamplePipeOneConfigUI(self, manager, config_page)

    def play(self, manager: Manager) -> None:
        if self.playing:
            return
        self.playing = True
        # do preparatory work before pipe execution

    def stop(self, manager: Manager, result: sample_pipe_one.SamplePipeOneOutput) -> None:
        if not self.playing:
            return
        self.playing = False
        # do cleanup work after pipe execution
