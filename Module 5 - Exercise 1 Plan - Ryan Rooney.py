// This code is intended to replicate a game of Jeopardy.
// This code will come from the view of the player.


start
    // setting the amount of time to answer and the total number of questions
    // as well as the number of categories
    set timeToAnswer = 5
    set numberOfQuestions = 0
    set row_1 = 200
    set row_2 = 400
    set row_3 = 600
    set row_4 = 800
    set row_5 = 1000
    // Ask the player to choose a category and give them 5 seconds to answer.
    // If the answer is correct, they are given the appropriate amount of
    // prize money.
    output "Please choose a category. You have 5 seconds to answer."
    while numberOfQuestions != 61
        input playerAnswer
        if playerAnswer == correctAnswer AND correctAnswer in row_1
            output "You answered correctly that's $200."
            increment numberOfQuestions + 1
        elif playerAnswer == correctAnswer AND correctAnswer in row_2
            output "You answered correctly that's $400."
            increment numberOfQuestions + 1
        elif playerAnswer == correctAnswer AND correctAnswer in row_3
            output "You answered correctly that's $600."
            increment numberOfQuestions + 1
        elif playerAnswer == correctAnswer AND correctAnswer in row_4
            output "You answered correctly that's $800."
            increment numberOfQuestions + 1
        elif playerAnswer == correctAnswer AND correctAnswer in row_5
            output "You answered correctly that's $1000."
            increment numberOfQuestions + 1
        elif timeAnswered >= timeToAnswer // If the answer took too long.
            output "You took to long to answer."
        else // If the answer is incorrect.
            output "I'm sorry that's the wrong answer." 
    endloop
    output "End of program."
stop
        
        
            
