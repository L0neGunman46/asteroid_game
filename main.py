import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    dt = 0
    pygame.init()
    clock_obj= pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    

    while True:
        log_state()
        ## below checks if user has closed the window
        game_events = pygame.event.get()
        for event in game_events:
            if event.type == pygame.QUIT:
                return 
        screen.fill(color="black")
        # pauses the game loop until 1/60th a second has passed
        time = clock_obj.tick(60)
        # convert second to millisecond
        dt = time/1000
        updatable.update(dt)
        for asteroid in asteroids:
            if CircleShape.collides_with_self(player, asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()






if __name__ == "__main__":
    main()
