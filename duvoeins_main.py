import pygame
import sys

def setup():
    pygame.init()
    pygame.font.init()
    # Window size + display surface
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Full Screen Pygame Window")
    # Initialize the Duvo Eins title
    title_font = pygame.font.SysFont("showcardgothic ", 120)
    title_surface = title_font.render("Duvo Eins", True, (75, 0, 110))
    title_rect = title_surface.get_rect()
    title_rect.center = (WIDTH / 2, HEIGHT / 5)
    # Clock object
    clock = pygame.time.Clock()
    # Main game loop flag
    running = True
    # Main game loop
    while running:
        screen.fill((0, 0, 0))
        screen.blit(title_surface, title_rect)
        # Update full display surface to screen
        pygame.display.flip()
        # Cap frame rate
        clock.tick(60)
        for event in pygame.event.get():
                # If X is hit
                if event.type == pygame.QUIT:
                    running = False
                # If escape key is hit
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
    # End mechanic
    pygame.quit()
    sys.exit()

setup()