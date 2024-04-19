import pygame
import random
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
player_paddle = pygame.Rect(screen_width - 20, screen_height // 2 - 70, 10, 140)
computer_paddle = pygame.Rect(10, screen_height // 2 - 70, 10, 140)
ball_speed_x = 7 * random.choice((-1, 1))
ball_speed_y = 7 * random.choice((-1, 1))
paddle_speed = 10
player_score = 0
computer_score = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    ball.move_ip(ball_speed_x, ball_speed_y)
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        ball.center = (screen_width // 2, screen_height // 2)
        ball_speed_y *= random.uniform(0.9, 1.1)
        ball_speed_x *= -1
    elif ball.right >= screen_width:
        computer_score += 1
        ball.center = (screen_width // 2, screen_height // 2)
        ball_speed_y *= random.uniform(0.9, 1.1)
        ball_speed_x *= -1
    if ball.colliderect(player_paddle) or ball.colliderect(computer_paddle):
        ball_speed_x *= -1
        ball_speed_y *= random.uniform(0.9, 1.1)
    if computer_paddle.centery < ball.centery and computer_paddle.bottom < screen_height:
        computer_paddle.move_ip(0, paddle_speed)
    elif computer_paddle.centery > ball.centery and computer_paddle.top > 0:
        computer_paddle.move_ip(0, -paddle_speed)
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w] and player_paddle.top > 0:
        player_paddle.move_ip(0, -paddle_speed)
    if keys_pressed[pygame.K_s] and player_paddle.bottom < screen_height:
        player_paddle.move_ip(0, paddle_speed)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), ball)
    pygame.draw.rect(screen, (0, 0, 0), player_paddle)
    pygame.draw.rect(screen, (0, 0, 0), computer_paddle)
    font = pygame.font.Font(None, 50)
    player_score_surface = font.render(str(player_score), True, (0, 0, 0))
    computer_score_surface = font.render(str(computer_score), True, (0, 0, 0))
    screen.blit(player_score_surface, (screen_width // 4, 50))
    screen.blit(computer_score_surface, (3 * screen_width // 4, 50))
    pygame.display.update()
    clock.tick(60)
