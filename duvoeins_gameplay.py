# Needed imports
import pygame
import random
import json

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
def setup_gameplay_assets(WIDTH, HEIGHT, MID_X, MID_Y):
    # Setup assets
    assets = {}
    assets["current_level"] = 1
    # Import questions
    
    # Function to pick questions
    def get_new_question(level):
        lvl_str = str(level)
        if lvl_str not in assets["level_questions"]:
            lvl_str = 1
            return random.choice(assets["level_questions"][lvl_str])
    # Returns assets
    return assets

# Handles gameplay visuals
def draw_gameplay(screen, assets):
    screen.fill((51, 51, 51))
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