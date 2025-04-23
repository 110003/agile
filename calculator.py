import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def main():
    print("Simple Calculator")
    a = float(os.getenv("FIRST_NUMBER", 0))
    b = float(os.getenv("SECOND_NUMBER", 0))
    operation = os.getenv("OP", "add").lower()

    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        result = "Invalid operation"

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
