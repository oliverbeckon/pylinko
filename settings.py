import ctypes, pygame, pymunk, enum

TITLE_STRING = 'Plinko'
FPS = 60

# Game config
STARTER_MONEY = 100
STARTER_BALLVAL = 5
STARTER_BALLAMOUNT = 10


# Maintain resolution regardless of Windows scaling settings
ctypes.windll.user32.SetProcessDPIAware()

WIDTH = 1920
HEIGHT = 1080

# Plinko config
BG_COLOR = (16, 32, 45)
MULTI_HEIGHT = int(HEIGHT / 19) # 56 on 1920x1080
MULTI_COLLISION = HEIGHT - (MULTI_HEIGHT * 2) # 968 on 1920x1080


OBSTACLE_COLOR = "White"
OBSTACLE_RAD = int(WIDTH / 240) # 8 on 1920x1080
OBSTACLE_PAD = int(HEIGHT / 19) # 56 on 1920x1080
OBSTACLE_START = (int((WIDTH / 2) - OBSTACLE_PAD), int((HEIGHT - (HEIGHT * .9)))) # (904, 108) on 1920x1080
segmentA_2 = OBSTACLE_START

BALL_RAD = 16


chip_Value = {
  1: 5,
  2: 10,
  0: 25,
}

class balls(enum.Enum):
    Normal = 0
    Golden = 1
    Charging = 2



# RGB Values for multipliers
multi_rgb = {
    (0, 20): (255, 0, 0),
    (1, 12): (255, 30, 0),
    (2, 6): (255, 60, 0),
    (3, 4): (255, 90, 0),
    (4, 2): (255, 120, 0),
    (5, 0.5): (255, 150, 0),
    (6, 0.2): (255, 180, 0),
    (7, 0.1): (255, 210, 0),
    (8, 0.1): (255, 240, 0),
    (9, 0.1): (255, 210, 0),
    (10, 0.2): (255, 180, 0),
    (11, 0.5): (255, 150, 0),
    (12, 2): (255, 120, 0),
    (13, 4): (255, 90, 0),
    (14, 6): (255, 60, 0),
    (15, 12): (255, 30, 0),
    (16, 20): (255, 0, 0),
    
}

# Number of multipliers shown underneath obstacles
NUM_MULTIS = 17

# Pymunk settings (prevent same class collisions)
BALL_CATEGORY = 1
OBSTACLE_CATEGORY = 2
BALL_MASK = pymunk.ShapeFilter.ALL_MASKS() ^ BALL_CATEGORY
OBSTACLE_MASK = pymunk.ShapeFilter.ALL_MASKS()

# Audio stuff
pygame.mixer.init()
click = pygame.mixer.Sound("audio/click.mp3")
sound01 = pygame.mixer.Sound("audio/001.mp3")
sound01.set_volume(0.2)
sound02 = pygame.mixer.Sound("audio/002.mp3")
sound02.set_volume(0.3)
sound03 = pygame.mixer.Sound("audio/003.mp3")
sound03.set_volume(0.4)
sound04 = pygame.mixer.Sound("audio/004.mp3")
sound04.set_volume(0.5)
sound05 = pygame.mixer.Sound("audio/005.mp3")
sound05.set_volume(0.6)
sound06 = pygame.mixer.Sound("audio/006.mp3")
sound06.set_volume(0.7)
sound07 = pygame.mixer.Sound("audio/007.mp3")
sound07.set_volume(0.8)