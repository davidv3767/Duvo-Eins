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

# Key maps
P1_KEY_MAP = {
    pygame.K_1: "1",
    pygame.K_2: "2",
    pygame.K_3: "3",
    pygame.K_4: "4"
}
P2_KEY_MAP = {
    pygame.K_7: "1",
    pygame.K_8: "2",
    pygame.K_9: "3",
    pygame.K_0: "4"
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
        self.font = pygame.font.SysFont(None, 36)
    def get_health_color(self):
        health_percent = max(0, min(1, self.health / self.maxHealth))
        if health_percent >= 0.5:
            red = int((1.0 - health_percent) * 2 * 255)
            green = 255
        else:
            red = 255
            green = int(health_percent * 2 * 255)
        return (red, green, 0)
    def draw(self, surface, WIDTH, HEIGHT):
        # Create character
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.width)
        # Create name badge
        text_surface = self.font.render(self.name, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.center[0], self.center[1] - self.radius - 30))
        background_rect = text_rect.inflate(20, 10)
        pygame.draw.rect(surface, (200, 200, 200), background_rect, 2, 6)
        surface.blit(text_surface, text_rect)
        # Create health bar
        max_bar_width = (WIDTH / 2) - 100
        current_bar_width = max(0, max_bar_width * (self.health / self.maxHealth))
        dynamic_color = self.get_health_color()
        if self.num == 1:
            bg_rect = pygame.Rect(50, HEIGHT - 90, max_bar_width, 40)
            fill_rect = pygame.Rect(50, HEIGHT - 90, current_bar_width, 40)
        else:
            bg_rect = pygame.Rect((WIDTH / 2) + 50, HEIGHT - 90, max_bar_width, 40)
            fill_rect = pygame.Rect((WIDTH / 2) + 50, HEIGHT - 90, current_bar_width, 40)
        pygame.draw.rect(surface, dynamic_color, fill_rect)
        pygame.draw.rect(surface, (255, 255, 255), bg_rect, 3)

# Initializes and returns all items needed for gameplay
def setup_gameplay_assets(WIDTH, HEIGHT, MID_X, MID_Y, p1_info=None, p2_info=None, p1_level="K", p2_level="K"):
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
    assets["p1_level"] = p1_level
    assets["p2_level"] = p2_level
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
            lvl_str = "K"
        questions_list = assets["level_questions"].get(lvl_str, [])
        if questions_list:
            return random.choice(questions_list)
        return None
    # Question storage
    assets["get_new_question"] = get_new_question
    assets["p1_question"] = get_new_question(p1_level)
    assets["p2_question"] = get_new_question(p2_level)
    assets["p1_total_questions"] = 0
    assets["p1_correct_questions"] = 0
    assets["p2_total_questions"] = 0
    assets["p2_correct_questions"] = 0
    # Second data sync tracker
    if P1_COLOR_STR == "default" or P2_COLOR_STR == "default":
        assets["second_datasync_done"] = False
    else:
        assets["second_datasync_done"] = True
    # Combat logic trackers
    assets["p1_shields"] = 0
    assets["p2_shields"] = 0
    assets["p1_phase"] = "answering"
    assets["p2_phase"] = "answering"
    # Returns assets
    return assets

# Handles gameplay visuals
def draw_gameplay(screen, assets, WIDTH, HEIGHT):
    screen.fill((30, 30, 35))
    # Player zones
    pygame.draw.rect(screen, (70, 70, 75), (0, 0, assets["MID_X"], assets["HEIGHT"] - 120))
    pygame.draw.rect(screen, (15, 15, 20), (assets["MID_X"], 0, assets["MID_X"], assets["HEIGHT"] - 120))
    pygame.draw.line(screen, (100, 100, 110), (assets["MID_X"], 0), (assets["MID_X"], assets["HEIGHT"] - 120), 4)
    # Draw players
    if "p1" in assets:
        assets["p1"].draw(screen, WIDTH, HEIGHT)
    if "p2" in assets:
        assets["p2"].draw(screen, WIDTH, HEIGHT)
    action_font = pygame.font.SysFont(None, 40)
    # Draw questions / choice of action
    if assets["p1_phase"] == "choosing_action":
        prompt_surf = action_font.render("CORRECT! Press [A] Attack or [D] Defend", True, (0, 255, 0))
        screen.blit(prompt_surf, (30, 100))
    else:
        p1_question = assets.get("p1_question")
        if p1_question:
            question_font = pygame.font.SysFont(None, 32)
            choice_font = pygame.font.SysFont(None, 28)
            question_surface = question_font.render(p1_question["question"], True, (255, 255, 255))
            screen.blit(question_surface, (30, 40))
            for index, choice_text in enumerate(p1_question["choices"]):
                text = f"{index + 1}. {choice_text}"
                choice_surface = choice_font.render(text, True, (255, 255, 255))
                screen.blit(choice_surface, (30, 90 + (index * 35)))
    shield_text = action_font.render(f"Shields: {assets['p1_shields']}", True, (100, 200, 255))
    screen.blit(shield_text, (30, assets["HEIGHT"] - 160))
    if assets["p2_phase"] == "choosing_action":
        prompt_surf = action_font.render("CORRECT! Press [J] Attack or [L] Defend", True, (0, 255, 0))
        screen.blit(prompt_surf, (assets["MID_X"] + 30, 100))
    else:
        p2_question = assets.get("p2_question")
        if p2_question:
            question_font = pygame.font.SysFont(None, 32)
            choice_font = pygame.font.SysFont(None, 28)
            question_surface = question_font.render(p2_question["question"], True, (255, 255, 255))
            screen.blit(question_surface, (WIDTH / 2 + 30, 40))
            for index, choice_text in enumerate(p2_question["choices"]):
                text = f"{index + 1}. {choice_text}"
                choice_surface = choice_font.render(text, True, (255, 255, 255))
                screen.blit(choice_surface, (WIDTH / 2 + 30, 90 + (index * 35)))
    shield_text2 = action_font.render(f"Shields: {assets['p2_shields']}", True, (100, 200, 255))
    screen.blit(shield_text2, (assets["MID_X"] + 30, assets["HEIGHT"] - 160))
    # Needed command
    pygame.display.flip()

