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
    assets["title_rect"] = assets["title_surface"].get_rect(center=(MID_X, HEIGHT / 6))
    # Instructions Setup
    assets["info_surface"] = assets["info_font"].render("P1: W/S to adjust | P2: I/K to adjust", True, (200, 200, 200))
    assets["info_rect"] = assets["info_surface"].get_rect(center=(MID_X, HEIGHT - 80))
    # Returns assets
    return assets

def draw_settings(screen, assets, p1_level, p2_level):
    screen.fill((40, 40, 40))
    # Draw Title & Instructions
    screen.blit(assets["title_surface"], assets["title_rect"])
    screen.blit(assets["info_surface"], assets["info_rect"])
    # Player 1 Box
    p1box_header = assets["header_font"].render("Player 1 Level", True, (100, 200, 255))
    p1box_header_rect = p1box_header.get_rect(center=(assets["WIDTH"] / 4, assets["MID_Y"] - 60))
    p1box_val = assets["value_font"].render(f"Grade {p1_level}", True, (255, 255, 255))
    p1box_val_rect = p1box_val.get_rect(center=(assets["WIDTH"] / 4, assets["MID_Y"] + 20))
    screen.blit(p1box_header, p1box_header_rect)
    screen.blit(p1box_val, p1box_val_rect)
    # Player 2 Box
    p2box_header = assets["header_font"].render("Player 2 Level", True, (100, 200, 255))
    p2box_header_rect = p2box_header.get_rect(center=(assets["WIDTH"] / 4 * 3, assets["MID_Y"] - 60))
    p2box_val = assets["value_font"].render(f"Grade {p2_level}", True, (255, 255, 255))
    p2box_val_rect = p2box_val.get_rect(center=(assets["WIDTH"] / 4 * 3, assets["MID_Y"] + 20))
    screen.blit(p2box_header, p2box_header_rect)
    screen.blit(p2box_val, p2box_val_rect)
    # Needed command
    pygame.display.flip()
 
def handle_settings_events(p1_level, p2_level):
    # Player level index
    p1_index = GRADES.index(p1_level) if p1_level in GRADES else 0
    p2_index = GRADES.index(p2_level) if p2_level in GRADES else 0
    # For loop
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", p1_level, p2_level
            elif event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_ESCAPE:
                    return "quit", p1_level, p2_level
                elif event.key == pygame.K_TAB:
                    return "menu", p1_level, p2_level
                # Player 1 controls
                elif event.key == pygame.K_w: 
                    p1_index = min(p1_index + 1, len(GRADES) - 1)
                elif event.key == pygame.K_s: 
                    p1_index = max(p1_index - 1, 0)
                # Player 2 controls
                elif event.key == pygame.K_i: 
                    p2_index = min(p2_index + 1, len(GRADES) - 1)
                elif event.key == pygame.K_k: 
                    p2_index = max(p2_index - 1, 0)
    return "settings", GRADES[p1_index], GRADES[p2_index]
