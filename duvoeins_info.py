import pygame

# Initializes and returns all items needed for menu screen
def setup_info_assets(WIDTH, HEIGHT, MID_X, MID_Y):
    assets = {}
    
    # Title Setup
    title_font = pygame.font.SysFont("showcardgothic", 150)
    assets['title_surface'] = title_font.render("Information", True, (255, 255, 255))
    assets['title_rect'] = assets['title_surface'].get_rect(center=(MID_X, HEIGHT / 4))
    
    # Version & Credits Setup
    version_font = pygame.font.SysFont(None, 75)
    assets['version_surface'] = version_font.render("Version: 0.1.3", True, (255, 255, 255))
    assets['version_rect'] = assets['version_surface'].get_rect(center=(WIDTH / 4, MID_Y))
    
    maindev_font = pygame.font.SysFont(None, 75)
    assets['maindev_surface'] = maindev_font.render("Made by David Vuddandam ", True, (255, 255, 255))
    assets['maindev_rect'] = assets['maindev_surface'].get_rect(center=(WIDTH / 4, HEIGHT / 8 * 5))
    
    # Instructions Setup
    instrtitle_font = pygame.font.SysFont(None, 125)
    assets['instrtitle_surface'] = instrtitle_font.render("Instructions", True, (255, 255, 255))
    assets['instrtitle_rect'] = assets['instrtitle_surface'].get_rect(center=(WIDTH / 4 * 3, HEIGHT / 7 * 3))
    
    return assets

# Handles visuals for info screen
def draw_info(screen, assets):
    screen.fill((40, 40, 40))
    # Draws Title
    screen.blit(assets['title_surface'], assets['title_rect'])
    # Draws Version & Credits Info
    screen.blit(assets['version_surface'], assets['version_rect'])
    screen.blit(assets['maindev_surface'], assets['maindev_rect'])
    # Draws Instructions
    screen.blit(assets['instrtitle_surface'], assets['instrtitle_rect'])
    pygame.display.flip()

# Processes player inputs at info screen
def handle_info_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "quit"
            elif event.key == pygame.K_TAB:
                return "menu"
    return "info"