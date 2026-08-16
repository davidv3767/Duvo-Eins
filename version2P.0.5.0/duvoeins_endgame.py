import pygame

def setup_endgame_assets(WIDTH, HEIGHT, MID_X, MID_Y, gameplay_assets):
    # Setup assets
    assets = {
        "WIDTH": WIDTH,
        "HEIGHT": HEIGHT,
        "MID_X": MID_X,
        "MID_Y": MID_Y
    }
    # Extract stats from gameplay_assets
    winner = gameplay_assets.get("winner_name", "Unknown Winner")
    p1_name = gameplay_assets.get("p1_name", "Player 1")
    p2_name = gameplay_assets.get("p2_name", "Player 2")
    p1_total = gameplay_assets.get("p1_total_questions", 0)
    p1_correct = gameplay_assets.get("p1_correct_questions", 0)
    p2_total = gameplay_assets.get("p2_total_questions", 0)
    p2_correct = gameplay_assets.get("p2_correct_questions", 0)
    # Fonts
    title_font = pygame.font.SysFont("showcardgothic", 100)
    header_font = pygame.font.SysFont(None, 60)
    stat_font = pygame.font.SysFont(None, 45)
    info_font = pygame.font.SysFont(None, 35)
    # Render winner
    assets["title_surface"] = title_font.render(f"{winner} Wins!", True, (255, 215, 0))
    assets["title_rect"] = assets["title_surface"].get_rect(center=(MID_X, HEIGHT / 6))
    # Render instructions
    assets["info_surface"] = info_font.render(f"Press ESC to Quit | Any Other Key for Menu", True, (255, 215, 0))
    assets["info_rect"] = assets["info_surface"].get_rect(center=(MID_X, HEIGHT - 50))
    # Render stats for Player 1
    assets["p1_header"] = header_font.render(f"{p1_name}'s Stats", True, (255, 255, 255))
    assets["p1_header_rect"] = assets["p1_header"].get_rect(center=(WIDTH / 4, MID_Y - 80))
    p1_accuracy = (p1_correct / p1_total * 100) if p1_total > 0 else 0
    assets["p1_stats_lines"] = [
        stat_font.render(f"Questions Attempted: {p1_total}", True, (220, 220, 220)),
        stat_font.render(f"Questions Correct: {p1_correct}", True, (220, 220, 220)),
        stat_font.render(f"Accuracy: {p1_accuracy:.1f}%", True, (220, 220, 220))
    ]
    # Render stats for Player 2
    assets["p2_header"] = header_font.render(f"{p2_name}'s Stats", True, (255, 255, 255))
    assets["p2_header_rect"] = assets["p2_header"].get_rect(center=(WIDTH / 4 * 3, MID_Y - 80))
    p2_accuracy = (p2_correct / p2_total * 100) if p2_total > 0 else 0
    assets["p2_stats_lines"] = [
        stat_font.render(f"Questions Attempted: {p2_total}", True, (220, 220, 220)),
        stat_font.render(f"Questions Correct: {p2_correct}", True, (220, 220, 220)),
        stat_font.render(f"Accuracy: {p2_accuracy:.1f}%", True, (220, 220, 220))
    ]
    # Returns assets
    return assets

def draw_endgame(screen, assets):
    # Renders screen to display
    screen.fill((30, 30, 30))
    # Title & Instructions
    screen.blit(assets["title_surface"], assets["title_rect"])
    screen.blit(assets["info_surface"], assets["info_rect"])
    # Player 1 Stats
    screen.blit(assets["p1_header"], assets["p1_header_rect"])
    for index, surface in enumerate(assets["p1_stats_lines"]):
        rect = surface.get_rect(center=(assets["WIDTH"] / 4, assets["MID_Y"] + (index * 45)))
        screen.blit(surface, rect)
    # Player 2 Stats
    screen.blit(assets["p2_header"], assets["p2_header_rect"])
    for index, surface in enumerate(assets["p2_stats_lines"]):
        rect = surface.get_rect(center=(assets["WIDTH"] / 4 * 3, assets["MID_Y"] + (index * 45)))
        screen.blit(surface, rect)
    pygame.display.flip()  

def handle_endgame_events():
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return "quit"
        elif event.type == pygame.KEYDOWN:   
            # Also quits game
            if event.key == pygame.K_ESCAPE:
                return "quit"
            # Returns to menu screen
            else:
                return "menu"
