print("-"*90)
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"


print("Select operations you want to perform :")
print()
print("For Addittion      :  +")
print("For Subtraction    :  -")
print("For Multiplication :  *")
print("For Division       :  /")

print("-"*30)
operator = input("Enter the operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    print("Invalid operator")


print("Result: ", result)
