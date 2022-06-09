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

class Pipe:
    def __init__(self):
        self.height = random.randint(50, 250)
        self.space = random.randint(50, 200) #space between 2 pipes
        self.x = 500
        self.y = 0
        #draw pipe
        pygame.draw.rect(screen, 'green', (self.x, self.y, 20, self.height))
        #draw revert pipe
        pygame.draw.rect(screen, 'green', (self.x, self.height + self.space, 20, 500 - self.height - self.space))

    def update(self):
        self.x -= 2
        pygame.draw.rect(screen, 'green', (self.x, self.y, 20, self.height))
        pygame.draw.rect(screen, 'green', (self.x, self.height + self.space, 20, 500 - self.height - self.space))

running = True
is_end = False
clock = pygame.time.Clock()
bird = Bird()
pipe_spawn_time = 0
pipes = []

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
        #get time
        current_time = pygame.time.get_ticks()
        if current_time > (pipe_spawn_time + random.randint(1000, 8000)):
            pipes.append(Pipe())
            pipe_spawn_time = current_time

        for pipe in pipes:
            pipe.update()
            if pipe.x < -20:
                pipes.remove(pipe)

    pygame.display.flip()

pygame.quit()