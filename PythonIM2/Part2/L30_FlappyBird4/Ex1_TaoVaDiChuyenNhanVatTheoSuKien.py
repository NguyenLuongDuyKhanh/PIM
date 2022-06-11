import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,0,255))
        self.rect = self.surf.get_rect()

player = Player()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Up")
                player.rect.move_ip(0, -5)
            elif event.key == pygame.K_DOWN:
                player.rect.move_ip(0, 5)
            elif event.key == pygame.K_LEFT:
                player.rect.move_ip(-5, 0)
            elif event.key == pygame.K_RIGHT:
                player.rect.move_ip(5, 0)
    screen.fill((0,0,0))
    screen.blit(player.surf, (player.rect))
    pygame.display.flip()

pygame.quit()