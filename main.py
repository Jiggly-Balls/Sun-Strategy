import pygame
from game_state import StateManager

from core.config import SCREEN_HEIGHT, SCREEN_WIDTH


def main() -> None:
    pygame.init()
    pygame.display.init()
    pygame.display.set_caption("Procedural World Generation")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    manager = StateManager(screen)
    manager.connect_state_hook("states.game")
    manager.change_state("Game")

    clock = pygame.time.Clock()

    while manager.is_running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            manager.current_state.process_event(event)

        manager.current_state.process_update(dt)


if __name__ == "__main__":
    main()
