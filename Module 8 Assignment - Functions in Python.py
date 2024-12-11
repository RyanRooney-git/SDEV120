a = 10
b = 6

def greaterThan(x, y):
    if x > y:
        return "true"
    else:
        return "false"
    
result = greaterThan(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + result + ".")
