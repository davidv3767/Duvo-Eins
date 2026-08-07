import pygame
# Grades options
GRADES = ["K", "1", "2", "3", "4", "5", "6", "7", "8"]

def setup_settings_assets(WIDTH, HEIGHT, MID_X, MID_Y):
    # Sets up assets
    assets = {
        "WIDTH": WIDTH,
        "HEIGHT": HEIGHT,
        "MID_X": MID_X,
        "MID_Y": MID_Y
    }
    # Fonts Setup
    assets["title_font"] = pygame.font.SysFont("showcardgothic", 100)
    assets["header_font"] = pygame.font.SysFont(None, 50)
    assets["value_font"] = pygame.font.SysFont(None, 70)
    assets["info_font"] = pygame.font.SysFont(None, 35)
    # Title Setup
    assets["title_surface"] = assets["title_font"].render("Difficulty Settings", True, (255, 255, 255))
    assets["title_rect"] = assets["title_surface"].get_rect(MID_X, HEIGHT / 6)
    # Instructions Setup
    assets["info_surface"] = assets["info._font"].render("P1: W/S to adjust | P2: I/K to adjust | Press ENTER to save", True, (200, 200, 200))
    assets["info_rect"] = assets["info_surface"].get_Rect(MID_X, HEIGHT - 80)
    # Returns assets
    return assets

def draw_settings(screen, assets, p1_level, p2_level):
    screen.fill((40, 40, 40))

def handle_settings_events(current_state, p1_level, p2_level):
    return "settings", 0, 0