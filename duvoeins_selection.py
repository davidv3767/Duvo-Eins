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
def setup_selection1_assets(WIDTH, HEIGHT, MID_X):
    assets = {}
    assets['font'] = pygame.font.SysFont(None, 120)
    assets['p1_box_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 8 * 3 - 120, MID_X, 120)
    assets['p2_box_rect'] = pygame.Rect(WIDTH / 4, HEIGHT / 8 * 5 - 120, MID_X, 120)
    return assets

# Handles visuals for first selection screen
def draw_selection1(screen, assets, p1_name, p2_name, active_box):
    screen.fill((100, 100, 100))
    
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
    
    p1_display_text = f"P1 Name: {p1_name}"
    p2_display_text = f"P2 Name: {p2_name}"
    if active_box == "p1":
        p1_display_text += "|"
    else:
        p2_display_text += "|"

    p1_surface = assets['font'].render(p1_display_text, True, (255, 255, 255))
    p1_rect = p1_surface.get_rect(center=assets['p1_box_rect'].center)
    
    p2_surface = assets['font'].render(p2_display_text, True, (255, 255, 255))
    p2_rect = p2_surface.get_rect(center=assets['p2_box_rect'].center)

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
    GRID_COLOR = (255, 255, 255)
    BORDER_PAD = 100
    GRID_SIZE = HEIGHT - (2 * BORDER_PAD)
    START_X = (WIDTH / 4) - (GRID_SIZE / 2)
    END_X = (WIDTH / 4) + (GRID_SIZE / 2)
    assets = {}
    
    assets['lines'] = [
        Line((START_X, BORDER_PAD), (END_X, BORDER_PAD), GRID_COLOR, 8),
        Line((START_X, HEIGHT - BORDER_PAD), (END_X, HEIGHT - BORDER_PAD), GRID_COLOR, 8),
        Line((START_X, BORDER_PAD), (START_X, HEIGHT - BORDER_PAD), GRID_COLOR, 8),
        Line((END_X, BORDER_PAD), (END_X, HEIGHT - BORDER_PAD), GRID_COLOR, 8),
        Line((WIDTH / 4, BORDER_PAD), (WIDTH / 4, HEIGHT - BORDER_PAD), GRID_COLOR, 6),
        Line((START_X, MID_Y), (END_X, MID_Y), GRID_COLOR, 6)
    ]
    
    assets['circles'] = [
        StaticCircle((WIDTH / 4 - GRID_SIZE / 4, MID_Y - GRID_SIZE / 4), 100, (215, 25, 28)),
        StaticCircle((WIDTH / 4 + GRID_SIZE / 4, MID_Y - GRID_SIZE / 4), 100, (245, 210, 0)),
        StaticCircle((WIDTH / 4 - GRID_SIZE / 4, MID_Y + GRID_SIZE / 4), 100, (0, 130, 80)),
        StaticCircle((WIDTH / 4 + GRID_SIZE / 4, MID_Y + GRID_SIZE / 4), 100, (15, 85, 215))
    ]

    assets['stats_background'] = pygame.Rect(MID_X + BORDER_PAD, HEIGHT / 4, MID_X - (2 * BORDER_PAD), MID_Y)

    return assets

# Handles visuals for second selection screen
def draw_selection2(screen, assets):
    screen.fill((40, 40, 40))
    for line in assets['lines']:
        line.draw(screen)
    for circle in assets['circles']:
        circle.draw(screen)
    pygame.draw.rect(screen, (245, 230, 222), assets['stats_background'])
    pygame.display.flip()

# Processes player inputs at second selection screen
def handle_selection2_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return "quit"
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "quit"
            elif event.key == pygame.K_TAB:
                return "selection1"
    return "selection2"