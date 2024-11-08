import pygame, math

pygame.init()

SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 8
TITLE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV = math.pi / 3
HALF_FOV = FOV / 2

player_x = (SCREEN_WIDTH / 2) / 2
player_y = (SCREEN_HEIGHT / 2)
player_angle = math.pi

MAP = (
    "########",
    "# #    #",
    "# #  ###",
    "#      #",
    "#      #",
    "#  ##  #",
    "#   #  #",
    "########"
)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw_map():
    for row in range(MAP_SIZE):
        for col in range(MAP_SIZE):
            if MAP[row][col] == "#":
                pygame.draw.rect(screen, (100, 100, 100),pygame.Rect(col*TITLE_SIZE, row*TITLE_SIZE, TITLE_SIZE, TITLE_SIZE))
            elif MAP[row][col] == " ":
                pygame.draw.rect(screen, (0, 0, 0),pygame.Rect(col*TITLE_SIZE, row*TITLE_SIZE, TITLE_SIZE, TITLE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0),pygame.Rect(col*TITLE_SIZE, row*TITLE_SIZE, TITLE_SIZE, TITLE_SIZE), 1)

def draw_player():
    pygame.draw.circle(screen, (255, 0, 0), (player_x, player_y), 5)
    pygame.draw.line(screen, (255, 0, 0), (player_x, player_y), (player_x + math.sin(player_angle) * 10, player_y + math.cos(player_angle) * 10))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    
    draw_map()
    draw_player()

    pygame.display.flip()

pygame.quit()