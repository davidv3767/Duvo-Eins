import pygame
import sys

# Import our custom modular state screens
import duvoeins_menu
import duvoeins_info
import duvoeins_selection
import duvoeins_gameplay

# Global constants (Populated dynamically during runtime)
WIDTH, HEIGHT = 0, 0
MID_X, MID_Y = 0, 0

# Initializes what's neccessary
def init_game():
    # Initialize variables + pygame
    global WIDTH, HEIGHT, MID_X, MID_Y
    pygame.init()
    pygame.font.init()
    # Assign values to global variables
    info_obj = pygame.display.Info()
    WIDTH, HEIGHT = info_obj.current_w, info_obj.current_h
    MID_X, MID_Y = WIDTH / 2, HEIGHT / 2
    # Create, name & return screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Duvo Eins")
    return screen

def main():
    # Setup clock & current state
    clock = pygame.time.Clock()
    current_state = "menu"
    # Selection trackers
    p1_name = ""
    p2_name = ""
    active_box = "p1"
    selection2_key_pressed = None
    p1_info = [p1_name, None, False]
    p2_info = [p2_name, None, False]
    # Input from other functions
    screen = init_game()
    menu_assets = duvoeins_menu.setup_menu_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    info_assets = duvoeins_info.setup_info_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    selection1_assets = duvoeins_selection.setup_selection1_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    selection2_assets = duvoeins_selection.setup_selection2_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    gameplay_assets = duvoeins_gameplay.setup_gameplay_assets(WIDTH, HEIGHT, MID_X, MID_Y, p1_info, p2_info)
    # Main game loop
    while current_state != "quit":
        if current_state == "menu":
            duvoeins_menu.draw_menu(screen, menu_assets)
            current_state = duvoeins_menu.handle_menu_events(menu_assets)
        # 2nd selection screen    
        elif current_state == "info":
            duvoeins_info.draw_info(screen, info_assets)
            current_state = duvoeins_info.handle_info_events()
        # 1st selection screen  
        elif current_state == "selection1":
            duvoeins_selection.draw_selection1(screen, selection1_assets, p1_name, p2_name, active_box)
            current_state, p1_name, p2_name, active_box = duvoeins_selection.handle_selection1_events(p1_name, p2_name, active_box)
        # 2nd selection screen
        elif current_state == "selection2":
            duvoeins_selection.draw_selection2(screen, selection2_assets)
            current_state, selection2_assets, selection2_key_pressed, p1_info, p2_info = duvoeins_selection.handle_selection2_events(selection2_assets, selection2_key_pressed, p1_info, p2_info)
        # Gameplay screen
        elif current_state == "gameplay":
            gameplay_assets = duvoeins_gameplay.setup_gameplay_assets(WIDTH, HEIGHT, MID_X, MID_Y, p1_info, p2_info)
            duvoeins_gameplay.draw_gameplay(screen, gameplay_assets)
            current_state = duvoeins_gameplay.handle_gameplay_events()
        # Limit tick rate to 60 fps
        clock.tick(60)
    # Ending mechanic
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()