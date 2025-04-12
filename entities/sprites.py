from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from typing import Sequence, TypeAlias

    from pygame import Surface

    from core.utils import Animation

    GroupParam: TypeAlias = pygame.sprite.Group | Sequence[pygame.sprite.Group]


class BaseSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        surf: Surface,
        z: int,
        group: GroupParam,
    ) -> None:
        """The base class to all sprites.

        Parameters
        ----------
        pos
            The position of the sprite in a tuple of x and y coordinate respectively.
        surf
            The surface object of the sprite.
        z
            The z index or the depth value of the sprite.
        group
            To which group the sprite belongs to.
        """
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z


class AnimatedSprite(BaseSprite):
    def __init__(
        self,
        pos: tuple[int, int],
        z: int,
        group: GroupParam,
        animation: Animation,
    ) -> None:
        """The base class to all sprites.

        Parameters
        ----------
        pos
            The position of the sprite in a tuple of x and y coordinate respectively.
        z
            The z index or the depth value of the sprite.
        group
            To which group the sprite belongs to.
        animation
            The animation instance for the sprite to play.
        """

        super().__init__(
            pos=pos, surf=animation.get_frame(0), z=z, group=group
        )
        self.animation = animation
        self.animation.sprite = self

    def update(self, dt: float) -> None:
        self.animation.play_status_ip(dt=dt)
