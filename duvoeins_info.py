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
    assets['version_surface'] = version_font.render("Version: 0.3.3", True, (255, 255, 255))
    assets['version_rect'] = assets['version_surface'].get_rect(center=(WIDTH / 4, MID_Y))
    maindev_font = pygame.font.SysFont(None, 75)
    assets['maindev_surface'] = maindev_font.render("Made by David Vuddandam ", True, (255, 255, 255))
    assets['maindev_rect'] = assets['maindev_surface'].get_rect(center=(WIDTH / 4, HEIGHT / 8 * 5))
    # Instruction Title Setup
    instrtitle_font = pygame.font.SysFont(None, 100)
    assets['instrtitle_surface'] = instrtitle_font.render("Instructions", True, (255, 255, 255))
    assets['instrtitle_rect'] = assets['instrtitle_surface'].get_rect(center=(WIDTH / 4 * 3, HEIGHT / 2 - 50))
    # Instructions Setup
    instructions_list = [
        "1. Enter names on Selection Screen 1.",
        "2. Triple-tap 1-4 to pick a player.",
        "3. Answer math questions by typing 1-4 (p1) or 7-0 (p2) to attack.",
        "4. Press TAB to go back / ESC to quit"
    ]
    instr_font = pygame.font.SysFont(None, 40)
    assets['instr_rendered_lines'] = []
    for index, line in enumerate(instructions_list):
        line_surface = instr_font.render(line, True, (255, 255, 255))
        line_rect = line_surface.get_rect(center=(WIDTH / 4 * 3, HEIGHT / 2 + 30 + (50 * index)))
        assets['instr_rendered_lines'].append((line_surface, line_rect))
    # Returns assets    
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
    for surface, rect in assets['instr_rendered_lines']:
        screen.blit(surface, rect)
    pygame.display.flip()

# Processes player inputs at info screen
def handle_info_events():
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return "quit"
        elif event.type == pygame.KEYDOWN:
            # Also quits game
            if event.key == pygame.K_ESCAPE:
                return "quit"
            # Returns to menu screen
            elif event.key == pygame.K_TAB:
                return "menu"
    return "info"