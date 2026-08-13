import pygame
import math

# Initializes and returns all items needed for menu screen
def setup_menu_assets(WIDTH, HEIGHT, MID_X, MID_Y):
    # Setup assets
    assets = {}
    # Title Setup
    title_font = pygame.font.SysFont("showcardgothic", 200)
    assets['title_surface'] = title_font.render("Duvo Eins", True, (75, 0, 110))
    assets['title_rect'] = assets['title_surface'].get_rect(center=(MID_X, HEIGHT / 4))
    # START Button Setup
    assets['start_button_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 5 * 3 - 200, MID_X, 200)
    start_font = pygame.font.SysFont(None, 120)
    assets['start_surface'] = start_font.render("START", True, (0, 0, 0))
    assets['start_rect'] = assets['start_surface'].get_rect(center=(MID_X, HEIGHT / 5 * 3 - 90))
    # INFO Button Setup
    assets['info_button_rect'] = pygame.Rect(WIDTH / 8 * 3, HEIGHT / 5 * 3 + 100, WIDTH / 4, 100)
    info_font = pygame.font.SysFont(None, 60)
    assets['info_surface'] = info_font.render("INFO", True, (240, 240, 240))
    assets['info_rect'] = assets['info_surface'].get_rect(center=(MID_X, HEIGHT / 5 * 3 + 150))
    # SETTINGS Button Setup
    assets['settings_center'] = (WIDTH - 70, 70)
    assets['settings_radius'] = 40
    icon_font = pygame.font.SysFont("segoeuisymbol", 50)
    assets['settings_surface'] = icon_font.render("⚙", True, (240, 240, 240))
    if assets['settings_surface'].get_width() == 0:
        icon_font = pygame.font.SysFont(None, 30)
        assets['settings_surface'] = icon_font.render("SET", True, (255, 255, 255))
    assets['settings_rect'] = assets['settings_surface'].get_rect(center=assets['settings_center'])
    # Returns assets
    return assets

# Handles visuals for menu screen
def draw_menu(screen, assets):
    screen.fill((0, 132, 134))
    # Draws Title
    screen.blit(assets['title_surface'], assets['title_rect'])
    # Draws START Button
    pygame.draw.rect(screen, (240, 240, 240), assets['start_button_rect'])
    screen.blit(assets['start_surface'], assets['start_rect'])
    # Draws INFO Button
    pygame.draw.rect(screen, (0, 0, 0), assets['info_button_rect'])
    screen.blit(assets['info_surface'], assets['info_rect'])
    # Draws SETTINGS Button
    pygame.draw.circle(screen, (40, 40, 40), assets['settings_center'], assets['settings_radius'])
    pygame.draw.circle(screen, (25, 25, 25), assets['settings_center'], assets['settings_radius'], 3)
    screen.blit(assets['settings_surface'], assets['settings_rect'])
    # Update display
    pygame.display.flip()

# Processes player inputs at menu screen
def handle_menu_events(assets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                return "quit"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                if assets['start_button_rect'].collidepoint(mouse_pos):
                    return "selection1"
                elif assets['info_button_rect'].collidepoint(mouse_pos):
                    return "info"
                center_x, center_y = assets['settings_center']
                distance = math.hypot(mouse_pos[0] - center_x, mouse_pos[1] - center_y)
                if distance <= assets['settings_radius']:
                    return "settings"
    return "menu"