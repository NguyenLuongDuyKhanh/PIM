import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Flappy Bird')

class Bird:
    def __init__(self):
        self.x = 200
        self.y = 200
        pygame.draw.circle(screen, 'red', (self.x, self.y), 10)

    def update(self):
        global is_end
        if self.y >= 490:
            is_end = True
        elif self.y <= 10:
            self.y += 3
        else:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_SPACE]:
                self.y -= 3
            else:
                self.y += 2
        pygame.draw.circle(screen, 'red', (self.x, self.y), 10)


running = True
is_end = False
clock = pygame.time.Clock()
bird = Bird()

while running:
    clock.tick(45)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
    if is_end:
        break
    else:
        #update bird
        bird.update()

    pygame.display.flip()

pygame.quit()