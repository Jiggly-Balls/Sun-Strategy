from __future__ import annotations

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Group

from core.config import SCREEN_HEIGHT, SCREEN_WIDTH

if TYPE_CHECKING:
    from pygame import Surface


class Camera(Group):
    def __init__(self, window: Surface) -> None:
        super().__init__()
        self.window = window
        self.offset = pygame.math.Vector2()

    def draw(self, player: Player) -> None:
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in sorted(
                self.sprites(), key=lambda sprite: sprite.rect.centery
            ):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.window.blit(sprite.image, offset_rect)
