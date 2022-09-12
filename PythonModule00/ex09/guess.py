import random

def main():
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")
    secret = random.randint(1, 99)
    guess = 0
    count = 0
    while guess != secret:
        print("What's your guess between 1 and 99?")
        print(">> ", end="")
        try:
            guess = input()
            if guess == "exit":
                print("Goodbye!")
                exit(0)
            guess = int(guess)
        except ValueError:
            print("That's not a number.")
            continue
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        count += 1
    if count == 1:
        print("The answer to the ultimate question of life, the universe and everything is 42.")
    print("Congratulations, you've got it!")
    print("You won in {} attempts!".format(count))

if __name__ == "__main__":
    main()

    
