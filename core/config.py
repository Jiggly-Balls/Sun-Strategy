from enum import Enum, IntEnum, auto

TITLE: str = "Sun Strategy"
FPS: int = 60
PIXEL_SIZE: int = 32
SCREEN_WIDTH: int = 1366
SCREEN_HEIGHT: int = 768


class Layers(IntEnum):
    MAIN = 1
    GROUND = 2
    WATER = 3
    WATER_ROCKS = 4


class AssetIdentifier(Enum):
    TERRAIN_ELEVATION = auto()
    TERRAIN_FLAT = auto()
    WATER = auto()
    ROCKS = auto()
    FOAM = auto()
    TREES = auto
