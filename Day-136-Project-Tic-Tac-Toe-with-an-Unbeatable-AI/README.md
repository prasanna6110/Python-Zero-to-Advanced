# Day 136 · Project: Tic-Tac-Toe with an Unbeatable AI

_Projects_

**Concepts:** lists, functions, game loops, win checks and the **minimax** algorithm (recursion and game trees).

Play against an AI that **can never lose**. Minimax tries every possible future move and picks the best one.

## Code

### Tic-Tac-Toe with Minimax AI  ([`main.py`](main.py))

```python
import sys

DEMO = not sys.stdin.isatty()
LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def show(b):
    print()
    for r in range(3):
        print(" " + " │ ".join(b[r * 3 + c] if b[r * 3 + c] != " " else str(r * 3 + c + 1) for c in range(3)))
        if r < 2:
            print("───┼───┼───")
    print()

def winner(b):
    for a, c, d in LINES:
        if b[a] != " " and b[a] == b[c] == b[d]:
            return b[a]
    return "draw" if " " not in b else None

def minimax(b, player):
    w = winner(b)
    if w == "O": return 1, None
    if w == "X": return -1, None
    if w == "draw": return 0, None
    best = (-2, None) if player == "O" else (2, None)
    for i in range(9):
        if b[i] == " ":
            b[i] = player
            score, _ = minimax(b, "X" if player == "O" else "O")
            b[i] = " "
            if (player == "O" and score > best[0]) or (player == "X" and score < best[0]):
                best = (score, i)
    return best

def human_move(b):
    if DEMO:                                  # the demo "human" also plays smart
        _, move = minimax(b, "X")
        print(f"You (X) play {move + 1}")
        return move
    while True:
        raw = input("Your move (1-9): ")
        if raw.isdigit() and 1 <= int(raw) <= 9 and b[int(raw) - 1] == " ":
            return int(raw) - 1
        print("Invalid move")

def main():
    board = [" "] * 9
    print("❌⭕ TIC-TAC-TOE  (you = X, AI = O)")
    turn = "X"
    while winner(board) is None:
        show(board)
        if turn == "X":
            board[human_move(board)] = "X"
        else:
            _, move = minimax(board, "O")
            board[move] = "O"
            print(f"AI (O) plays {move + 1}")
        turn = "O" if turn == "X" else "X"
    show(board)
    w = winner(board)
    print("🤝 It's a draw! (perfect play from both sides)" if w == "draw" else f"🏆 {w} wins!")

if __name__ == "__main__":
    main()
```

## Extend this project

1. Add an "easy" AI that sometimes plays randomly.
2. Add alpha-beta pruning and count how many positions it skips.
3. Generalise the game to Connect Four.

---

[⬅ Day 135](../Day-135-Project-Hangman/README.md) · [🏠 Home](../README.md) · [Day 137 ➡](../Day-137-Project-To-Do-List-Manager-JSON-Storage/README.md)
