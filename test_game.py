"""
Simple tests for Space Dodge game components
"""
import pygame
import sys
import os

# Add the current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import game components
from space_dodge import Player, Particle, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_SIZE, PARTICLE_SIZE

def test_player_initialization():
    """Test that player initializes correctly"""
    pygame.init()
    player = Player()
    assert player.x == SCREEN_WIDTH // 2
    assert player.y == SCREEN_HEIGHT - 100
    assert player.width == PLAYER_SIZE
    assert player.height == PLAYER_SIZE
    print("✓ Player initialization test passed!")

def test_player_movement():
    """Test that player can move"""
    pygame.init()
    player = Player()
    initial_x = player.x
    
    # Create a mock key state dictionary-like object
    class MockKeys:
        def __init__(self):
            self.keys = {}
        def __getitem__(self, key):
            return self.keys.get(key, False)
    
    # Test right movement
    keys = MockKeys()
    keys.keys[pygame.K_RIGHT] = True
    player.move(keys)
    assert player.x > initial_x, "Player should move right"
    
    # Reset and test left movement
    player.x = initial_x
    keys = MockKeys()
    keys.keys[pygame.K_LEFT] = True
    player.move(keys)
    assert player.x < initial_x, "Player should move left"
    
    print("✓ Player movement test passed!")

def test_particle_initialization():
    """Test that particle initializes correctly"""
    pygame.init()
    particle = Particle()
    assert 0 <= particle.x <= SCREEN_WIDTH - PARTICLE_SIZE
    assert particle.y == -PARTICLE_SIZE
    assert particle.width == PARTICLE_SIZE
    assert particle.height == PARTICLE_SIZE
    print("✓ Particle initialization test passed!")

def test_particle_movement():
    """Test that particle moves down"""
    pygame.init()
    particle = Particle()
    initial_y = particle.y
    particle.move()
    assert particle.y > initial_y, "Particle should move down"
    print("✓ Particle movement test passed!")

def test_particle_off_screen():
    """Test particle off-screen detection"""
    pygame.init()
    particle = Particle()
    assert not particle.is_off_screen(), "Particle should not be off screen initially"
    
    particle.y = SCREEN_HEIGHT + 10
    assert particle.is_off_screen(), "Particle should be off screen"
    print("✓ Particle off-screen detection test passed!")

def test_collision_detection():
    """Test collision detection between player and particle"""
    pygame.init()
    player = Player()
    particle = Particle()
    
    # Position particle at player location
    particle.x = player.x
    particle.y = player.y
    
    player_rect = player.get_rect()
    particle_rect = particle.get_rect()
    
    assert player_rect.colliderect(particle_rect), "Should detect collision"
    print("✓ Collision detection test passed!")

def test_boundary_constraints():
    """Test that player stays within screen boundaries"""
    pygame.init()
    player = Player()
    
    # Create a mock key state
    class MockKeys:
        def __init__(self):
            self.keys = {}
        def __getitem__(self, key):
            return self.keys.get(key, False)
    
    # Test left boundary
    player.x = 0
    keys = MockKeys()
    keys.keys[pygame.K_LEFT] = True
    player.move(keys)
    assert player.x >= 0, "Player should not go beyond left boundary"
    
    # Test right boundary
    player.x = SCREEN_WIDTH - player.width
    keys = MockKeys()
    keys.keys[pygame.K_RIGHT] = True
    player.move(keys)
    assert player.x <= SCREEN_WIDTH - player.width, "Player should not go beyond right boundary"
    
    # Test top boundary
    player.y = 0
    keys = MockKeys()
    keys.keys[pygame.K_UP] = True
    player.move(keys)
    assert player.y >= 0, "Player should not go beyond top boundary"
    
    # Test bottom boundary
    player.y = SCREEN_HEIGHT - player.height
    keys = MockKeys()
    keys.keys[pygame.K_DOWN] = True
    player.move(keys)
    assert player.y <= SCREEN_HEIGHT - player.height, "Player should not go beyond bottom boundary"
    
    print("✓ Boundary constraints test passed!")

if __name__ == "__main__":
    print("\nRunning Space Dodge Game Tests...\n")
    
    try:
        test_player_initialization()
        test_player_movement()
        test_particle_initialization()
        test_particle_movement()
        test_particle_off_screen()
        test_collision_detection()
        test_boundary_constraints()
        
        print("\n" + "="*50)
        print("All tests passed successfully! ✓")
        print("="*50 + "\n")
        
        pygame.quit()
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        pygame.quit()
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Error running tests: {e}")
        pygame.quit()
        sys.exit(1)
