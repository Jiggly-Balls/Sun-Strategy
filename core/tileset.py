from __future__ import annotations

from typing import TYPE_CHECKING

import numpy
import pygame

if TYPE_CHECKING:
    from pygame import Surface


class Tileset:
    def __init__(
        self,
        file: str,
        size: tuple[int, int] = (32, 32),
        margin: int = 0,
        spacing: int = 0,
        pack: int = 1,
    ) -> None:
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.pack = pack // 2

        self._x_total: None | int = None
        self._y_total: None | int = None
        self.tiles = self.load()

    @property
    def x_total(self) -> int:
        return self._x_total

    @property
    def y_total(self) -> int:
        return self._y_total

    def load(self) -> dict[tuple[int, int], Surface]:
        tiles: dict[tuple[int, int], Surface] = {}
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        self._x_total = (w // dx) - 1
        self._y_total = (h // dy) - 1

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size, pygame.SRCALPHA, 32)
                tile = tile.convert_alpha()
                tile.blit(self.image, (0, 0), (x, y, *self.size))

                tile = pygame.transform.scale(tile, (64, 64))

                # np_array = pygame.surfarray.array_alpha(tile)
                # if not numpy.any(np_array != 0):
                #     print("no alpa")
                #     continue

                # if numpy.all(np_array == np_array[0]):
                #    print("all sam")
                #    continue
                tiles[(x // dx, y // dx)] = tile

        return tiles


if __name__ == "__main__":
    from pprint import pprint

    terrain = Tileset("assets/Terrain/Water/Rocks/Rocks_01.png")
    pprint(terrain.tiles)
    print(terrain.x_total, terrain.y_total)
