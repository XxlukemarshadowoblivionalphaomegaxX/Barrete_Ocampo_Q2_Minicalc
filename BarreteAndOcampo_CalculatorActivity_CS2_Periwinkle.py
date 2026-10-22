print ("Welcome to calculator")
print ("Please choose an operation:")
print ("1: Addition")
print ("2: Subtraction")
print ("3: Multiplication")
print ("4: Division")
def operation_choice(choice):
    if choice == '1':
        print ("You have chosen addition.")
        return "addition"
    elif choice == '2':
        print ("You have chosen subtraction.")
        return "subtraction"
    elif choice == '3':
        print ("You have chosen multiplication.")
        return "multiplication"
    elif choice == '4':
        print ("You have chosen division.")
        return "division"
    elif choice < '1' or choice > '4':
        print ("Invalid choice.")
        return None

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        print("Error: Division by zero is not allowed.")
        return None

def getValues():
    num1 = int(input("enter your first number: "))
    num2 = int(input("enter your second number: "))
    return num1, num2

num1, num2 = getValues()

operation_choice = int(input("Enter your choice (1/2/3/4): "))
    
if operation_choice == 1:
    addition_result = addition(num1, num2)
    print ("The result of addition is: ", addition_result)
elif operation_choice == 2:
    subtraction_result = subtraction(num1, num2)
    print ("The result of subtraction is: ", subtraction_result)
elif operation_choice == 3:
    multiplication_result = multiplication(num1, num2)
    print ("The result of multiplication is: ", multiplication_result)
elif operation_choice == 4:
    division_result = division(num1, num2)
    if division_result is not None:
        print ("The result of division is: ", division_result)
