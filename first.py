# Example file showing a basic pygame "game loop"
import pygame
import math
# pygame setup
höjd = 1280
bredd = 720
pygame.init()
screen = pygame.display.set_mode((höjd, bredd))
clock = pygame.time.Clock()
running = True
dt = 0
bredd = 1280
höjd = 720
player_pos = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_colour = "blue" 
velocity = pygame.Vector2(300,300)
hit = False

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
        velocity.x = - velocity.x

    #Y led hastighet
    if ball_pos.y >= höjd or ball_pos.y <= 0: 
        velocity.y = -velocity.y


    distvec = ball_pos - player_pos
    normalvec = distvec.normalize()
    
    #collision detection
    c = distvec.magnitude()
    timeToHit = (c - 80)/velocity.magnitude()

    if(not hit and timeToHit < dt) :
        ball_pos += velocity * timeToHit 
        velocity = velocity.reflect(normalvec)
        ball_pos += velocity * (dt - timeToHit)
        ball_colour = "orange"
        hit = True
    else:
        ball_colour = "pink"
        ball_pos += velocity * dt
        hit = False
    
    #background
    screen.fill("black")
    #player
    pygame.draw.circle(screen, "white",player_pos, 40)
    #ball
    pygame.draw.circle(screen, ball_colour,ball_pos, 40)

    pygame.draw.line(screen, "white", ball_pos, player_pos)

    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()