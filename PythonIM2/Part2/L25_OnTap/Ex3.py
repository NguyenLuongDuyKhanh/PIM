# Fill the screen with white
screen.fill((255, 255, 255))

# Create a surface and pass in a tuple containing its length and width
surf = pygame.Surface((50, 50))

# Give the surface a color to separate it from the background
surf.fill((0, 0, 0))
rect = surf.get_rect()