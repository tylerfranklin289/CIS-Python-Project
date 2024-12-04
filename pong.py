import pygame
import sys

pygame.init()



#resolution 
screen_width = 800
screen_height = 600

#color reference
white = (255, 255, 255)
black = (0, 0, 0)

#paddle
paddle_width = 10
paddle_height = 100


ball_size = 15

#speed, adjust for difficulty
PADDLE_SPEED = 5
ball_speed_X = 4
ball_speed_Y = 4


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")


clock = pygame.time.Clock()

#positions
player1_paddle = pygame.Rect(50, (screen_height - paddle_height) // 2, paddle_width, paddle_height)
player2_paddle = pygame.Rect(screen_width - 50 - paddle_width, (screen_height - paddle_height) // 2, paddle_width, paddle_height)
ball = pygame.Rect((screen_width - ball_size) // 2, (screen_height - ball_size) // 2, ball_size, ball_size)

#ball direction
ball_dx = ball_speed_X
ball_dy = ball_speed_Y

#scoring
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

#loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player1_paddle.bottom < screen_height:
        player1_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player2_paddle.bottom < screen_height:
        player2_paddle.y += PADDLE_SPEED

    #ball movement with edge
    ball.x += ball_dx
    ball.y += ball_dy

    #ball collision with paddle
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_dy = -ball_dy

    #ball collision 
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_dx = -ball_dx
##    ai
##    def player2_ai():
##        if player2_paddle.top < ball.y:
##            player2_paddle.top += player2_speed
##        if player2_paddle.bottom -= player2_






    #ball out of bounds
    if ball.left <= 0:
        player2_score += 1
        ball.x, ball.y = (screen_width - ball_size) // 2, (screen_height - ball_size) // 2
        ball_dx = ball_speed_X
    if ball.right >= screen_width:
        player1_score += 1
        ball.x, ball.y = (screen_width - ball_size) // 2, (screen_height - ball_size) // 2
        ball_dx = -ball_speed_X

    #drawing ball and paddle
    screen.fill(black)
    pygame.draw.rect(screen, white, player1_paddle)
    pygame.draw.rect(screen, white, player2_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (screen_width // 2, 0), (screen_width // 2, screen_height))

    #scores
    player1_text = font.render(str(player1_score), True, white)
    player2_text = font.render(str(player2_score), True, white)
    screen.blit(player1_text, (screen_width // 4, 20))
    screen.blit(player2_text, (screen_width * 3 // 4, 20))

    #display update
    pygame.display.flip()
    clock.tick(60)


#quit
pygame.quit()
sys.exit()
