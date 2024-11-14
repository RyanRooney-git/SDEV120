// This code is intended to mimic looking up a word in the dictionary and have the user guess a
// random word. If the word is incorrect the user will be told it is too
// far forward or too far back from the random word created.

start
    // setting a random word
    set randomWord
    // collecting user input
    output "Please enter a random word: "
    input playerWord
    // looping until the word is looked up
    while playerWord != randomWord
        if playerWord > randomWord
            output "Your too far forward. Try another word earlier."
            input playerWord
        elif playerWord < randomWord
            output "Your too far backwards. Try another word later."
            input playerWord
    output print "You found the word."             
stop
