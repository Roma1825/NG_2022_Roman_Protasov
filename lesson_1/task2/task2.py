variable_1 = float(input("Your first variable:"))              #Request to enter the first variable
variable_2 = float(input("Your second variable:"))             #Request to enter the second variable

print("Yours variables:", variable_1, "and", variable_2)       #Output the entered variables to the user

operation = input('''Ok, now u need to choose what the operation you want to do:
-
+
*
/
= (compares your numbers, yes)
*2 - square (uses first variable as base, second as exponent number)
/2 - root of the square (uses only first variable)
Type one of the symbol shown before to start calculation.''')  #Requests to select an operation with the entered numbers

match operation:
    case "-":                                                  #Subtraction operation
        print(variable_1 - variable_2)
    case "+":                                                  #Sum operation
        print (variable_1 + variable_2)
    case "*":                                                  #Multiplication operation
        print(variable_1 * variable_2)
    case "/":                                                  #Division operation
        if variable_2 == 0:                                    #Check if the second variable is equal to zero
            print("Cant divide by zero.")                      #Warning not to divide by zero
        else:
            print(variable_1 / variable_2)
    case "=":                                                  #Compare operation
        if variable_1 > variable_2:
            print("Value",variable_1,"bigger then",variable_2) #If the first variable is larger than the second, the output follows the format "1 > 2"
        elif variable_1 < variable_2:
            print("Value",variable_2,"bigger then",variable_1) #If the second variable is larger than the first, the output follows the format "2 > 1"
        elif variable_1 == variable_2:
            print("Entered numbers are the same.")             #If both variables are equal, then output the corresponding message
    case "*2":                                                 #Exponentiation operation, the second variable acts as a power number
        print(variable_1 ** variable_2)
    case "/2":                                                 #Root of the number operation
        print(variable_1 ** 0.5)