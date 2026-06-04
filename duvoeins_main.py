# This is the MAIN file for the Duvo Eins program

# Needed imports
import pygame
import sys
# Global constants
WIDTH, HEIGHT = 0, 0

# Initializes pygame, setting s, and returns screen
def init_game():
    # Pygame initialization
    global WIDTH, HEIGHT
    pygame.init()
    pygame.font.init()
    # Window size + display surface
    info = pygame.display.Info()
    WIDTH, HEIGHT = info.current_w, info.current_h
    screen = pygame.display.set_mode((WIDTH - 100, HEIGHT - 100))
    pygame.display.set_caption("Duvo Eins")
    # Returns screen
    return screen

# Initializes and returns all items needed for menu screen
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

# Processes player inputs at menu screen
def handle_menu_events(assets):
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return "quit"
        elif event.type == pygame.KEYDOWN:  
            # Also quits game
            if event.key == pygame.K_ESCAPE:
                return "quit"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                mouse_pos = event.pos
                # Buttons on menu screen
                if assets['start_button_rect'].collidepoint(mouse_pos):
                    return "selection1"
                elif assets['info_button_rect'].collidepoint(mouse_pos):
                    return "info"
    # If nothing is returned, stay on menu page               
    return "menu"

# Initializes and returns all items needed for menu screen
def setup_info_assets():
    # Sets up assets
    assets = {}
    # Title Setup
    title_font = pygame.font.SysFont("showcardgothic", 150)
    assets['title_surface'] = title_font.render("Information", True, (255, 255, 255))
    assets['title_rect'] = assets['title_surface'].get_rect(center=(WIDTH / 2, HEIGHT / 4))
    # Version & Credits Setup
    version_font = pygame.font.SysFont(None, 75)
    assets['version_surface'] = version_font.render("Version: 0.1.1", True, (255, 255, 255))
    assets['version_rect'] = assets['version_surface'].get_rect(center=(WIDTH / 4, HEIGHT / 2))
    maindev_font = pygame.font.SysFont(None, 75)
    assets['maindev_surface'] = maindev_font.render("Made by David Vuddandam", True, (255, 255, 255))
    assets['maindev_rect'] = assets['maindev_surface'].get_rect(center=(WIDTH / 4, HEIGHT / 8 * 5))
    # Instructions Setup
    instrtitle_font = pygame.font.SysFont(None, 125)
    assets['instrtitle_surface'] = instrtitle_font.render("Instructions", True, (255, 255, 255))
    assets['instrtitle_rect'] = assets['instrtitle_surface'].get_rect(center=(WIDTH / 4 * 3, HEIGHT / 7 * 3))
    instructions_font = pygame.font.SysFont(None, 50)
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
            # Returns to menu page
            elif event.key == pygame.K_TAB:
                return "menu"
    # If nothing is returned, stay on info page               
    return "info"

# Initializes and returns all items needed for first selection screen
def setup_selection1_assets():
    # Set up assets
    assets = {}
    # Set up player name graphics
    assets['font'] = pygame.font.SysFont(None, 120)
    assets['p1_box_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 8 * 3 - 60, WIDTH / 2, 120)
    assets['p2_box_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 8 * 5 - 60, WIDTH / 2, 120)
    # Returns assets
    return assets

# Handles visuals for first selection screen
def draw_selection1(screen, assets, p1_name, p2_name, active_box):
    # Fill screen
    screen.fill((100, 100, 100))
    # Outline colors
    if active_box == "p1":
        p1_box_color = (255, 215, 0)
        p2_box_color = (100, 100, 100)
    elif active_box == "p2":
        p1_box_color = (100, 100, 100)
        p2_box_color = (255, 215, 0)
    else:
         p1_box_color = (100, 100, 100)
         p2_box_color = (100, 100, 100)
    # Draws visible input box
    pygame.draw.rect(screen, p1_box_color, assets['p1_box_rect'], 4)
    pygame.draw.rect(screen, p2_box_color, assets['p2_box_rect'], 4)
    # Create temporary string variables that include the cursor for the active box
    p1_display_text = f"P1 Name: {p1_name}"
    p2_display_text = f"P2 Name: {p2_name}"
    if active_box == "p1":
        p1_display_text += "|"
    else:
        p2_display_text += "|"

    # Render temporary display strings instead of raw variables:
    p1_surface = assets['font'].render(p1_display_text, True, (255, 255, 255))
    p1_rect = p1_surface.get_rect(center=assets['p1_box_rect'].center)
    
    p2_surface = assets['font'].render(p2_display_text, True, (255, 255, 255))
    p2_rect = p2_surface.get_rect(center=assets['p2_box_rect'].center)

    # Draws elemnts
    screen.blit(p1_surface, p1_rect)
    screen.blit(p2_surface, p2_rect)
    pygame.display.flip()

# Processes player inputs at info screen
def handle_selection1_events(p1_name, p2_name, active_box):
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return "quit", p1_name, p2_name, "p1"
        elif event.type == pygame.KEYDOWN:
            # Also quits game
            if event.key == pygame.K_ESCAPE:
                return "quit", p1_name, p2_name, "p1"
            elif event.key == pygame.K_TAB:
                if active_box == "p2":
                    active_box = "p1"
                else:
                    return "menu", p1_name, p2_name, "p1"
            elif event.key == pygame.K_BACKSPACE:
                if active_box == "p1":
                    p1_name = p1_name[:-1]
                else:
                    p2_name = p2_name[:-1]
            elif event.key == pygame.K_RETURN:
                if active_box == "p1":
                    active_box = "p2"
                else:
                    return "selection2", p1_name, p2_name, "p2"
            else:
                if event.unicode.isprintable() and len(event.unicode) > 0:
                    if active_box == "p1" and len(p1_name) < 15:
                        p1_name += event.unicode
                    elif active_box == "p2" and len(p2_name) < 15:
                        p2_name += event.unicode
    # If nothing is returned, stay on first selection page               
    return "selection1", p1_name, p2_name, active_box

# Defines Line class
class Line:
    def __init__(self, start, end, color, width=1):
        self.start = start
        self.end = end
        self.color = color
        self.width = width

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.start, self.end, self.width)

# Initializes and returns all items needed for second selection screen
def setup_selection2_assets():
    print("Coming soon!")

# Main execution function
def main():
    # Runs setup functions
    screen = init_game()
    menu_assets = setup_menu_assets()
    info_assets = setup_info_assets()
    selection1_assets = setup_selection1_assets()
    clock = pygame.time.Clock()
    # Current state
    current_state = "menu"
    # Player names
    p1_name = ""
    p2_name = ""
    active_box = "p1"
    # Main game loop
    while current_state != "quit":
        if current_state == "menu":
            draw_menu(screen, menu_assets)
            current_state = handle_menu_events(menu_assets)
        elif current_state == "info":
            draw_info(screen, info_assets)
            current_state = handle_info_events()
        elif current_state == "selection1":
            draw_selection1(screen, selection1_assets, p1_name, p2_name, active_box)
            current_state, p1_name, p2_name, active_box = handle_selection1_events(p1_name, p2_name, active_box)
        clock.tick(60)
    # End mechanic
    pygame.quit()
    sys.exit()

main()