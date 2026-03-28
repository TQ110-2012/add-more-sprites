import pygame
import random

pygame.init()

screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Collision Game")

bg_color = (58, 58, 58)
score = 0
font = pygame.font.SysFont("Arial", 24)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]: self.rect.x += self.speed
        if keys[pygame.K_UP]: self.rect.y -= self.speed
        if keys[pygame.K_DOWN]: self.rect.y += self.speed

player = Sprite((0, 255, 0), 250, 250)
enemies = pygame.sprite.Group()

for i in range(7):
    enemy = Sprite((255, 0, 0), random.randint(0, 470), random.randint(0, 470))
    enemies.add(enemy)

all_sprites = pygame.sprite.Group(player, *enemies)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    collisions = pygame.sprite.spritecollide(player, enemies, True)
    for hit in collisions:
        score += 1

    screen.fill(bg_color)
    all_sprites.draw(screen)
    
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
