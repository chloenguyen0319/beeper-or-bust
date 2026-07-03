# Beeper or Bust - Karel's Journey Home

A simple terminal puzzle game written in Python. Guide Karel from the top-left corner of a 10×10 grid to the goal at the bottom-right, while managing a limited bag of beepers and a limited number of steps.

## How to Run

```bash
python Karel_game.py
```

## Gameplay

Karel starts at position (1, 10) - the top-left of the grid - and must reach position (10, 1), marked **G**, in the bottom-right corner.

**Starting conditions:**
- Bag: 4 beepers
- Step limit: 20 steps

### Beeper Rules

Each step Karel takes onto a new square, the beeper rule applies:

| Beepers on square | Effect on bag |
|-------------------|---------------|
| 0 (empty)         | −1 beeper     |
| 1                 | no change     |
| 2                 | +1 beeper     |
| 3                 | +2 beepers    |

After landing, Karel picks up all beepers on the square and puts exactly 1 back down.

### Win / Lose Conditions

- **You win** - Karel reaches the goal square (G) within the step limit with beepers remaining.
- **Game over** - Karel's bag drops below 0, or Karel runs out of steps.

## Controls

| Key | Direction |
|-----|-----------|
| `w` | Up        |
| `s` | Down      |
| `a` | Left      |
| `d` | Right     |

## Tips

- Plan a route that passes through squares with 2 or 3 beepers to keep your bag topped up.
- The grid is fixed, so you can map out an optimal path before committing to moves.
- A shorter, more direct route conserves steps but may miss beeper pickups - balance both.
