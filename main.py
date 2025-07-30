import random
import time
import nltk
from nltk.corpus import words

try:
    words.words()
except LookupError:
    nltk.download('words')

full_vocab = set(words.words())
five_letter_words = {word.lower() for word in full_vocab if len(word) == 5 and word.isalpha()}


def generate_random_word():
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))


def is_valid(candidate, heat):
    candidate = candidate.lower()

    if heat == 0:
        return True
    elif 1 <= heat <= 4:
        prefix_length = heat
        return any(word.startswith(candidate[:prefix_length]) for word in five_letter_words)
    elif heat == 5:
        return candidate in five_letter_words
    return False


def play_game(heat):
    if heat < 0 or heat > 5:
        print("Heat must be between 0 and 5.")
        return

    tries = 0
    start_time = time.perf_counter()

    while True:
        candidate = generate_random_word()
        tries += 1

        if is_valid(candidate, heat):
            break

    elapsed = time.perf_counter() - start_time
    print(f"\nGenerated Word: {candidate}")
    print(f"Tries: {tries}")
    print(f"Time: {elapsed:.2f} seconds")


if __name__ == "__main__":
    print("Welcome to the Word Heat Generator!")
    try:
        heat = int(input("Choose a heat level (0-5): "))
        play_game(heat)
    except ValueError:
        print("Invalid input. Please enter an integer between 0 and 5.")
