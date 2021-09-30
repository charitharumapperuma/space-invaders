import pygame

# Initialize game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Set game title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
