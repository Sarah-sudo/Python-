def add(a, b):
    print(f"Here we want to  find the answer of {a} + {b}: ")
    return a + b

def subtract(a, b):
    print(f"Here we want to  find the answer of {a} - {b}: ")
    return a - b

def multiply(a, b):
    print(f"Here we want to  find the answer of {a} * {b}: ")
    return a * b

def divide(a, b):
    print(f"Here we want to  find the answer of {a} / {b}: ")
    return a / b


print("\nLet's do some math with just functions: ")
age = add(20, 2)
height = subtract(178, 7)
weight = multiply(30, 2)
iq = divide(100, 2)
print(f"\nAge: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


