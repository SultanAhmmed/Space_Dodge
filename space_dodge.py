import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
PARTICLE_SIZE = 30
PLAYER_SPEED = 5
PARTICLE_SPEED = 3
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 100
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE
        self.speed = PLAYER_SPEED
    
    def move(self, keys):
        # Move left
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.x > 0:
            self.x -= self.speed
        # Move right
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
        # Move up
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.y > 0:
            self.y -= self.speed
        # Move down
        if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Particle:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - PARTICLE_SIZE)
        self.y = -PARTICLE_SIZE
        self.width = PARTICLE_SIZE
        self.height = PARTICLE_SIZE
        self.speed = PARTICLE_SPEED + random.uniform(-1, 1)
    
    def move(self):
        self.y += self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Dodge - Dodge the Particles!")
    clock = pygame.time.Clock()
    
    # Fonts
    font_large = pygame.font.Font(None, 74)
    font_medium = pygame.font.Font(None, 48)
    font_small = pygame.font.Font(None, 36)
    
    # Game state
    game_over = False
    score = 0
    
    # Create player
    player = Player()
    
    # Particle list
    particles = []
    particle_spawn_timer = 0
    particle_spawn_interval = 60  # Spawn every 60 frames initially
    
    running = True
    while running:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Restart game on SPACE when game over
                if event.key == pygame.K_SPACE and game_over:
                    game_over = False
                    score = 0
                    player = Player()
                    particles = []
                    particle_spawn_timer = 0
                    particle_spawn_interval = 60
        
        if not game_over:
            # Get keys pressed
            keys = pygame.key.get_pressed()
            
            # Move player
            player.move(keys)
            
            # Spawn particles
            particle_spawn_timer += 1
            if particle_spawn_timer >= particle_spawn_interval:
                particles.append(Particle())
                particle_spawn_timer = 0
                # Gradually increase difficulty
                if particle_spawn_interval > 20:
                    particle_spawn_interval -= 0.1
            
            # Move particles
            for particle in particles[:]:
                particle.move()
                
                # Check collision with player
                if player.get_rect().colliderect(particle.get_rect()):
                    game_over = True
                
                # Remove particles that are off screen
                if particle.is_off_screen():
                    particles.remove(particle)
                    score += 10  # Award points for dodging
        
        # Drawing
        screen.fill(BLACK)
        
        if not game_over:
            # Draw player
            player.draw(screen)
            
            # Draw particles
            for particle in particles:
                particle.draw(screen)
            
            # Draw score
            draw_text(screen, f"Score: {score}", font_small, WHITE, 100, 30)
            draw_text(screen, "Use Arrow Keys or WASD to move", font_small, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
        else:
            # Game over screen
            draw_text(screen, "GAME OVER!", font_large, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
            draw_text(screen, f"Final Score: {score}", font_medium, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20)
            draw_text(screen, "Press SPACE to restart", font_small, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80)
            draw_text(screen, "Press ESC to quit", font_small, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
