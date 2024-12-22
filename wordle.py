import random

## Compare guess to the hidden word and provide feedback on each letter.
class Word:
    def __init__(self, word):
        self._word = word  # Hidden word
        
    def check_guess(self, guess):
        feedback = []
        for i, char in enumerate(guess):
            if char == self._word[i]:  # Correct letter and position
                feedback.append("🟩")
            elif char in self._word:  # Correct letter, wrong position
                feedback.append("🟧")
            else:  # Incorrect letter
                feedback.append("⬛")
        return feedback


class Game:
    def __init__(self, word_list):
        self.word = Word(random.choice(word_list))
        self.attempts = 6  # Maximum attempts
        self.score = 0     # Initial score

    def make_guess(self, guess):
        feedback = self.word.check_guess(guess)
        self.attempts -= 1
        return feedback

    def is_game_over(self, guess):
        # Game is over if guessed correctly or out of attempts
        return guess == self.word._word or self.attempts <= 0

    def calculate_score(self):
        # Score based on remaining attempts
        self.score = self.attempts * 10

    def display_feedback(self, feedback):
        print(" ".join(feedback))


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            # Read lines, strip newline characters, and filter only 5-letter words
            return [line.strip().lower() for line in file if len(line.strip()) == 5]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []


def main():
    # Load word list from file
    word_list = read_file("word.txt")
    
    # Ensure word list is not empty
    if not word_list:
        print("Word list is empty or file could not be read. Exiting game.")
        return
    
    # Initialize the game
    game = Game(word_list)
    print("Welcome to Wordle! Try to guess the 5-letter word.")
    
    # Main game loop
    while game.attempts > 0:
        guess = input(f"Enter your guess ({game.attempts} attempts left): ").lower()
        
        # Validate guess length
        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        feedback = game.make_guess(guess)
        game.display_feedback(feedback)
        
        # Check if game is over
        if game.is_game_over(guess):
            if guess == game.word._word:
                print("Congratulations! You've guessed the word correctly!")
                game.calculate_score()
            else:
                print(f"Game over! The correct word was '{game.word._word}'.")
            
            print(f"Your score: {game.score}")
            break
    else:
        print(f"Out of attempts! The word was '{game.word._word}'.")
        print(f"Your score: {game.score}")


if __name__ == "__main__":
    main()
