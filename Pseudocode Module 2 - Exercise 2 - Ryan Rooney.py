// This pseudocode is intended to determine a monthly
// checking account fee

start
    // use variables for account balance and overdrawn fees
    set accountBalance = 0 
    set overDrawnFee = 0
    // collect account balance and number of times overdrawn
    input accountBalance
    input overDrawn
    // calculate fee and new balance
    compute overDrawnFee = accountBalance * .01 - 5
    compute fee = overDrawnFee * overDrawn
    compute newBalance = accountBalance - fee
    // display final calculations
    output print "This is the fee calculated: " + fee
    output print "This is the new balance: " + newBalance
    output print "Thanks for using this program."
stop
    
