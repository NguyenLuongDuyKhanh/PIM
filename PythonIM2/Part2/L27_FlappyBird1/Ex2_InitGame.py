# 1. Cài đặt Pygame.
# 2. Nhập thư viện và khởi tạo pygame.
import pygame
pygame.init()

# 3. Đặt tên và kích thước cho cửa sổ.
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Hello world!')

# 4. Tạo vòng lặp cho game để hiển thị cửa sổ.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# 5. Thoát khỏi Pygame khi đã hoàn tất.
pygame.quit()