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
pipe_spawn_time = 0
score = 0
pipes = []
bird = Bird()

font_big = pygame.font.SysFont("couriernew", 48, bold=True)
font_small = pygame.font.SysFont("couriernew", 28, bold=True)

begin = True
pygame.time.set_timer(pygame.USEREVENT+1, 1000)
counter = 5
countdown_text = font_big.render(str(counter), True, 'white')

bg = pygame.image.load('bg_FB.png')

while running:
    clock.tick(45)
    screen.blit(bg, (0, 0))
    #screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.USEREVENT+1: #countdown
            counter -= 1
            if counter == 0:
                countdown_text = font_big.render('Start!', True, 'white')
            elif counter < 0:
                pygame.time.set_timer(pygame.USEREVENT+1, 0)
                begin = False
            else:
                countdown_text = font_big.render(str(counter), True, 'white')
        elif event.type == pygame.KEYDOWN: #reset
            if event.key == pygame.K_RETURN:
                is_end = False
                score = 0
                bird.__init__()
                pipes = []
    if begin:
        screen.blit(countdown_text, (230, 220))
    else:
        if is_end:
            game_over_text = font_big.render("Game Over", True, 'white', 'red')
            reset_text = font_small.render("Press Enter to restart", True, 'white', 'red')
            screen.blit(game_over_text, (120, 210))
            screen.blit(reset_text, (70, 270))
            screen.blit(score_text, (170, 0))
        else:
            current_time = pygame.time.get_ticks()
            #update bird
            bird.update()
            #update score
            score_text = font_small.render("Score: " + str(score), True, 'white', 'red')
            screen.blit(score_text, (170, 0))

            if current_time > (pipe_spawn_time + random.randint(1000, 8000)):
                pipes.append(Pipe())
                pipe_spawn_time = current_time

            for pipe in pipes:
                pipe.update()
                if pipe.x < -20:
                    pipes.remove(pipe)
                # consider collisions
                if (bird.y + 10 >= pipe.height + pipe.space or bird.y - 10 <= pipe.height) \
                        and (bird.x + 10 >= pipe.x and bird.x - 10 <= pipe.x + 20):
                    is_end = True
                    break
                # calculate score
                if bird.x - 10 >= pipe.x and bird.x + 10 <= pipe.x + 20:
                    score += 1

    pygame.display.flip()

pygame.quit()