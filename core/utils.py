from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pygame import Surface
    from pygame.sprite import Sprite


class Animation:
    def __init__(
        self,
        frames: dict[str, list[Surface]],
        *,
        auto_set_status: bool = False,
        start_status: None | str = None,
        sprite: None | Sprite = None,
        speed: int = 4,
        ignore_invalid_state: bool = True,
    ) -> None:
        self.frames = frames
        self.auto_set_status = auto_set_status
        self.sprite = sprite
        self.speed = speed
        self.ignore_invalid_state = ignore_invalid_state

        self.status: None | str = None
        self.current_frame = 0
        self.max_frames = 0
        if start_status is not None:
            self.set_status(start_status)

        if self.auto_set_status:
            self.set_status(tuple(self.frames.keys())[0])

    def get_frame(self, frame: int) -> Surface:
        return self.frames[self.status][frame]

    def set_status(self, animation: str) -> None:
        if not self.ignore_invalid_state:
            assert animation in self.frames, (
                f"{animation} is not present in list of animations: {self.frames.keys()}"
            )

        if animation in self.frames:
            self.status = animation
            self.max_frames = len(self.frames[self.status]) - 1

    def play_status(self, dt: float) -> Surface:
        if not self.ignore_invalid_state:
            assert self.ignore_invalid_state or self.status is not None, (
                "No animation state has been set to run"
            )

        self.current_frame += self.speed * dt
        if self.current_frame > self.max_frames:
            self.current_frame = 0

        return self.frames[self.status][round(self.current_frame)]

    def play_status_ip(self, dt: float) -> None:
        assert self.sprite is not None, (
            "No sprite has been passed to play the status in-place."
        )

        self.current_frame += self.speed * dt
        if self.current_frame > self.max_frames:
            self.current_frame = 0
        self.sprite.image = self.frames[self.status][round(self.current_frame)]
