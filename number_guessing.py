import random

secret_number = random.randint(1, 100)
guess_count = 0

while True:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess > secret_number:
        print("Too High!")

    elif guess < secret_number:
        print("Too Low!")

    else:
        print("Congratulations! You guessed it!")
        break

print(f"You guessed the secret number in {guess_count} moves.")
