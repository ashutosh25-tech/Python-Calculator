def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("Calculator")
    print("+. Addition")
    print("-. Subtraction")
    print("*. Multiplication")
    print("/. Division")

    value = (input("Enter Your operator:-"))
    
    if value == "+":
        a = float(input("Enter the 1st value :-"))
        b = float(input("Enter the 2nd value :-"))
        
        print("Result:-",addition(a,b))

    elif value == "-":
        a = float(input("Enter the 1st value :-"))
        b = float(input("Enter the 2nd value :-"))

        print("Result:-",subtraction(a,b))

    elif value == "*":
        a = float(input("Enter the 1st value :-"))
        b = float(input("Enter the 2nd value :-"))


        print("Result:-",multiplication(a,b))

    elif value == "/":
        a = float(input("Enter the 1st value :-"))
        b = float(input("Enter the 2nd value :-"))


        print("Result:-",division(a,b))
    else:
        print("Exited")
        break