import random
def guess_num():
    start = 1
    end = 100
    target_number = random.randint(start, end)
    attempts = 0
    max_attempts = 7
    print("Welcome to Guess the Number!")
    print(f"I'm thinking of a number between {start} and {end}. Can you guess it?")
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        attempts += 1
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
            break
    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The correct number was {target_number}. Better luck next time!")
def main():
    while True:
        guess_num()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
