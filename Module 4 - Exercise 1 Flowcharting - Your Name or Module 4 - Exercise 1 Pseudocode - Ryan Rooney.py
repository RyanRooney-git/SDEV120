// This code is intended to describe the process
// of guessing a number between 1 and 100
// After each guess, the player is told that the guess is too high or too low.
// The process continues until the player guesses the correct number.

start
    // gather input from player and set random number
    set randomNumber = (1, 100)
    output print "Please enter a number between 1 and 100: "
    input playerGuess
    // guessing for correct number
    while playerGuess != randomNumber:
        if playerGuess < randomNumber
            output print "Your guess is too low. Please try again. "
            input playerGuess
        elif playerGuess > randomNumber
            output print "Your guess is too high. Please try again. "
            input playerGuess
    output print "You guessed the right number!"

stop
