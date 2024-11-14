import random
NUM_ROUNDS=5
def high_low_game(rounds):
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    user_score = 0

    for round_number in range(1, rounds + 1):
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"\nRound {round_number}")
        print(f"Your number is {user_number}")
        print("Do you think your number is higher or lower than the computer's? (type 'higher' or 'lower')")

        user_guess = input("Your guess: ").strip().lower()

        if (user_guess == 'higher' and user_number > computer_number) or \
           (user_guess == 'lower' and user_number < computer_number):
            user_score += 1
            print(f"You were right! The computer's number was {computer_number}")
            print(f"Your score is now {user_score}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
            print(f"Your score is now {user_score}")

    print("\nThanks for playing!")
    print(f"Your final score is {user_score} out of {rounds}")
    print(f"Better luck next next time! ")

rounds_to_play = 5  
high_low_game(rounds_to_play)
