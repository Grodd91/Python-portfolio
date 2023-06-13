import pygame
import random

# Initialize Pygame library
pygame.init()

# Screen settings
screen_width = pygame.display.Info().current_w
screen_height = pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.display.set_caption("Fleeing Pet")

# Background color
background_color = (255, 255, 255)

# Pet class
class Pet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("pet.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, screen_width), random.randint(0, screen_height))
        self.speed = 3

    def update(self, mouse_pos):
        dx = self.rect.x - mouse_pos[0]
        dy = self.rect.y - mouse_pos[1]
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance < 200:
            if dx != 0:
                self.rect.x += self.speed if dx > 0 else -self.speed
            if dy != 0:
                self.rect.y += self.speed if dy > 0 else -self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

# Main program function
def main():
    clock = pygame.time.Clock()
    running = True

    pet = Pet()
    all_sprites = pygame.sprite.Group(pet)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_color)

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            pet.update(mouse_pos)

        all_sprites.update(mouse_pos)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Call the main program function
if __name__ == "__main__":
    main()
