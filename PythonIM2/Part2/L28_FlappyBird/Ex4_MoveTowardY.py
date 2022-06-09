import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello world!')

# 1. Tạo biến khởi tạo toạ độ, hướng của hình tròn và đồng hồ.
running = True
move = 'down'
x = 200
y = 200
clock = pygame.time.Clock()

# 2. Viết hàm xử lí toạ độ y của hình tròn.
def checkPosition():
    global y, move
    if y >= 450 and move == 'down':
        move = 'up'
    elif y <= 50 and move == 'up':
        move = 'down'

    if move == 'up':
        y -= 1
    else:
        y += 1
# 3. Tạo vòng lặp game theo đúng quy trình.
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, 'red', (x, y), 50)
    checkPosition()
    print(y)

    pygame.display.flip()

pygame.quit()