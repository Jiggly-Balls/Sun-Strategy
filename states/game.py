from __future__ import annotations

from typing import TYPE_CHECKING

import pygame
from game_state import State

from core.tileset import Tileset

if TYPE_CHECKING:
    from pygame.event import Event

# import time
from pprint import pprint


class Game(State):
    def on_setup(self) -> None:
        self.terrain_tileset = Tileset("assets/Terrain/Ground/Flat.png")
        self.rocks_tileset = Tileset(
            "assets/Terrain/Water/Rocks/Rocks_01.png", (128, 128)
        )
        print(len(self.rocks_tileset.tiles))
        pprint(self.rocks_tileset.tiles)

    def process_event(self, event: Event) -> None:
        if event.type == pygame.QUIT:
            self.manager.is_running = False

    def process_update(self, dt: float) -> None:
        # for x in range(self.rocks_tileset.x_total + 1):
        #     for y in range(self.rocks_tileset.y_total + 1):
        #         surf = self.rocks_tileset.tiles[x, y]
        #         surf = pygame.transform.scale(surf, (32, 32))
        #         self.window.blit(surf, (x * 32, y * 32))
        #         print(x, y)
        #         time.sleep(0.5)
        pygame.display.update()


def hook() -> None:
    Game.manager.load_states(Game)
