import random

# Predefined list of words
word_list = [
    "love", "life", "home", "work", "play", "good", "time", "help", "come", "gone",
    "read", "book", "food", "walk", "talk", "stop", "open", "fast", "slow",
    "cold", "warm", "rain", "snow", "wind", "fire", "dark", "blue", "pink",
    "baby", "girl", "boy", "name", "face", "hand", "foot", "head", "hair", "eyes",
    "shop", "cash", "card", "bank", "ride", "bike", "cook", "bake", "wash",
    "call", "text", "mail", "send", "list", "note", "news", "data", "file", "code"
]

# Choose a random word
chosen_word = random.choice(word_list)
word_display = ["_"] * len(chosen_word)
guessed_letters = set()
incorrect_guesses = 0
max_incorrect = 6

print("🎉 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(f"You have {max_incorrect} incorrect guesses allowed.\n")

while incorrect_guesses < max_incorrect and "_" in word_display:
    print("Word:", " ".join(word_display))
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.\n")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for i, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[i] = guess
        print("✅ Good guess!\n")
    else:
        incorrect_guesses += 1
        print(f"❌ Wrong guess! You have {max_incorrect - incorrect_guesses} tries left.\n")

# Final result
if "_" not in word_display:
    print("🎊 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)
