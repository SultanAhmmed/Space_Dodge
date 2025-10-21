# Quick Start Guide

## Get Started in 3 Steps!

### 1. Install Dependencies
```bash
pip install pygame
```

or use the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Run the Game
```bash
python space_dodge.py
```

### 3. Play!
- Use **Arrow Keys** or **WASD** to move
- Dodge the red falling particles
- Try to get the highest score!

## Controls
| Key | Action |
|-----|--------|
| ⬆️ / W | Move Up |
| ⬇️ / S | Move Down |
| ⬅️ / A | Move Left |
| ➡️ / D | Move Right |
| SPACE | Restart (when game over) |
| ESC | Quit Game |

## Tips
- The game gets harder over time
- Stay near the bottom for more reaction time
- Watch out for multiple particles at once
- Your score increases by 10 for each particle dodged

## Troubleshooting

### "pygame not found"
Install pygame:
```bash
pip install pygame
```

### "No module named 'space_dodge'"
Make sure you're in the Space_Dodge directory:
```bash
cd Space_Dodge
python space_dodge.py
```

### Game runs slowly
Close other applications to free up system resources.

## Running Tests
To verify everything works correctly:
```bash
python test_game.py
```

You should see all tests pass with ✓ marks.

---

**Have fun playing Space Dodge!** 🚀
