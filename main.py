import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    fps = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    mc = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    astfil = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for astd in asteroids:
            if mc.check_col(astd) is True:
                print("Game Over!")
                sys.exit()
        for sht in shots:
            for astd in asteroids:
                if astd.check_col(sht):
                    astd.split()
                    sht.kill()
        for updt in updateable:
            updt.update(dt)
        for drw in drawable:
            drw.draw(screen)
            

        pygame.display.flip()
        fps.tick(60)
        dt = fps.tick(60) / 1000
        
if __name__ == "__main__":
    main()
