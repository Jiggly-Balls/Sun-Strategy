from __future__ import annotations

from typing import TYPE_CHECKING

import pygame
from game_state import State

from core.tileset import Tileset

if TYPE_CHECKING:
    from pygame.event import Event


class Game(State):
    def on_setup(self) -> None:
        self.terrain_tileset = Tileset(
            "assets/Terrain/Ground/Tilemap_flat.png"
        )

    def process_event(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            self.manager.is_running = False

    def process_update(self, dt: float) -> None:
        for x in range(0, 20, 2):
            for y in range(0, 7, 2):
                self.window.blit(
                    self.terrain_tileset.tiles[x, y], (x * 32, y * 32)
                )

        pygame.display.flip()


def hook() -> None:
    Game.manager.load_states(Game)
