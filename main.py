# Make sure art.py is in the same directory



import art
print(art.logo)

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    if n2 == 0:
        return "Cannot divide by zero"
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2

process = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

n1 = int(input("Write a first number: "))
calculator = True
while calculator:
    symbol = input("Pick an operation(+, -, *, /): ")
    n2 = int(input("Write a second number: "))

    answer = process[symbol](n1, n2)
    print(f"{n1} {symbol} {n2} = {answer}")
    choice = input("Do you want to continue?(yes/no): ")
    if choice == "yes":
        if answer == "Cannot divide by zero":
            n1 = int(input("Write a first number: "))
        else:
            ask = input(f"Do you want to continue calculating with {answer}?(yes/no): ")
            if ask == "yes":
                n1 = answer
            else:
                n1 = int(input("Write a first number: "))
    else:
        calculator = False
