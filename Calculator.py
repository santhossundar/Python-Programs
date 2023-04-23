def add(operandOne, operandTwo):
    result = float(operandOne + operandTwo)
    return result

def subtract(operandOne, operandTwo):
    result = float(operandOne - operandTwo)
    return result

def multiply(operandOne, operandTwo):
    result = float(operandOne * operandTwo)
    return result

def divide(operandOne, operandTwo):
    result = "None"
    try:
        result = float(operandOne / operandTwo)
    except:
        print("float division by zero")
    
    return result

def power(operandOne, operandTwo):
    result = float(operandOne ^ operandTwo)
    return result

def remainder(operandOne, operandTwo):
    result = float(operandOne % operandTwo)
    return result

def history(history):
    if(len(history) != 0):
        for operation in range(len(history)):
            print(history[operation])
    else:
        print("No past calculations to show")

operationHistory = []

def getFormat(choice, op1, op2, result):
    operation = str(str(op1)+" "+choice+" "+str(op2)+" = "+str(result))
    return operation

def select_op(choice):
    if(choice == "#"): 
        return -1
    elif(choice == "?"):
        history(operationHistory)
        return 0

    print("Enter first number: ", end="")
    operandOne = str(input())
    print(operandOne)

    if("$" in operandOne):
        return 0
    elif("#" in operandOne):
        return -1
    elif("?" in operandOne):
        history(operationHistory)
        return 0

    try:
        _operandOne = float(operandOne)
    except:
        print("Not a valid number,please enter again")

    print("Enter second number: ", end="")
    operandTwo = str(input())
    print(operandTwo)

    if("$" in operandTwo):
        return 0
    elif("#" in operandTwo):
        return -1
    elif("?" in operandOne):
        history(operationHistory)
        return 0

    try:
        _operandTwo = float(operandTwo)
    except:
        print("Not a valid number,please enter again")

    if(choice == "+"):
        result = add(_operandOne, _operandTwo)
        operation = getFormat(choice, _operandOne, _operandTwo, result)
        operationHistory.append(operation)
        print(operation)
    elif (choice == "-"):
        result = subtract(_operandOne, _operandTwo)
        operation = getFormat(choice, _operandOne, _operandTwo, result)
        operationHistory.append(operation)
        print(operation)
    elif (choice == "*"):
        result = multiply(_operandOne, _operandTwo)
        operation = getFormat(choice, _operandOne, _operandTwo, result)
        operationHistory.append(operation)
        print(operation)
    elif (choice == "/"):
        result = divide(_operandOne, _operandTwo)
        operation = getFormat(choice, _operandOne, _operandTwo, result)
        operationHistory.append(operation)
        print(operation)
    elif (choice == "^"):
        result = power(_operandOne, _operandTwo)
        operation = getFormat(choice, _operandOne, _operandTwo, result)
        operationHistory.append(operation)
        print(operation)
    elif (choice == "%"):
        result = remainder(_operandOne, _operandTwo)
        operation = getFormat(choice, _operandOne, _operandTwo, result)
        operationHistory.append(operation)
        print(operation)
    else:
        print("Unrecognized operation")

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")
    
    # take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
    print(choice)
    if(select_op(choice) == -1):
        #program ends here
        print("Done. Terminating")
        exit()