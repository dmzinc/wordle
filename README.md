# Wordle Game

## Introduction

This project is a Wordle-style game implemented using object-oriented programming principles. The player attempts to guess a five-letter word within six tries, receiving feedback after each guess.

The game is structured around two main classes: `Game` and `Word`. It emphasizes clean, modular design and includes features like emoji-based feedback and scoring based on remaining attempts.

## Deliverables

- Developed game logic and feedback mechanism.
- Implemented an object-oriented structure.
- Scoring system based on remaining attempts.

## Features

- **Word Management:** The `Word` class handles the hidden word and feedback generation.
- **Game Logic:** The `Game` class manages gameplay, scoring, and attempts.
- **Feedback:** Visual feedback (e.g., emoji) is provided for each guess.
- **Scoring System:** Players score points based on remaining attempts.

## Program Design

### Classes Used

#### Word Class
Handles the hidden word and feedback generation:
- **`check_guess(guess):`** Compares the guess with the hidden word and provides feedback.

#### Game Class
Manages gameplay and scoring:
- **`make_guess(guess):`** Calls `check_guess()` and returns feedback.
- **`is_game_over(guess):`** Checks if the game has ended.
- **`calculate_score():`** Calculates the score based on remaining attempts.
- **`display_feedback(feedback):`** Outputs feedback for each letter in the guess.

### Supporting Functions
- **`load_words_from_file(file_path):`** Reads a list of five-letter words from a file.
- **`calculate_score():`** Calculates the player's score.
- **`display_feedback(feedback):`** Displays feedback symbols.

## Challenges and Solutions

### Splitting and Position Checking
One challenge was ensuring accurate feedback for letters present multiple times in a guess or the hidden word. This was solved by using a two-pass system:
1. Check for exact matches.
2. Check for misplaced matches.

### Emoji Feedback
Finding appropriate emojis to represent feedback categories was difficult. Symbols sourced from YayText.com were used to visually differentiate correct, misplaced, and incorrect letters.

## How to Run the Game

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd wordle
2. Ensure you have Python installed (version 3.7 or later is recommended).

3. Run the game with:
```bash
    Python wordle.py