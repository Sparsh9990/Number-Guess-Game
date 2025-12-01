print("\nVS Code and Python setup complete! Happy coding! \n" )

# Numbers and math
x = 15
y = 4
print("x * y =", x * y, "\n")

# Strings
my_language = "Python"
print("I'm learning", my_language, "\n")

# Boolean
is_fun = True
print("Is coding fun?", is_fun, "\n")

# Ask the user for their name
name = input("Enter your name: ")
print("\nHello,", name)

# Ask for a number, add 10, and print result
num = input("\nType a number: ")
result = int(num) + 10
print("\nYour number plus 10 is:", result)

# Ask for the user's age
age = int(input("\nWhat is your age? "))

# Use if/else to give feedback
if age < 18:
    print("\nYou're a minor.")
elif age < 65:
    print("\nYou're an adult.")
else:
    print("\nYou're a senior.")
print("\nThis is your bootcamp logic demo! \n")

for i in range(5):
    print("This runs 5 times!\n")

count = 0
while count < 5:
    print("Counting:", count, "\n")
    count += 1

def greet(name):
    print("Hello,", name,"\n")

greet("Sparsh")  # Try calling the function with your name

def add_numbers(a, b):
    return a + b

result = add_numbers(7, 8)
print("7 + 8 is", result, "\n")

def double(x):
    return x * 2

num = int(input("Enter a number to double: "))
print("\n Doubled value is:", double(num), "\n")