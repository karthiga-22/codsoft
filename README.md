

🤖 Tic-Tac-Toe AI with Minimax & Alpha-Beta Pruning

This is a simple command-line implementation of the classic Tic-Tac-Toe game in Python where a human player competes against an unbeatable AI opponent. The AI uses the Minimax algorithm with Alpha-Beta Pruning to make optimal moves.

📌 Features

Human vs AI gameplay

AI uses Minimax algorithm with Alpha-Beta Pruning for efficiency

Clean and interactive command-line interface

Detects win/loss/draw after each move

Fully functional 3x3 game board

🧠 How It Works

The AI (playing as 'O') uses the Minimax algorithm to simulate all possible future moves and chooses the optimal one. Alpha-Beta Pruning is applied to reduce the number of unnecessary branches evaluated, making the AI fast and efficient.


---

🕹 Gameplay

You play as 'X', AI plays as 'O'

Input your move as two integers: row col (e.g., 1 2)

The board is indexed from 0 to 2


Example:

You are 'X'. AI is 'O'.
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------
Enter your move (row and col 0-2):
✅ Requirements
Python 3.x
No external libraries are needed.

🚀 How to Run
1. Clone the repository:

git clone https://github.com/yourusername/tic-tac-toe-ai.git
cd tic-tac-toe-ai

2. Run the game:

python tic_tac_toe_ai.py

🧪 Algorithms Used

Minimax Algorithm: Explores all possible moves and selects the optimal one by maximizing the AI's chances of winning and minimizing the human player's.

Alpha-Beta Pruning: Enhances the Minimax algorithm by cutting off branches that don't need to be explored, improving efficiency.



