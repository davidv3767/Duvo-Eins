import pygame
import sys

# Import our custom modular state screens
import duvoeins_menu
import duvoeins_settings
import duvoeins_info
import duvoeins_selection
import duvoeins_gameplay
import duvoeins_endgame

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
    # Selection variables & other trackers
    p1_level = "K"
    p2_level = "K"
    p1_name = ""
    p2_name = ""
    active_box = "p1"
    selection2_key_pressed = None
    p1_info = [p1_name, None, False]
    p2_info = [p2_name, None, False]
    # Input from other functions
    screen = init_game()
    menu_assets = duvoeins_menu.setup_menu_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    settings_assets = duvoeins_settings.setup_settings_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    info_assets = duvoeins_info.setup_info_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    selection1_assets = duvoeins_selection.setup_selection1_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    selection2_assets = duvoeins_selection.setup_selection2_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    gameplay_assets = duvoeins_gameplay.setup_gameplay_assets(WIDTH, HEIGHT, MID_X, MID_Y, p1_info, p2_info, p1_level, p2_level)
    # Main game loop
    while current_state != "quit":
        if current_state == "menu":
            duvoeins_menu.draw_menu(screen, menu_assets)
            current_state = duvoeins_menu.handle_menu_events(menu_assets)
        # Settings screen
        elif current_state == "settings":
            duvoeins_settings.draw_settings(screen, settings_assets, p1_level, p2_level)
            current_state, p1_level, p2_level = duvoeins_settings.handle_settings_events(p1_level, p2_level)
        # Info screen  
        elif current_state == "info":
            duvoeins_info.draw_info(screen, info_assets)
            current_state = duvoeins_info.handle_info_events()
        # 1st selection screen  
        elif current_state == "selection1":
            duvoeins_selection.draw_selection1(screen, selection1_assets, p1_name, p2_name, active_box)
            current_state, p1_name, p2_name, active_box = duvoeins_selection.handle_selection1_events(p1_name, p2_name, active_box)
        # 2nd selection screen
        elif current_state == "selection2":
            p1_info[0] = p1_name
            p2_info[0] = p2_name
            duvoeins_selection.draw_selection2(screen, selection2_assets)
            current_state, selection2_assets, selection2_key_pressed, p1_info, p2_info = duvoeins_selection.handle_selection2_events(selection2_assets, selection2_key_pressed, p1_info, p2_info)
        # Gameplay screen
        elif current_state == "gameplay":
            if gameplay_assets["second_datasync_done"] == False: 
                gameplay_assets = duvoeins_gameplay.setup_gameplay_assets(WIDTH, HEIGHT, MID_X, MID_Y, p1_info, p2_info, p1_level, p2_level)
            duvoeins_gameplay.draw_gameplay(screen, gameplay_assets, WIDTH, HEIGHT)
            current_state, gameplay_assets = duvoeins_gameplay.handle_gameplay_events(gameplay_assets)
        elif current_state == "endgame":
            print("Welcome to the endgame... which is an endgame!")
        # Limit tick rate to 60 fps
        clock.tick(60)
    # Ending mechanic
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()