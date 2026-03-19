# 🎮 AI Games Hub

A collection of classic games built with Python, featuring intelligent AI opponents powered by algorithms like **Minimax** and **Alpha-Beta Pruning**. This project serves as a learning resource for understanding AI decision-making in game development.

---

## 📁 Project Overview

The repository contains three classic games, each implemented with a clean architecture and an unbeatable or challenging AI.

| Game          | Description                                                                 | AI Technique                     |
|---------------|-----------------------------------------------------------------------------|----------------------------------|
| **Chess**     | Full chess game with GUI, move validation, and AI opponent.                | Minimax with Alpha-Beta Pruning |
| **Nim**       | Mathematical strategy game where players remove objects from piles.        | Minimax with depth limiting      |
| **Tic Tac Toe** | Classic 3×3 board game against an unbeatable AI.                          | Minimax Algorithm                |

Each game has its own dedicated documentation inside its respective folder.

---

## ✨ Features

- **🤖 AI-Powered Gameplay** – Play against intelligent agents that use classic search algorithms.
- **🧠 Algorithmic Learning** – Clear implementation of Minimax and Alpha-Beta Pruning.
- **🖥️ Graphical Interfaces** – User‑friendly GUIs built with Tkinter and Pygame.
- **📂 Modular Structure** – Each game is self‑contained, making it easy to navigate and extend.
- **🐍 Pure Python** – No external dependencies beyond the standard library and a few lightweight packages.

---

## 🛠️ Technologies Used

- **Python 3.6+**
- **Tkinter** (built‑in) – for Nim and Tic Tac Toe GUIs
- **Pygame** – for Chess board rendering and interaction
- **Chess** library – for move generation and validation in Chess
- **Minimax Algorithm** – core AI decision‑making
- **Alpha‑Beta Pruning** – optimization for the Chess AI

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher installed on your system.
- `pip` package manager.

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/zahidul2001/AI_Game.git
   cd ai-games-hub
   ```

2. **Install required packages**

   The Chess game requires `pygame` and `chess`. Run:

   ```bash
   pip install pygame chess
   ```

   Nim and Tic Tac Toe use only Tkinter, which comes pre‑installed with Python.

### Running a Game

Navigate to the desired game folder and execute the main Python file:

- **Chess**  
  ```bash
  cd chess
  python chess_game.py
  ```

- **Nim**  
  ```bash
  cd nim
  python nim_game.py
  ```

- **Tic Tac Toe**  
  ```bash
  cd tic_tac_toe
  python tic_tac_toe.py
  ```

---

## 📚 Learning Outcomes

By exploring this project, you will:

- Understand how the **Minimax algorithm** works and how it can be applied to turn‑based games.
- Learn about **Alpha‑Beta Pruning** and its role in optimising game trees.
- Gain experience in building **graphical user interfaces** with Tkinter and Pygame.
- See practical examples of **object‑oriented design** and **modular programming** in Python.

---

## 🔮 Future Improvements

- [ ] Add difficulty levels for Chess (adjustable search depth).
- [ ] Convert the games into web applications using Flask or Django.
- [ ] Include more classic games (e.g., Connect Four, Checkers).
- [ ] Implement a scoring system or game statistics.
- [ ] Provide an option for human‑vs‑human mode.

---

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the code, fix a bug, or add a new game, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

Please ensure your code follows the existing style and includes appropriate comments.

---

## 📧 Contact

For suggestions, feedback, or questions, feel free to open an issue or reach out via email at **your.email@example.com**.

---

⭐ **If you find this project helpful or interesting, please consider giving it a star!** ⭐