import random

def hangman():
    words = ["python", "flask", "pandas", "numpy", "django"]
    word = random.choice(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("=" * 40)
    print("       🎮 HANGMAN GAME 🎮")
    print("=" * 40)
    print(f"Guess the word! You have {max_incorrect} lives.")
    print(f"Word length: {len(word)} letters\n")
    
    while incorrect_guesses < max_incorrect:
        # Display current progress
        display = ""
        for letter in word:
            display += letter + " " if letter in guessed_letters else "_ "
        print(f"\nWord: {display}")
        print(f"Lives remaining: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: '{word}'")
            return True
        
        # Get user input
        guess = input("\nEnter a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter!")
            continue
            
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue
            
        guessed_letters.add(guess)
        
        if guess in word:
            print(f"✅ '{guess}' is in the word!")
        else:
            incorrect_guesses += 1
            print(f"❌ '{guess}' is not in the word!")
    
    print(f"\n💀 Game Over! The word was: '{word}'")
    return False

if __name__ == "__main__":
    hangman()
