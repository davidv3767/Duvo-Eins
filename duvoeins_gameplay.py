# Needed imports
import pygame
import random
import json

# Color dictionary
COLOR_DICTIONARY = {
    "red": (215, 25, 28),
    "yellow": (245, 210, 0),
    "green": (0, 130, 80),
    "blue": (15, 85, 215),
    "default": (255, 255, 255)
}

# Defines character class
class Character:
    def __init__(self, color, center, radius, playerName, playerNum):
        self.color = color
        self.center = center
        self.radius = radius
        self.name = playerName
        self.num = playerNum
        self.width = 0
        self.health = 100
        self.maxHealth = 100
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.width)

# Initializes and returns all items needed for gameplay
def setup_gameplay_assets(WIDTH, HEIGHT, MID_X, MID_Y, p1_info=None, p2_info=None):
    # Setup assets
    assets = {}
    assets["current_level"] = 1
    # Store dimensions for rendering
    assets["WIDTH"] = WIDTH
    assets["HEIGHT"] = HEIGHT
    assets["MID_X"] = MID_X
    assets["MID_Y"] = MID_Y
    # Setup player colors
    P1_COLOR_STR = p1_info[1] if p1_info and p1_info[1] else "default"
    P2_COLOR_STR = p2_info[1] if p2_info and p2_info[1] else "default"
    P1_COLOR = COLOR_DICTIONARY.get(P1_COLOR_STR)
    P2_COLOR = COLOR_DICTIONARY.get(P2_COLOR_STR)
    # Setup player names
    P1_NAME = p1_info[0] if p1_info and p1_info[0] else "Player 1"
    P2_NAME = p2_info[0] if p2_info and p2_info[0] else "Player 2"
    # Setup player characters
    player1 = Character(P1_COLOR, (200, HEIGHT - 220), 100, P1_NAME, 1)
    player2 = Character(P2_COLOR, (WIDTH - 200, HEIGHT - 220), 100, P2_NAME, 2)
    assets["p1"] = player1
    assets["p2"] = player2
    # Import questions
    try:
        with open("providedquestions.json", "r", encoding="utf-8") as file:
            assets["level_questions"] = json.load(file)
    except FileNotFoundError:
        print("Error: The file 'providedquestions.json' is not found.")
        assets["level_questions"] = {}
    # Function to pick questions
    def get_new_question(level):
        lvl_str = str(level)
        if lvl_str not in assets["level_questions"]:
            lvl_str = 1
        questions_list = assets["level_questions"].get(lvl_str, [])
        if questions_list:
            return random.choice(questions_list)
        return None
    # Returns assets
    return assets

# Handles gameplay visuals
def draw_gameplay(screen, assets):
    screen.fill((30, 30, 35))
    # Player zones
    pygame.draw.rect(screen, (70, 70, 75), (0, 0, assets["MID_X"], assets["HEIGHT"] - 120))
    pygame.draw.rect(screen, (15, 15, 20), (assets["MID_X"], 0, assets["MID_X"], assets["HEIGHT"] - 120))
    pygame.draw.line(screen, (100, 100, 110), (assets["MID_X"], 0), (assets["MID_X"], assets["HEIGHT"] - 120), 4)
    # Draw players
    if "p1" in assets:
        assets["p1"].draw(screen)
    if "p2" in assets:
        assets["p2"].draw(screen)
    pygame.display.flip()

# Processes player inputs during gameplay
def handle_gameplay_events():
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return "quit"
        elif event.type == pygame.KEYDOWN:   
            # Also quits game
            if event.key == pygame.K_ESCAPE:
                return "quit"
            # Returns to second selection screen
            elif event.key == pygame.K_TAB:
                return "selection2"
    # Return gameplay state by default
    return "gameplay"