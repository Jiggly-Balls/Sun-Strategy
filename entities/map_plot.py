from __future__ import annotations

import random
from typing import TYPE_CHECKING

import pygame
from perlin_noise import PerlinNoise

from core.config import PIXEL_SIZE, AssetIdentifier, Layers
from core.tileset import Tileset
from core.utils import Animation
from entities.sprites import AnimatedSprite, BaseSprite

if TYPE_CHECKING:
    from typing import Sequence

    from pygame.sprite import Group


class MapPlot:
    def __init__(
        self,
        size: tuple[int, int],
        terrain_tileset: Tileset,
        tree_tileset: Tileset,
        water_tileset: Tileset,
        water_rocks_tileset: Sequence[Tileset],
        foam_tileset: Tileset,
    ) -> None:
        self.size = size
        self.terrain_tiles = terrain_tileset
        self.tree_tileset = tree_tileset
        self.water_tileset = water_tileset
        self.water_rocks_tileset = water_rocks_tileset
        self.foam_tileset = foam_tileset
        self.map_cache: dict[tuple[int, int], list[str]] = {}
        self.surface_layer = pygame.Surface(
            (size[0] * PIXEL_SIZE, size[1] * PIXEL_SIZE)
        )
        self.rock_layer = pygame.Surface(
            (size[0] * PIXEL_SIZE, size[1] * PIXEL_SIZE)
        )

    def create_map(self, group: Group) -> None:
        noise = PerlinNoise(octaves=0.25, seed=random.random() * 100)
        xpix, ypix = self.size[0], self.size[1]
        pic = [
            [
                noise([y / xpix, x / ypix])
                for x in range(0, (xpix + 1) * PIXEL_SIZE, PIXEL_SIZE)
            ]
            for y in range(0, (ypix + 1) * PIXEL_SIZE, PIXEL_SIZE)
        ]

        sprites = Tileset(
            f"assets/Terrain/Water/Rocks/Rocks_0{random.choice([1, 2])}.png",
            (128, 128),
        ).tiles
        animation = Animation(
            {"water_rock": list(sprites.values())}, auto_set_status=True
        )

        print("drawing")
        for y, row in enumerate(pic):
            for x, column in enumerate(row):
                x_pixel_size = x * PIXEL_SIZE
                y_pixel_size = y * PIXEL_SIZE
                if column >= 0.002:
                    # BaseSprite(
                    #     (x_pixel_size, y_pixel_size),
                    #     self.terrain_tiles.tiles[1, 1],
                    #     Layers.MAIN,
                    #     group=group,
                    # )

                    self.surface_layer.blit(
                        self.terrain_tiles.tiles[1, 1],
                        (x_pixel_size, y_pixel_size),
                    )

                    self.map_cache[x_pixel_size, y_pixel_size] = [
                        AssetIdentifier.TERRAIN_FLAT
                    ]
                elif column >= -0.06:
                    # BaseSprite(
                    #     (x_pixel_size, y_pixel_size),
                    #     self.terrain_tiles.tiles[11, 1],
                    #     Layers.MAIN,
                    #     group=group,
                    # )

                    self.surface_layer.blit(
                        self.terrain_tiles.tiles[11, 1],
                        (x_pixel_size, y_pixel_size),
                    )

                    self.map_cache[x_pixel_size, y_pixel_size] = [
                        AssetIdentifier.TERRAIN_FLAT
                    ]
                elif column >= -0.1:
                    # BaseSprite(
                    #     (x_pixel_size, y_pixel_size),
                    #     self.water_tileset.tiles[0, 0],
                    #     Layers.WATER,
                    #     group=group,
                    # )

                    # self.surface_layer.blit(
                    #     self.water_tileset.tiles[0, 0],
                    #     (x_pixel_size, y_pixel_size),
                    # )

                    self.map_cache[x_pixel_size, y_pixel_size] = [
                        AssetIdentifier.WATER
                    ]

                    if random.random() < 0.3:
                        AnimatedSprite(
                            (x_pixel_size, y_pixel_size),
                            Layers.WATER_ROCKS,
                            group=group,
                            animation=animation,
                        )
                        self.map_cache[x_pixel_size, y_pixel_size].append(
                            AssetIdentifier.ROCKS
                        )

                else:
                    # self.surface_layer.blit(
                    #     self.water_tileset.tiles[0, 0],
                    #     (x_pixel_size, y_pixel_size),
                    # )

                    # BaseSprite(
                    #     (x_pixel_size, y_pixel_size),
                    #     self.water_tileset.tiles[0, 0],
                    #     Layers.WATER,
                    #     group=group,
                    # )
                    self.map_cache[x_pixel_size, y_pixel_size] = [
                        AssetIdentifier.WATER
                    ]

                    if random.random() < 0.2:
                        # sprites = Tileset(
                        #     f"assets/Terrain/Water/Rocks/Rocks_0{random.choice([3, 4])}.png"
                        # ).tiles
                        # animation = Animation(
                        #     {"water_rock": list(sprites.values())}, auto_set_status=True
                        # )
                        AnimatedSprite(
                            (x_pixel_size, y_pixel_size),
                            Layers.WATER_ROCKS,
                            group=group,
                            animation=animation,
                        )
                        self.map_cache[x_pixel_size, y_pixel_size].append(
                            AssetIdentifier.ROCKS
                        )

        print("Done")
        BaseSprite((0, 0), self.surface_layer, Layers.MAIN, group)
        # print("land")
        # tree_noise = PerlinNoise(octaves=1, seed=random() * 100)  # Trees
        # tree_xpix, tree_ypix = self.size[0], self.size[1]
        # tree_pic = [
        #     [
        #         tree_noise([y / tree_xpix, x / tree_ypix])
        #         for x in range(0, (tree_xpix + 1) * PIXEL_SIZE, PIXEL_SIZE)
        #     ]
        #     for y in range(0, (tree_ypix + 1) * PIXEL_SIZE, PIXEL_SIZE)
        # ]
        #
        # for y, tree_row in enumerate(tree_pic):
        #     for x, column in enumerate(tree_row):
        #         if column <= -0.1:
        #             if (
        #                 "water_0"
        #                 not in self.map_cache[x * PIXEL_SIZE, y * PIXEL_SIZE]
        #                 and "water_1"
        #                 not in self.map_cache[x * PIXEL_SIZE, y * PIXEL_SIZE]
        #             ):
        #                 if (
        #                     "sand_0"
        #                     in self.map_cache[x * PIXEL_SIZE, y * PIXEL_SIZE]
        #                 ):
        #                     self.map_cache[
        #                         x * PIXEL_SIZE, y * PIXEL_SIZE
        #                     ].append(f"coconut_{random.randint(0, 5)}")
        #                 else:
        #                     self.map_cache[
        #                         x * PIXEL_SIZE, y * PIXEL_SIZE
        #                     ].append(f"tree_{random.randint(0, 3)}")
        #
        # print("trees")
        #
        # rock_noise = PerlinNoise(octaves=1, seed=random() * 100)  # rocks
        # rock_xpix, rock_ypix = self.size[0], self.size[1]
        # rock_pic = [
        #     [
        #         rock_noise([y / rock_xpix, x / rock_ypix])
        #         for x in range(0, (rock_xpix + 1) * PIXEL_SIZE, PIXEL_SIZE)
        #     ]
        #     for y in range(0, (rock_ypix + 1) * PIXEL_SIZE, PIXEL_SIZE)
        # ]
        #
        # for y, rock_row in enumerate(rock_pic):
        #     for x, column in enumerate(rock_row):
        #         if column <= -0.1:
        #             image = self.map_cache[x * PIXEL_SIZE, y * PIXEL_SIZE]
        #             if (
        #                 "water_0" not in image
        #                 and "water_1" not in image
        #                 and "sand_0" not in image
        #                 and "tree_0" not in image
        #                 and "tree_1" not in image
        #                 and "tree_2" not in image
        #                 and "tree_3" not in image
        #             ):
        #                 if (
        #                     random() <= 0.33
        #                 ):  # 33% of deploying rock to a coordinate
        #                     self.map_cache[
        #                         x * PIXEL_SIZE, y * PIXEL_SIZE
        #                     ].append(f"rock_{random.randint(0, 5)}")
