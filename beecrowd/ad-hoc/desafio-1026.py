# Problem 1026 - To Carry or not to Carry
# Source: https://judge.beecrowd.com/

# The problem asks to compute the bitwise XOR
# between two unsigned integers.

# Idea:
# 1. Read two integers
# 2. Apply the XOR operator (^)
# 3. Print the result

# Solution 1

# Input
a, b = map(int, input().split())

# Processing
result = a ^ b

# Output
print(result)
