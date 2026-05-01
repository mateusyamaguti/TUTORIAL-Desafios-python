# Problem 1060 - Positive Numbers
# Source: https://judge.beecrowd.com/

# The problem asks to read 6 values and count how many of them are positive.

# Idea:
# 1. Read 6 numbers
# 2. Check if each number is greater than zero
# 3. Count how many satisfy the condition
# 4. Print the result

# Solution 1

# Input
count = 0

for _ in range(6):
    value = float(input())

    # Processing
    if value > 0:
        count += 1

# Output
print(f"{count} valores positivos")


# Solution 2

# empty list
even_list = []
odd_list = []

for i in range(0, 6):
    # Processing
    ask = int(input())
    if ask > 0:
        even_list.append(ask)
     
# Output   
print(f"{len(even_list)} valores positivos")
