import pygame
import sys

# Import our custom modular state screens
import duvoeins_menu
import duvoeins_info
import duvoeins_selection

# Global constants (Populated dynamically during runtime)
WIDTH, HEIGHT = 0, 0
MID_X, MID_Y = 0, 0

def init_game():
    global WIDTH, HEIGHT, MID_X, MID_Y
    pygame.init()
    pygame.font.init()
    
    info_obj = pygame.display.Info()
    WIDTH, HEIGHT = info_obj.current_w, info_obj.current_h
    MID_X, MID_Y = WIDTH / 2, HEIGHT / 2
    
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("Duvo Eins")
    return screen

def main():
    screen = init_game()
    
    # Setup state assets using calculated resolution mappings
    menu_assets = duvoeins_menu.setup_menu_assets(WIDTH, HEIGHT, MID_X)
    info_assets = duvoeins_info.setup_info_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    selection1_assets = duvoeins_selection.setup_selection1_assets(WIDTH, HEIGHT, MID_X)
    selection2_assets = duvoeins_selection.setup_selection2_assets(WIDTH, HEIGHT, MID_X, MID_Y)
    
    clock = pygame.time.Clock()
    current_state = "menu"
    
    # Selection text state trackers
    p1_name = ""
    p2_name = ""
    active_box = "p1"
    
    # Core Central Game Loop
    while current_state != "quit":
        if current_state == "menu":
            duvoeins_menu.draw_menu(screen, menu_assets)
            current_state = duvoeins_menu.handle_menu_events(menu_assets)
            
        elif current_state == "info":
            duvoeins_info.draw_info(screen, info_assets)
            current_state = duvoeins_info.handle_info_events()
            
        elif current_state == "selection1":
            duvoeins_selection.draw_selection1(screen, selection1_assets, p1_name, p2_name, active_box)
            current_state, p1_name, p2_name, active_box = duvoeins_selection.handle_selection1_events(p1_name, p2_name, active_box)
            
        elif current_state == "selection2":
            duvoeins_selection.draw_selection2(screen, selection2_assets)
            current_state = duvoeins_selection.handle_selection2_events()
            
        clock.tick(60)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()