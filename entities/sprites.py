from __future__ import annotations

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from typing import Sequence, TypeAlias

    from pygame import Surface

    GroupParam: TypeAlias = pygame.sprite.Group | Sequence[pygame.sprite.Group]


class BaseSprite(pygame.sprite.Sprite):
    def __init__(
        self,
        pos: tuple[int, int],
        surf: Surface,
        group: GroupParam,
        z: int,
    ) -> None:
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(
            -self.rect.width * 0.2, -self.rect.height * 0.75
        )
