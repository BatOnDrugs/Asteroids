# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()   
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,) 
    Shot.containers = (bullets, updatable, drawable)  
    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    while True:    
        pygame.Surface.fill(screen,(0,0,0))
        for item in updatable:
            item.update(dt)
        for item in asteroids:
            if item.collisions(player) == True:
                exit("Game over!")
        for bullet in bullets:
            for item in asteroids:
                if bullet.collisions(item) == True:
                    bullet.kill()
                    item.kill()


        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        clock.tick(60)
        dt = clock.get_time() / 1000
        
        
       
        

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()

