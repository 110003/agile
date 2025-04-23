"""
calculator.py - A simple calculator app that performs operations based on environment variables.
"""

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b."""
    return a / b

def main():
    """Main function to perform the operation based on environment variables."""
    a = int(os.getenv("FIRST_NUMBER", "0"))
    b = int(os.getenv("SECOND_NUMBER", "0"))
    op = os.getenv("OP", "add")

    if op == "add":
        print(add(a, b))
    elif op == "sub":
        print(subtract(a, b))
    elif op == "mul":
        print(multiply(a, b))
    elif op == "div":
        print(divide(a, b))
    else:
        print("Invalid operation")

if __name__ == "__main__":
    main()
