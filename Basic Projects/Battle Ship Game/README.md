# 🚢 BattleShip Lite (Python)

A simple text-based **BattleShip Lite** game built in Python.  
The player has **3 attempts** to find the hidden ship randomly placed on a **3x3 grid**.

---

## 🎮 Game Rules

- The grid is numbered **1 to 9** like this:

1 | 2 | 3
---+---+---
4 | 5 | 6
---+---+---
7 | 8 | 9


- The ship is hidden in one of these 9 spots.
- You have **3 attempts** to guess the correct spot.
- Each wrong guess is marked as `X`.
- If you find the ship, it’s marked as 🚢.
- If all attempts are used, the real ship position is revealed.

---

## 🧩 Features

- Random ship placement each round  
- Input validation for invalid or duplicate guesses  
- Clean 3x3 board display after every attempt  
- Option to replay or quit the game  

---

## 🛠️ Requirements

- Python 3.x (any version after 3.6 works)
- No external libraries required (only `random` is used)

---

## ▶️ How to Run

1. Download or clone this repository  
 ```bash
 git clone https://github.com/<your-username>/BattleShip-Lite.git


Navigate into the folder

cd BattleShip-Lite


Run the Python file

python battleship_lite.py

📸 Example Gameplay
<-----Battle Ship Lite Game is Started----->
1 | 2 | 3
---+---+---
4 | 5 | 6
---+---+---
7 | 8 | 9

Attempt 1 to find Battle Ship choose b/w (1-9): 4

Wrong Guess
_  | _ | _
---+---+---
X  | _ | _
---+---+---
_  | _ | _

Attempt 2 to find Battle Ship choose b/w (1-9): 7
You found the Battle Ship at position 7!

💡 Future Improvements (Optional Ideas)

Add levels (3x3 → 5x5)

Add score tracking or limited lives

Use emojis or colors to improve terminal visuals

Store win/loss history in a file (once you learn file handling)

👨‍💻 Author

Prince Dedha
Learning Python through mini-projects to build strong logic and programming foundation.