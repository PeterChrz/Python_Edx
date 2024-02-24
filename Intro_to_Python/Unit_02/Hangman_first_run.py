def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    guesses = 8
    letters_guessed = []
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long")
    print("------------")

    while guesses > 0:  # Game loop starts here
        print("You have", guesses, "guesses left.")
        print("Available letters:", getAvailableLetters(letters_guessed)) 
        letter = input("Please guess a letter: ").lower()

        if letter in letters_guessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, letters_guessed))
        elif letter in secretWord:
            letters_guessed.append(letter)
            print("Good guess:", getGuessedWord(secretWord, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", getGuessedWord(secretWord, letters_guessed))
            letters_guessed.append(letter)
            guesses -= 1

        print("------------")

        if isWordGuessed(secretWord, letters_guessed):
            print("Congratulations, you won!")
            break  # Exit the loop if the player wins

    # The 'else' block executes if the loop ends naturally (no breaks occurred)
    else:  
        print("Sorry, you ran out of guesses. The word was", secretWord)