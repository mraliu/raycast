import pygame, math

pygame.init()

SCREEN_HEIGHT = 480
SCREEN_WIDTH = SCREEN_HEIGHT * 2
MAP_SIZE = 8
TITLE_SIZE = int((SCREEN_WIDTH / 2) / MAP_SIZE)
FOV = math.pi / 3
HALF_FOV = FOV / 2

player_x = (SCREEN_HEIGHT / 2) / 2
player_y = (SCREEN_HEIGHT / 2) / 2 

MAP = (
    '########'
    '# #    #'
    '# #  ###'
    '#      #'
    '#      #'
    '#  ##  #'
    '#   #  #'
    '########'
)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

def draw_map():
    for i in range(MAP_SIZE):
        
        if MAP[i] == "#":
            pygame.draw.rect(screen, (100, 100, 100),pygame.Rect(i*TITLE_SIZE, 0, TITLE_SIZE, TITLE_SIZE))
            print(i+TITLE_SIZE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), 10)

    draw_map()

    pygame.display.flip()

pygame.quit()