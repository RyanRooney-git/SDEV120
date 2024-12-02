# This code is intended to show how a
# telecommunications company charges
# its customers. It collects a customer's area code,
# phone number, and total number of tex messages.
# It should then output the bill data before and after taxes.
# It should collect text message data until a value is entered.

start
    // Set starting fees and other variables
    set monthlyFee = 5
    set first100 = 100
    set first300 = 300
    set tax = .14
    // Collect customer information
    output "Please enter your area code, phone number, and total number of text."
    input areaCode = three digit area code
    input phoneNum = seven digit number
    input totalText = total number text messages
    // Output information back to customer
    output " Your area code is: " + areaCode
    output " Your phone number is: " + phoneNum
    output " You total number of texts is: " + totalText
    


    input sentinelVal = ""
    while sentinelVal != "q"
    // Calculate company fees
        if totalText < first100
            bill = monthlyFee
        elif totalText > first300
            bill = (totalText * .02) + monthlyFee
        elif
            bill = (totalText * .03) + monthlyFee
        endif
        // Apply taxes to bill
        afterTaxes = bill * tax
        if totalText > first100 OR totalText > 10
            output "Your total bill before taxes is: " + bill
            output "Your total bill after taxes is : " + afterTaxes
            output "Total text messages: " + totalText
            output "Area code: " + areaCode
            output "Phone number: " + phoneNum
        endif
    endwhile

    // Prompt user to enter area code to view bills
    input sentinelVal = ""
    while sentinelVal != "q"
        output "Please enter a three digit area code to
        " view your bill or enter q to stop: "
        input regionCode
        if regionCode = areaCode
            output "Here is your bill before tasxes: " + bill
            output "Here is your bill after tasxes: " + afterTaxes
        endif
    endwhile
    output "Program ended."
stop

        
        

    

        
