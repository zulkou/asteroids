import pygame
from constants import *
import player

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

    player.Player.containers = (updateable, drawable)
    mc = player.Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for updt in updateable:
            updt.update(dt)
        for drw in drawable:
            drw.draw(screen)

        pygame.display.flip()
        fps.tick(60)
        dt = fps.tick(60) / 1000
        
if __name__ == "__main__":
    main()
