# Kniffel (Yahtzee) Game

> [!NOTE]
> This README was generated using Claude AI.

A digital implementation of the classic dice game Kniffel built with Python and Pygame.

## About

Kniffel (or Yahtzee) is a dice game where players roll five dice up to three times per turn to make specific combinations. The goal is to achieve the highest total score across all categories.

## Installation

1. Clone this repository
2. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

```bash
python main.py
```

The game launches in fullscreen mode.

## Controls

**Rolling Phase:**
- `SPACE` - Roll the dice (up to 3 rolls per turn)
- `1-5` - Toggle keeping a specific die
- `ENTER` - Finish rolling and move to scoring
- `ESC` - Quit

**Scoring Phase:**
- Click on any empty category box to record your score

**Between Turns:**
- `ENTER` - Start next player's turn

## Scoring Categories

**Upper Section:** Ones through Sixes (sum of matching dice)

**Lower Section:**
- Three/Four of a Kind: Sum of all dice
- Full House: 25 points
- Small Street: 30 points
- Big Street: 40 points
- Kniffel: 50 points
- Chance: Sum of all dice

**Bonus:** 35 points if upper section totals 63 or more!

## Requirements

- Python 3.13+
- Pygame 2.6+

## License

MIT License - see LICENSE file for details.
