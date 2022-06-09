import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
"""
    pygame.draw.rect(surface, color, rect, width)
    ➔  surface: surface ở trong Pygame tương tự với frame ở Tkinter, tức là một
        khung dùng để chứa các đối tượng. Cửa sổ ta tạo cũng gọi là một surface.
    ➔  color: tô màu cho hình vẽ. Có hai cách thể hiện màu là dạng chuỗi (tên màu
        bằng tiếng Anh) hoặc dạng tuple (hệ màu RGB)
    ➔  rect: vị trí và độ dài của hình chữ nhật, được thể hiện bằng tuple có 4 thông
        số sau: (<toạ độ x>, <toạ độ y>, <chiều dài>, <chiều rộng>)
        Trong đó, toạ độ x, y nằm ở góc trên bên trái của hình chữ nhật.
    ➔  width: độ dày của nét vẽ, và cũng là độ rộng để tô màu. Nếu ta bỏ trống
        tham số này thì sẽ tô màu toàn bộ hình.
"""
pygame.draw.rect(screen, 'red', (100,100,90,130),3)
"""
    Nhớ flip để update
"""
# pygame.display.flip()
# pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()