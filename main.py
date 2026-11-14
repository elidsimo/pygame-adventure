import pygame
from constants  import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event




def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt= 0.0
    
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids =pygame.sprite.Group()
    
    
    #containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable )
    AsteroidField.containers = (updatable)
    
    #create objects
     
    player=Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    asteroid_field = AsteroidField()
    
    
    while True :
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
    
if __name__ == "__main__":
    main()
