import random # this imports the library needed to pick a random word

def play_hangman():
   # A list of the different possible animals that the user can guess
    word_list = [
        "monkey", "donkey", "jaguar", "cougar", "beaver", "rabbit", "badger", 
        "ferret", "weasel", "baboon", "coyote", "gopher", "walrus", "turtle", 
        "lizard", "iguana", "falcon", "parrot", "toucan", "pigeon", "puffin", 
        "condor", "osprey", "magpie", "salmon", "shrimp", "oyster", "spider", 
        "beetle", "hornet", "locust", "kitten"
    ]
     # it will randomly select one word from the list above
    secret_word = random.choice(word_list)
    
    lives = 6
    # an empty list to keep track of all the guesses the user inputs
    guessed_letters = []
    
    print("Welcome to Hangman Monkey")

    #this keeps the game running forever untill they win or lose
    while True:
        display_word = ""
        # builds the word and shows the letter guessed 
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\nWord: {display_word.strip()}")
        print(f"Remaining Lives: {lives}")

        # asks the player for the input then it converts it into lowerscase 
        guess = input("Guess a letter: ").lower().strip()

       # makes sure that the user only inputs 1 letter at a time
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            #makes sure that the user didnt guess the same letter
        if guess in guessed_letters:
            print("You already guessed that letter please try another one.")
            continue

        # adds the guess if valid to the tracking list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")
            
            # verifies if every letter in the word has been guessed
            word_complete = True
            for letter in secret_word:
                if letter not in guessed_letters:
                    word_complete = False
                    break
            
            # if the whole word was found then print the message "You win"
            if word_complete:
                
                print(f"\nWord: {' '.join(list(secret_word))}")
                print("you win even tho u suck!!!!")
                break
         # if the guess is wrong      
        else:
           
            print(f"Incorrect! '{guess}' is not in the word.")
            lives -= 1 # remove one life
            
            # if all lives are gone then print game over and reveal the word
            if lives == 0:
                
                print("\ngame over")
                print(f"The correct word was: {secret_word}")
                break
          
 #runs the game automatically when the code starts
if __name__ == "__main__":
    play_hangman()
