# Define the functions needed: add, sub, mul, div
# Print option to the user
# Get user input
# Call the function, when needed
# Loop till the user wants to exit

# Define add fucntion
def add(a, b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result))

# Sub function
def sub(a, b):
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result))

# Def multiplication function
def multiply(a, b):
    result = a * b
    print(str(a) + " * " + str(b) + " = " + str(result))

# Def division function
def divide(a, b):
    result = a / b
    print(str(a) + " / " + str(b) + " = " + str(result))

def prompt_user():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    return a, b

def main():
    choice_list = {"A": "Addition", 
                   "B":"Substraction", 
                   "C":"Multiplication", 
                    "D": "Division", 
                    "E":"Exit"}
    while True:
        for key, value in choice_list.items():
            print(key, value, sep=":")
        choice = input("Enter your choice (A, B, C, D, E): ").upper()
        match choice:
            case "A":
                a, b = prompt_user()
                add(a, b)
            case "B":
                a, b = prompt_user()
                sub(a, b)
            case "C":
                a, b = prompt_user()
                multiply(a, b) 
            case "D":
                a, b = prompt_user()
                if b > 0:
                   divide(a, b)
                else:
                    print("Divide by zero error") 
            case "E":
                break