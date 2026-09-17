import random

easy_words = ["apple", "train", "tiger", "money", "pakistan"]
medium_words = ["pyhon", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "umbrella", "diamond", "computer", "mountain"]

print("welcome to the password guessing game")
print("chose a difficulty level: easy, medium or hard")

level = input('ENTER Difficulty: ').lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("invalid chice. defaulting to easy level")
    secret = random.choice(easy_words)


attempts = 0
print("\nGuess the secret password")

while True:
    guess = input("Enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f'Congratulations! You guessed it in {attempts} attempts.')
        break

    hint = ""

    for  i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint: ", hint)
print("Game Over")
