# 🚢 Battleship Lite (Python)

A simple yet fun **terminal-based Battleship guessing game** built using Python.  
Test your luck and logic — can you find the hidden battleship in just **3 attempts**?

---

## 🎮 Game Overview

**Battleship Lite** is a minimal version of the classic Battleship game designed for beginners learning Python.  
You play on a **3×3 grid** (positions 1–9), and your goal is to **find the hidden ship** randomly placed by the computer.

- You have **3 attempts** to find it.
- The game shows your **previous guesses** with ❌ marks.
- If you find the ship — it’s revealed with a 🚢 symbol.
- After 3 wrong guesses, the ship’s position is revealed.

---

## 🧠 Features

✅ 3×3 grid layout for easy visualization  
✅ Input validation (handles invalid or duplicate guesses)  
✅ Random ship placement every round  
✅ Replayable — play as many rounds as you want  
✅ Clear grid display and pattern reference  

---

## 🕹️ How to Play

1. **Run the program** in any Python terminal:
   ```bash
   python battleship_lite.py
2. Choose whether to start or quit:
   Do you Want to Play?(Y/N):
3. If you choose Y, a grid pattern will be shown:
   ```
   1  | 2 | 3
   ---+---+---
   4  | 5 | 6
   ---+---+---
   7  | 8 | 9
   ```
4. Guess where the ship might be by entering a number (1–9).  
   You get 3 total attempts.  
If you hit: 🚢 appears on that spot.  
If you miss: ❌ appears.  
5. After 3 attempts or a win, you can choose to play again or quit.
-----------------------------------------------------------------------------------------------------------------------------------------
## 💻 Example Gameplay  
Do you Want to Play?(Y/N): y  

<-----Battle Ship Lite Game is Started----->  

```
1  | 2 | 3
---+---+---
4  | 5 | 6
---+---+---
7  | 8 | 9
```

Attempt 1 to find Battle Ship choose b/w (1-9): 3  
Wrong Guess  

```
_  | _ | X
---+---+---
_  | _ | _
---+---+---
_  | _ | _
```

Attempt 2 to find Battle Ship choose b/w (1-9): 8  
Wrong Guess  

```
_  | _ | X
---+---+---
_  | _ | _
---+---+---
_  | _ | X
```

Attempt 3 to find Battle Ship choose b/w (1-9): 5  
Wrong Guess  

All attempt ended! Battle Ship was at 2  

```
_  | 🚢 | X
---+---+---
_  | X | _
---+---+---
_  | _ | X

```
----------------------------------------------------------------------------------------------------------------------------------------
## 🧩 Code Highlights  

Randomized ship position using random.randint(1,9)  

Smart input checks with:
```
if choice not in all_guesses and (1 <= choice <= 9):
```
Exception handling for invalid input:  
```
except ValueError:  
    print("❌ Invalid input. Enter a number between 1 and 9.")  
```
----------------------------------------------------------------------------------------------------------------------------------------
## 🧱 Project Structure  
```
Python-Learning-Journey/
│
└── Battle Ship Lite Game/
    ├── battleship_lite.py
    └── README.md

```
----------------------------------------------------------------------------------------------------------------------------------------
## 🏗️ Future Improvements  

Add difficulty levels (larger grids, more ships)  

Include score tracking across rounds  

Add AI hints (e.g., "You're close!")  

----------------------------------------------------------------------------------------------------------------------------------------

## 🧑‍💻 Author  

Prince Dedha  
Part of my ongoing Python learning journey.  
Exploring logic-building through fun, small projects.  

----------------------------------------------------------------------------------------------------------------------------------------

## 📜 License  

This project is open-source and available under the MIT License.  
   python battleship_lite.py
