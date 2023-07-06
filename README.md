# Snake Game

## Requirements

- Python 3
- Pygame
- Pip package manager

## Getting started

First clone or download the repository, then run the command below inside the project directory :

`pip install -r requirements.txt`

When the installation is finished run this command to start the game :

`python3 main.py`

Enjoy !!

## Code structure

### Folders and files

- assets
  - apple.png
- src
  - config
    - constants.py
  - background.py
  - collision.py
  - fruit.py
  - score.py
  - snake.py
- .gitignore
- main.py
- README.md
- requirements.txt

### Constants

```
WIDTH : int : default = 800
HEIGHT : int : default = 800
PIXELS : int : default = 40
SQUARES : int : default = int(WIDTH / PIXELS)

# Colors
BG_PRIMARY : tuple : default = (146, 200, 50)
BG_SECONDARY : tuple : default = (137, 185, 47)
SNAKE_COLOR : tuple : default = (36, 0, 144)
TEXT_COLOR : tuple : default = (33, 33, 33)
```
