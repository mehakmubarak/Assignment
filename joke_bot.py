PROMPT: str = "What do you want? "
JOKE: str = "Why did the programmer quit his job? Because he did not get arrays (a raise)!"
SORRY: str = "Sorry, I only tell more jokes."

def joke_bot():
    while True:
        user_input = input(PROMPT).strip().lower()
        
        if user_input == "joke":
            print(JOKE)
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print(SORRY)
if __name__ == "__main__":
    joke_bot()




