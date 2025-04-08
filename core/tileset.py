from __future__ import annotations

from typing import TYPE_CHECKING

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
    ) -> None:
        self.file = file
        self.size = size
        self.margin = margin
        self.spacing = spacing
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.tiles = self.load()

    def load(self) -> dict[tuple[int, int], Surface]:
        tiles: dict[tuple[int, int], Surface] = {}
        x0 = y0 = self.margin
        w, h = self.rect.size
        dx = self.size[0] + self.spacing
        dy = self.size[1] + self.spacing

        for x in range(x0, w, dx):
            for y in range(y0, h, dy):
                tile = pygame.Surface(self.size)
                tile.blit(self.image, (0, 0), (x, y, *self.size))
                tiles[(x // dx, y // dx)] = tile

        return tiles


if __name__ == "__main__":
    from pprint import pprint

    terrain = Tileset("assets/Terrain/Ground/Tilemap_flat.png")
    pprint(terrain.tiles)
