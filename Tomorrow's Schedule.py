import random

# List of words with optional hints
words = {
    "python": "A popular programming language",
    "hangman": "A classic word guessing game",
    "elephant": "The largest land animal",
    "guitar": "A musical instrument with strings"
}

# Hangman visual stages
stages = [
    """
      -----
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      -----
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

# Choose a random word
word, hint = random.choice(list(words.items()))
word_letters = set(word)  # unique letters in the word
guessed_letters = set()
wrong_guesses = 0
max_wrong = len(stages) - 1

print("Welcome to Hangman!")
print(f"Hint: {hint}")

# Game loop
while wrong_guesses < max_wrong and word_letters:
    # Display current progress
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print("\nWord: ", " ".join(display))
    
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue
    
    if guess in word_letters:
        guessed_letters.add(guess)
        word_letters.remove(guess)
        print("Good guess!")
    else:
        wrong_guesses += 1
        guessed_letters.add(guess)
        print("Wrong guess!")
        print(stages[wrong_guesses])

# End of game
if not word_letters:
    print(f"\nCongratulations! You guessed the word '{word}' correctly!")
else:
    print(f"\nGame Over! The word was '{word}'.")
