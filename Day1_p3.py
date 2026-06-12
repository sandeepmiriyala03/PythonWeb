def add(a, b):
    return a + b

result = add(10, 20)
print(result)
def subtract(a, b):
    if a > b:
        return a - b
    return b - a

def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
