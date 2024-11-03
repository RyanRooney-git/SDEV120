
// This pseudocode is intended to compute the number
// of miles per gallon you get with your automobile

start
    input milesTraveled
    input gallonsOfGas
    milesPerGallon = milesTraveled / gallonsOfGas
    output milesPerGallon

stop


// This pseudocode is intended to describe
// computing the daily cost of your rent
// in a 30-day month

start
    input monthRent
    dailyCost = monthRent / 30
    output dailyCost
    
stop

// This program accepts a user's monthly pay
// and rent, utilities, and grocery bills
// and displays the amount available for discretionary spending
// (which might be negative)
// Your program should output the pay and the total bills
// as well as the remaining discretionary amount

start
    input monthlyPay
    input rent
    input utilities
    input groceryBills
    bills = rent + utilities + groceryBills
    discretionarySpending = monthlyPay - bills
    output monthlyPay
    output bills
    output discretionarySpending

stop
