import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
"""
    pygame.draw.circle(surface, color, coordinates, radius, width)
    ➔ coordinates: toạ độ của tâm hình tròn, được thể hiện dưới dạng tuple
        (<toạ độ x>, <toạ độ y>)
    ➔ radius: bán kính hình tròn
"""
pygame.draw.circle(screen, 'red', (200, 200), 50, 3)
"""
    Nhớ flip để update
"""
pygame.display.flip()
# pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()