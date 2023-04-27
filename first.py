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
player_pos2 = pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2)
ball_colour = "blue" 
velocity = pygame.Vector2(300,300)
text_color = (255, 255, 255)
score = 0
font = pygame.font.SysFont(None, 24)

def collision_detection(player_pos, ball_pos, velocity, dt) :

    distvec = ball_pos - player_pos
    normalvec = distvec.normalize()

    #collision detection
    c = distvec.magnitude()
    timeToHit = (c - 80)/velocity.magnitude()
    hit = False

    if(not hit and timeToHit < dt) :
        ball_pos += velocity * timeToHit 
        velocity = velocity.reflect(normalvec)
        ball_pos += velocity * (dt - timeToHit)
        hit = True
    else:
        ball_pos += velocity * dt
        hit = False
    return ball_pos, velocity

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

    keys = pygame.key.get_pressed()
    if keys [pygame.K_o]:
        player_pos2.y -= 300 * dt
    if keys [pygame.K_l]:
        player_pos2.y += 300 * dt

    if player_pos.x < 0:
        player_pos.x = 0
    if player_pos.x > bredd:
        player_pos.x = bredd
    if player_pos.y > höjd:
        player_pos.y = höjd
    if player_pos.y < 0:
        player_pos.y = 0

    if player_pos2.x < 0:
        player_pos2.x = 0
    if player_pos2.x > bredd:
        player_pos2.x = bredd
    if player_pos2.y > höjd:
        player_pos2.y = höjd
    if player_pos2.y < 0:
        player_pos2.y = 0
    #X led hastighet
    if ball_pos.x >= bredd or ball_pos.x <= 0: 
        velocity.x = - velocity.x
        score = score + 1

    #Y led hastighet
    if ball_pos.y >= höjd or ball_pos.y <= 0: 
        velocity.y = -velocity.y


    ball_pos, velocity = collision_detection(player_pos, ball_pos, velocity, dt)
    ball_pos, velocity = collision_detection(player_pos2, ball_pos, velocity, dt)
    
    #background
    screen.fill("black")
    #player
    pygame.draw.circle(screen, "white",player_pos, 40)
    pygame.draw.circle(screen, "white",player_pos2, 40)
    
    #ball
    pygame.draw.circle(screen, ball_colour,ball_pos, 40)

    pygame.draw.line(screen, "white", ball_pos, player_pos)
    pygame.draw.line(screen, "white", ball_pos, player_pos2)
    img = font.render(str(score), True, text_color)
    screen.blit(img, (740, 20))
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(60) / 1000  # limits FPS to 60

pygame.quit()