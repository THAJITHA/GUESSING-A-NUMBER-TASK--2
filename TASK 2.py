import random

def get_difficulty():
    print("\n🎮 Choose a difficulty level:")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        return 1, 10
    elif choice == "2":
        return 1, 50
    elif choice == "3":
        return 1, 100
    else:
        print("❌ Invalid choice. Defaulting to Medium level.")
        return 1, 50

def play_game(high_score):
    print("\n🔢 Starting a New Game!")
    min_val, max_val = get_difficulty()
    secret_number = random.randint(min_val, max_val)
    attempts = 0

    print(f"\n🤖 I'm thinking of a number between {min_val} and {max_val}. Can you guess it?")
    
    while True:
        try:
            guess = int(input("👉 Your guess: "))
            attempts += 1
            if guess < secret_number:
                print("📉 Too low!")
            elif guess > secret_number:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {attempts} attempts.")
                if high_score is None or attempts < high_score:
                    print("🏆 New High Score!")
                    high_score = attempts
                else:
                    print(f"⭐ Current High Score: {high_score} attempts")
                break
        except ValueError:
            print("❗ Please enter a valid number.")
    return high_score

def main():
    print("╔════════════════════════════════════════════╗")
    print("║        🎉 WELCOME TO NUMBER GUESSING GAME!         ║")
    print("╚════════════════════════════════════════════╝")
    high_score = None

    while True:
        high_score = play_game(high_score)
        again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
        if again not in ('yes', 'y'):
            print("\n👋 Thanks for playing! Come back soon.")
            break

# Run the game
main()
