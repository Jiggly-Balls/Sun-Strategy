import pygame
from game_state import StateManager

from core.config import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE
from core.tileset import Tileset
from entities.camera import Camera
from entities.map_plot import MapPlot

__version__ = "1.0.0"


def main() -> None:
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption(f"{TITLE} v{__version__}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    manager = StateManager(screen)
    manager.connect_state_hook("states.game")
    manager.change_state("Game")

    clock = pygame.time.Clock()
    manager.camera = Camera(screen)
    manager.terrain_tileset = Tileset("assets/Terrain/Ground/Flat.png")
    manager.water_tileset = Tileset("assets/Terrain/Water/Water.png")
    map_plotter = MapPlot(
        (500, 500),
        manager.terrain_tileset,
        ...,
        manager.water_tileset,
        ...,
        ...,
    )
    map_plotter.create_map(manager.camera)

    x = y = 0
    speed = 500

    while manager.is_running:
        screen.fill("white")
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            manager.current_state.process_event(event)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            y -= speed * dt

        if keys[pygame.K_s]:
            y += speed * dt

        if keys[pygame.K_a]:
            x -= speed * dt

        if keys[pygame.K_d]:
            x += speed * dt

        manager.camera.update(dt)
        manager.camera.draw(x, y)
        manager.current_state.process_update(dt)


if __name__ == "__main__":
    main()
