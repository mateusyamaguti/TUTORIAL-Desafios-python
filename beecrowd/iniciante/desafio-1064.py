# Problem 1064 - Positives and Average
# Source: https://judge.beecrowd.com/

# The problem asks to read 6 floating-point numbers,
# count how many are positive, and calculate the average
# of the positive values.

# Idea:
# 1. Read the 6 numbers into a list
# 2. Filter only the positive numbers using a lambda function
# 3. Count the positive numbers
# 4. Calculate the average of the positive values
# 5. Print the amount and the average

# Solution 1

# Input
numbers = []

for _ in range(6):
    numbers.append(float(input()))

# Processing
positive_numbers = list(filter(lambda x: x > 0, numbers))

# It is also possible to count positives using:
# amount_positive_numbers = sum(map(lambda x: x > 0, numbers))
amount_positive_numbers = len(positive_numbers)

average_positive_numbers = (
    sum(positive_numbers) / amount_positive_numbers
)

# Output
print(f"{amount_positive_numbers} valores positivos")
print(f"{average_positive_numbers:.1f}")