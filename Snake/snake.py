import pygame
import time
import random

pygame.init()

# Screen settings
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 255, 0)
}

# Snake settings
snake_size = 20
snake_speed = 20

# Fonts
font_size = 35
font_style = pygame.font.SysFont(None, font_size)
score_font = pygame.font.SysFont(None, 25)

# Method to display the score
def display_score(score):
    text = score_font.render("Score: " + str(score), True, colors["black"])
    screen.blit(text, [0, 0])

# Method to draw the snake on the screen
def draw_snake(snake_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, colors["green"], [x[0], x[1], snake_size, snake_size])

# Main game method
def game():
    game_over = False
    game_exit = False

    # Initial snake position
    snake_x = screen_width / 2
    snake_y = screen_height / 2

    # Change in snake position
    snake_x_change = 0
    snake_y_change = 0

    # Create the snake
    snake_list = []
    snake_length = 1

    # Create food position
    food_x = round(random.randrange(0, screen_width - snake_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, screen_height - snake_size) / 20.0) * 20.0

    while not game_exit:
        while game_over:
            # Game over screen
            screen.fill(colors["white"])
            game_over_text = font_style.render("Game Over", True, colors["red"])
            screen.blit(game_over_text, [screen_width / 2 - 100, screen_height / 2 - 50])
            display_score(snake_length - 1)
            restart_button = pygame.Rect(screen_width / 2 - 70, screen_height / 2 + 50, 140, 50)
            pygame.draw.rect(screen, colors["black"], restart_button)
            restart_text = font_style.render("Restart", True, colors["white"])
            screen.blit(restart_text, [screen_width / 2 - 50, screen_height / 2 + 60])
            pygame.display.update()

            # Handle button click events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_r:
                        game()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if restart_button.collidepoint(mouse_x, mouse_y):
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_speed
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_speed
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_speed
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_speed
                    snake_x_change = 0

        # Update snake position
        snake_x += snake_x_change
        snake_y += snake_y_change

        # Wrap the snake around the screen boundaries
        if snake_x >= screen_width:
            snake_x = 0
        elif snake_x < 0:
            snake_x = screen_width - snake_size
        elif snake_y >= screen_height:
            snake_y = 0
        elif snake_y < 0:
            snake_y = screen_height - snake_size

        # Check for snake collision with itself
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        # Check for snake collision with food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, screen_height - snake_size) / 20.0) * 20.0
            snake_length += 1

        screen.fill(colors["white"])
        pygame.draw.rect(screen, colors["red"], [food_x, food_y, snake_size, snake_size])
        draw_snake(snake_size, snake_list)
        display_score(snake_length - 1)
        pygame.display.update()

        # Set the game speed
        pygame.time.Clock().tick(15)

    pygame.quit()

# Start the game
game()