# Processes player inputs during gameplay
def handle_gameplay_events(assets):
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return "quit", assets
        elif event.type == pygame.KEYDOWN:   
            # Also quits game
            if event.key == pygame.K_ESCAPE:
                return "quit", assets
            # Returns to second selection screen
            elif event.key == pygame.K_TAB:
                return "selection2", assets
            if assets["p1_phase"] == "answering":
                if event.key in P1_KEY_MAP:
                    selected_choice = P1_KEY_MAP[event.key]
                    assets["p1_total_questions"] += 1
                    current_question = assets.get("p1_question")
                    if current_question:
                        if selected_choice == str(current_question["answer"]):
                            print("Player 1 Correct!")
                            assets["p1_correct_questions"] += 1
                            assets["p1_phase"] = "choosing_action"
                        else:
                            print("Player 1 Incorrect!")
                            get_new_question = assets.get("get_new_question")
                            if get_new_question:
                                assets["p1_question"] = get_new_question(assets["p1_level"])
            elif assets["p1_phase"] == "choosing_action":
                if event.key == pygame.K_a:
                    if assets["p2_shields"] > 0:
                        assets["p2_shields"] -= 1
                        print("Player 1 broke 1 of Player 2's shields!")
                    else:
                        assets["p2"].health -= 10
                        if assets["p2"].health <= 0:
                            assets["winner_name"] = assets["p1"].name
                            return "endgame", assets
                    assets["p1_phase"] = "answering"
                    get_new_question = assets.get("get_new_question")
                    if get_new_question:
                        assets["p1_question"] = get_new_question(assets["p1_level"])
                elif event.key == pygame.K_d:
                    assets["p1_shields"] += 1
                    print(f"Player 1 added a shield! Total shields: {assets['p1_shields']}")
                    assets["p1_phase"] = "answering"
                    get_new_question = assets.get("get_new_question")
                    if get_new_question:
                        assets["p1_question"] = get_new_question(assets["p1_level"])
            if assets["p2_phase"] == "answering":
                if event.key in P2_KEY_MAP:
                    selected_choice = P2_KEY_MAP[event.key]
                    assets["p2_total_questions"] += 1
                    current_question = assets.get("p2_question")
                    if current_question:
                        if selected_choice == str(current_question["answer"]):
                            print("Player 2 Correct!")
                            assets["p2_correct_questions"] += 1
                            assets["p2_phase"] = "choosing_action"
                        else:
                            print("Player 2 Incorrect!")
                            get_new_question = assets.get("get_new_question")
                            if get_new_question:
                                assets["p2_question"] = get_new_question(assets["p2_level"])
            elif assets["p2_phase"] == "choosing_action":
                if event.key == pygame.K_j:
                    if assets["p1_shields"] > 0:
                        assets["p1_shields"] -= 1
                        print("Player 2 broke 1 of Player 1's shields!")
                    else:
                        assets["p1"].health -= 10
                        if assets["p1"].health <= 0:
                            assets["winner_name"] = assets["p2"].name
                            return "endgame", assets
                    assets["p2_phase"] = "answering"
                    get_new_question = assets.get("get_new_question")
                    if get_new_question:
                        assets["p2_question"] = get_new_question(assets["p2_level"])
                elif event.key == pygame.K_l:
                    assets["p2_shields"] += 1
                    print(f"Player 2 added a shield! Total shields: {assets['p2_shields']}")
                    assets["p2_phase"] = "answering"
                    get_new_question = assets.get("get_new_question")
                    if get_new_question:
                        assets["p2_question"] = get_new_question(assets["p2_level"])  
    # Return gameplay state by default
    return "gameplay", assets