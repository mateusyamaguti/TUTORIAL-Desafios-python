# Problem 1059 - Even Numbers
# Source: https://judge.beecrowd.com/

# The problem asks to print all even numbers from 1 to 100 (inclusive).

# Idea:
# 1. Iterate through numbers from 1 to 100
# 2. Check if the number is even (divisible by 2)
# 3. Print the even numbers

# Solution 1

for cont in range(1, 101):
    if (cont % 2) == 0:
        print(cont)


# Solution 2
for i in range(2, 101, 2):
    print(i)