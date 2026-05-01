# Problem 1052 - Month
# Source: https://judge.beecrowd.com/

# The problem asks to convert an integer (1 to 12)
# into the corresponding month name in English.

# Idea:
# 1. Read the month number
# 2. Map the number to the month name
# 3. Print the result

# Solution 1

# Input
mes = int(input())

# Processing
meses_dict = {1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"}

# Output
print(meses_dict[mes])