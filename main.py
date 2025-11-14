import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
pygame.init()

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()
        ## below checks if user has closed the window
        game_events = pygame.event.get()
        for event in game_events:
            if event.type == pygame.QUIT:
                return 
        print(game_events)
        screen.fill(color="black")
        pygame.display.flip()



if __name__ == "__main__":
    main()
