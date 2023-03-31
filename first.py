# Example file showing a basic pygame "game loop"
import pygame
import math
# pygame setup
hastighetx = 200
hastighety = 250
höjd = 1280
bredd = 720
pygame.init()
screen = pygame.display.set_mode((höjd, bredd))
clock = pygame.time.Clock()
running = True
dt = 0
bredd = 1280
höjd = 720
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_colour = "blue" 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys [pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys [pygame.K_s]:
        player_pos.y += 300 * dt
    if keys [pygame.K_d]:
        player_pos.x += 300 * dt
    if keys [pygame.K_a]:
        player_pos.x -= 300 * dt

    if player_pos.x < 0:
        player_pos.x = 0
    if player_pos.x > bredd:
        player_pos.x = bredd
    if player_pos.y > höjd:
        player_pos.y = höjd
    if player_pos.y < 0:
        player_pos.y = 0


    #X led hastighet
    if ball_pos.x >= bredd or ball_pos.x <= 0: 
        hastighetx = -hastighetx

    ball_pos.x += hastighetx * dt 

    #Y led hastighet
    if ball_pos.y >= höjd or ball_pos.y <= 0: 
        hastighety = -hastighety

    ball_pos.y += hastighety * dt 
    



    #collision detection
    c = math.sqrt(math.pow(ball_pos.x-player_pos.x,2) + math.pow(ball_pos.y-player_pos.y,2))
    
    if c <= 80:
        ball_colour = "red"
    else:
        ball_colour = "blue"


    
    #background
    screen.fill("black")
    #player
    pygame.draw.circle(screen, "white",player_pos, 40)
    #ball
    pygame.draw.circle(screen, ball_colour,ball_pos, 40)
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()