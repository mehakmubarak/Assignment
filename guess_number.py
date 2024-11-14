import random
def guess_my_number():
    target_number = random.randint(0, 99)
    attempts = 0  
    print("I am thinking of a number between 0 and 99...")
    while attempts < 4:
        guess = int(input("Enter a guess: ").strip())
        attempts += 1
        
        if guess > target_number:
            print("Your guess is too high.")
        elif guess < target_number:
            print("Your guess is too low.")
        else:
            print(f"Congrats! The number was: {target_number}")
            return 
    print("Good effort! The number was:", target_number)
    print("Keep trying, you'll crack it next time!")
    print("Better luck next time")
if __name__ == '__main__':
    guess_my_number()


