# Needed imports
import pygame
import sys
# Global constants
WIDTH, HEIGHT = 0, 0

# Initializes pygame, settings, and returns screen
def init_game():
    # Pygame initialization
    global WIDTH, HEIGHT
    pygame.init()
    pygame.font.init()
    # Window size + display surface
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Duvo Eins")
    # Returns screen
    return screen

# Initializes and returns all items needed for menus creen
def setup_menu_assets():
    # Sets up assets
    assets = {}
    # Title Setup
    title_font = pygame.font.SysFont("showcardgothic", 200)
    assets['title_surface'] = title_font.render("Duvo Eins", True, (75, 0, 110))
    assets['title_rect'] = assets['title_surface'].get_rect(center=(WIDTH / 2, HEIGHT / 4))
    # START Button Setup
    assets['start_button_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 5 * 3 - 200, WIDTH / 2, 200)
    start_font = pygame.font.SysFont(None, 120)
    assets['start_surface'] = start_font.render("START", True, (0, 0, 0))
    assets['start_rect'] = assets['start_surface'].get_rect(center=(WIDTH / 2, HEIGHT / 5 * 3 - 90))
    # INFO Button Setup
    assets['info_button_rect'] = pygame.Rect(WIDTH / 8 * 3, HEIGHT / 5 * 3 + 100, WIDTH / 4, 100)
    info_font = pygame.font.SysFont(None, 60)
    assets['info_surface'] = info_font.render("INFO", True, (240, 240, 240))
    assets['info_rect'] = assets['info_surface'].get_rect(center=(WIDTH / 2, HEIGHT / 5 * 3 + 150))
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
    # Update display
    pygame.display.flip()

# Processes player inputs & contains game loop
def handle_events(assets):
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return False
        # Also guits game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                # Buttons on menu screen
                if assets['start_button_rect'].collidepoint(mouse_pos):
                    print("THIS WORKS")
                elif assets['info_button_rect'].collidepoint(mouse_pos):
                    print("THIS ALSO WORKS")
                    
    return True

# Main execution function
def main():
    # Runs other functions
    screen = init_game()
    assets = setup_menu_assets()
    clock = pygame.time.Clock()
    
    current_state = "menu"
    running = True
    
    while running:
        if current_state == "menu":
            draw_menu(screen, assets)
            running = handle_events(assets)
        
        clock.tick(60)

    # End mechanic
    pygame.quit()
    sys.exit()

main()