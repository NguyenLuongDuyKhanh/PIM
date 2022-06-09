import pygame
pygame.init()
"""
    Thiết lập kích thước bằng 1 tuple of (width, height)
"""
screen = pygame.display.set_mode((500, 500))
"""
    title name
"""
pygame.display.set_caption("This is main screen")
"""
    Chọn màu và update màn hình
    Có thể thêm màu bằng tên màu hoặc tuple of three elements
"""
# screen.fill('green')
# screen.fill((0,0,255))
# pygame.display.flip()

"""
print(pygame.event.get())
[   <Event(4352-AudioDeviceAdded {'which': 0, 'iscapture': 0})>,
    <Event(4352-AudioDeviceAdded {'which': 1, 'iscapture': 0})>,
    <Event(4352-AudioDeviceAdded {'which': 0, 'iscapture': 1})>,
    <Event(32768-ActiveEvent {})>,
    <Event(32774-WindowShown {'window': None})>,
    <Event(32768-ActiveEvent {'gain': 1, 'state': 1})>,
    <Event(32785-WindowFocusGained {'window': None})>,
    <Event(770-TextEditing {'text': '', 'start': 0, 'length': 0, 'window': None})>,
    <Event(32770-VideoExpose {})>,
    <Event(32776-WindowExposed {'window': None})>
]
"""
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()