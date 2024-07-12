from __future__ import annotations
import flet as ft
from src.pipe.config import Config, ConfigUI
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.manager import Manager
    from src.ui.common import ConfigPage
    from packages.sample_package.sample_pipe_two import SamplePipeTwoPipe

class SamplePipeTwoConfig(Config):
    name: str = "Sample Pipe Two Output"

class SamplePipeTwoConfigUI(ConfigUI):
    def __init__(self, instance: SamplePipeTwoPipe, manager: Manager, config_page: ConfigPage, content: ft.Control | None = None) -> None:
        self.instance: SamplePipeTwoPipe = instance
        # build configuration UI
        super().__init__(instance, manager, config_page, ft.Column(spacing=20, controls=[
            ft.TextField(self.instance.config.name, label="Output Name", border_color="grey"),
        ]))

    def dismiss(self) -> None:
        # save configuration data
        self.instance.config = SamplePipeTwoConfig(
            name=self.content.controls[0].value,
        )
