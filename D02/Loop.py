# Printing 3 Hello Worlds 
for i in range(3) : 
    print("Hello World")

# Using the i Variable 
for i in range(3) : 
    print(i)

# Using loop with Custom Range and Steps 
for i in range(3, 6) : 
    print(i)

for i in range(1, 8, 3) : 
    print(i)

#  Reverse Loop 
for i in range(8, -3, -1) : 
    print(i)

# Nested Loop 
for i in range(5) : 
    for j in range(3) : 
        print(j, end="")
    print()

# While Loop 
i = 0
while i < 4 : 
    print(i)
    i += 1; 

Number Guesser 
guess = int(input("Guess a number! (1-10): "))
answer = 10
while guess != answer : 
    print("That is the wrong answer")
    guess = int(input("Guess another number! (1-10): "))
print("You guessed the right number!")

# Create a square
for i in range(5) : 
    for j in range(5) : 
        print("*", end="")
    print()


# Coordinates
for i in range(5) : 
    for j in range(5) : 
        print("( " + str(i) + " , " + str(j) + " )", end=" ")
    print()


# Create a custom image 
for i in range(5) : 
    for j in range(5) : 
        if i == j or i + j == 4: 
            print("*", end="")
        else : 
            print(" ", end="")
    print()

# Create another custom image 
n = 10
for i in range(n) : 
    for j in range(n) : 
        if i == 0 or i == n-1 or j == 0 or j == n-1: 
            print("*", end="")
        else : 
            print(" ", end="")
    print()
    
# Create a trapezoid 
# Doesn't work it height > width 
height = 9
width = 30
for i in range(height) : 
    for j in range(width) : 
        if (i + j == height - 1 or i + j == width-1) or ( i == height - 1 and j < abs(width-height)) or ( j >= height - 1 and j < width - 1 and i == 0) : 
            print("*", end="")
        else : 
            print(" ", end="")
    print()