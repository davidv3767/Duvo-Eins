import pygame

# Defines line class
class Line:
    def __init__(self, start, end, color, width=1):
        self.start = start
        self.end = end
        self.color = color
        self.width = width
    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.start, self.end, self.width)

# Defines static circle class
class StaticCircle:
    def __init__(self, center, radius, color, width=0):
        self.center = center
        self.radius = radius
        self.color = color 
        self.width = width
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.width)

# Initializes and returns all items needed for first selection screen
def setup_selection1_assets(WIDTH, HEIGHT, MID_X, MID_Y):
    # Setup assets
    assets = {}
    # Setup font
    assets['font'] = pygame.font.SysFont(None, 120)
    # Sets rectangles for text
    assets['p1_box_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 8 * 3 - 120, MID_X, 120)
    assets['p2_box_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 8 * 5 - 120, MID_X, 120)
    # Returns assets
    return assets

# Handles visuals for first selection screen
def draw_selection1(screen, assets, p1_name, p2_name, active_box):
    screen.fill((100, 100, 100))
    # Draws active boxes
    if active_box == "p1":
        p1_box_color = (255, 215, 0)
        p2_box_color = (100, 100, 100)
    elif active_box == "p2":
        p1_box_color = (100, 100, 100)
        p2_box_color = (255, 215, 0)
    else:
        p1_box_color = (100, 100, 100)
        p2_box_color = (100, 100, 100)    
    pygame.draw.rect(screen, p1_box_color, assets['p1_box_rect'], 4)
    pygame.draw.rect(screen, p2_box_color, assets['p2_box_rect'], 4)
    # Creates text for test graphics
    p1_display_text = f"P1 Name: {p1_name}"
    p2_display_text = f"P2 Name: {p2_name}"
    if active_box == "p1":
        p1_display_text += "|"
    else:
        p2_display_text += "|"
    # Initializes text graphics
    p1_surface = assets['font'].render(p1_display_text, True, (255, 255, 255))
    p1_rect = p1_surface.get_rect(center=assets['p1_box_rect'].center)
    p2_surface = assets['font'].render(p2_display_text, True, (255, 255, 255))
    p2_rect = p2_surface.get_rect(center=assets['p2_box_rect'].center)
    # Draws text graphics
    screen.blit(p1_surface, p1_rect)
    screen.blit(p2_surface, p2_rect)
    pygame.display.flip()

# Processes player inputs at first selection screen
def handle_selection1_events(p1_name, p2_name, active_box):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit", p1_name, p2_name, "p1"
        elif event.type == pygame.KEYDOWN:
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
                    if p1_name.strip() == p2_name.strip():
                        print("Error: Same Names")
                        active_box = "p1"
                    elif p1_name.strip() == "":
                        print("Error: Blank Name(s)")
                        active_box = "p2"
                    elif p2_name.strip() == "":
                        print("Error: Blank Name(s)")
                        active_box = "p1"
                    else:
                        return "selection2", p1_name, p2_name, "p2"
            else:
                if event.unicode.isprintable() and len(event.unicode) > 0:
                    if active_box == "p1" and len(p1_name) < 15:
                        p1_name += event.unicode
                    elif active_box == "p2" and len(p2_name) < 15:
                        p2_name += event.unicode
                        
    return "selection1", p1_name, p2_name, active_box

# Initializes and returns all items needed for second selection screen
def setup_selection2_assets(WIDTH, HEIGHT, MID_X, MID_Y):
    # Variables needed
    GRID_COLOR = (255, 255, 255)
    BORDER_PAD = 100
    GRID_SIZE = HEIGHT - (2 * BORDER_PAD)
    START_X = (WIDTH / 4) - (GRID_SIZE / 2)
    END_X = (WIDTH / 4) + (GRID_SIZE / 2)
    assets = {}
    # Initialize lines
    assets['lines'] = [
        Line((START_X, BORDER_PAD), (END_X, BORDER_PAD), GRID_COLOR, 8),
        Line((START_X, HEIGHT - BORDER_PAD), (END_X, HEIGHT - BORDER_PAD), GRID_COLOR, 8),
        Line((START_X, BORDER_PAD), (START_X, HEIGHT - BORDER_PAD), GRID_COLOR, 8),
        Line((END_X, BORDER_PAD), (END_X, HEIGHT - BORDER_PAD), GRID_COLOR, 8),
        Line((WIDTH / 4, BORDER_PAD), (WIDTH / 4, HEIGHT - BORDER_PAD), GRID_COLOR, 6),
        Line((START_X, MID_Y), (END_X, MID_Y), GRID_COLOR, 6)
    ]
    # Initialize circles
    assets['circles'] = [
        StaticCircle((WIDTH / 4 - GRID_SIZE / 4, MID_Y - GRID_SIZE / 4), 100, (215, 25, 28)),
        StaticCircle((WIDTH / 4 + GRID_SIZE / 4, MID_Y - GRID_SIZE / 4), 100, (245, 210, 0)),
        StaticCircle((WIDTH / 4 - GRID_SIZE / 4, MID_Y + GRID_SIZE / 4), 100, (0, 130, 80)),
        StaticCircle((WIDTH / 4 + GRID_SIZE / 4, MID_Y + GRID_SIZE / 4), 100, (15, 85, 215))
    ]
    # Initialize stats graphic
    assets['stats_background'] = pygame.Rect(MID_X + BORDER_PAD, HEIGHT / 4, MID_X - (2 * BORDER_PAD), MID_Y)
    assets['stats_font'] = pygame.font.SysFont(None, 60)
    # Initialize stats data
    assets['elements_data'] = {
        "1": {"color": "Red", "strong": "Yellow", "weak": "Blue"},
        "2": {"color": "Yellow", "strong": "Green", "weak": "Red"},
        "3": {"color": "Green", "strong": "Blue", "weak": "Yellow"},
        "4": {"color": "Blue", "strong": "Red", "weak": "Green"},
        "none": {"color": "Press 1-4 to See", "strong": "Press 1-4 to See", "weak": "Press 1-4 to See"}
    }
    assets['current_data'] = "none"
    # Key tracker
    assets['key_tracker'] = {
        "1": [0, 0],
        "2": [0, 0],
        "3": [0, 0],
        "4": [0, 0]
    }
    assets['current_chooser'] = "Player 1"
    assets['width'] = WIDTH
    assets['height'] = HEIGHT
    # Returns assets
    return assets

# Handles visuals for second selection screen
def draw_selection2(screen, assets):
    screen.fill((40, 40, 40))
    # Create grid lines
    for line in assets['lines']:
        line.draw(screen)
    # Create lines
    for circle in assets['circles']:
        circle.draw(screen)
    # Create stats (multi-step process) 
    pygame.draw.rect(screen, (245, 230, 222), assets['stats_background'])
    # Initialize what's neccessary
    TEXT_FONT = assets['stats_font']
    CURRENT_KEY = assets['current_data']
    ACTIVE_ELEMENT = assets['elements_data'][CURRENT_KEY]
    # Prepare surfaces & position
    COLOR_SURFACE = TEXT_FONT.render(f"Color: {ACTIVE_ELEMENT['color']}", True, (30, 30, 30))
    STRENGTH_SURFACE = TEXT_FONT.render(f"Strong Against: {ACTIVE_ELEMENT['strong']}", True, (30, 30, 30))
    WEAK_SURFACE = TEXT_FONT.render(f"Weak To: {ACTIVE_ELEMENT['weak']}", True, (30, 30, 30))
    FIRST_X = assets['stats_background'].x + 40
    FIRST_Y = assets['stats_background'].y + 50
    LINE_SPACING = 200
    # Create player num
    PLAYER_SURFACE = TEXT_FONT.render(assets['current_chooser'], True, (255, 255, 255))
    # Draw to screen
    screen.blit(COLOR_SURFACE, (FIRST_X, FIRST_Y))
    screen.blit(STRENGTH_SURFACE, (FIRST_X, FIRST_Y + LINE_SPACING))
    screen.blit(WEAK_SURFACE, (FIRST_X, FIRST_Y + (LINE_SPACING * 2)))
    screen.blit(PLAYER_SURFACE, (assets['width'] - 300, 100))
    pygame.display.flip()

# Processes player inputs at second selection screen
def handle_selection2_events(assets, PRESSED_KEY, p1_info, p2_info):
    # Input time for triple click
    CURRENT_TIME = pygame.time.get_ticks()
    TRIPLE_CLICK_THRESHOLD = 500
    for event in pygame.event.get():
        # Quits game
        if event.type == pygame.QUIT:
            return "quit", assets, None, p1_info, p2_info
        elif event.type == pygame.KEYDOWN:   
            # Also quits game
            if event.key == pygame.K_ESCAPE:
                return "quit", assets, None, p1_info, p2_info
            # Returns to first selection screen
            elif event.key == pygame.K_TAB:
                return "selection1", assets, None, p1_info, p2_info
            # Character data/selection keys
            elif event.key == pygame.K_1:
                PRESSED_KEY = "1"
            elif event.key == pygame.K_2:
                PRESSED_KEY = "2"
            elif event.key == pygame.K_3:
                PRESSED_KEY = "3"
            elif event.key == pygame.K_4:
                PRESSED_KEY = "4"
            # If character data/selection keys are pressed
            if PRESSED_KEY:
                # Show character data
                assets['current_data'] = PRESSED_KEY
                # Creates needed variables
                COUNT, LAST_PRESS_TIME = assets['key_tracker'][PRESSED_KEY]
                # Reset/add to count based on duration between clicks
                if CURRENT_TIME - LAST_PRESS_TIME > TRIPLE_CLICK_THRESHOLD:
                    COUNT = 1
                else:
                    COUNT += 1
                # Update tracker data
                assets['key_tracker'][PRESSED_KEY] = [COUNT, CURRENT_TIME]
                # Confirm seleciton if triple-tap
                if COUNT >= 3:
                    assets['key_tracker'][PRESSED_KEY][0] = 0
                    if p1_info[2] == False:
                        if PRESSED_KEY == 1:
                            p1_info[1] = "red"
                        elif PRESSED_KEY == 2:
                            p1_info[1] = "yellow"
                        elif PRESSED_KEY == 3:
                            p1_info[1] = "green"
                        elif PRESSED_KEY == 4:
                            p1_info[1] = "blue"
                        p1_info[2] = True
                        assets['current_chooser'] = "Player 2"
                    elif p2_info[2] == False:
                        if PRESSED_KEY == 1:
                            p2_info[1] = "red"
                        elif PRESSED_KEY == 2:
                            p2_info[1] = "yellow"
                        elif PRESSED_KEY == 3:
                            p2_info[1] = "green"
                        elif PRESSED_KEY == 4:
                            p2_info[1] = "blue"
                        p2_info[2] = True
                        return "gameplay", assets, None, p1_info, p2_info
    # Return default for 2nd selections screen
    return "selection2", assets, None, p1_info, p2_info