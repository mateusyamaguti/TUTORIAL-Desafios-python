# Problem 1061 - Event Time
# Source: https://judge.beecrowd.com/

# The problem asks to calculate the duration of an event given its
# start and end day/time. The result must be displayed in days,
# hours, minutes, and seconds.

# Idea:
# 1. Read the initial and final day/time
# 2. Convert both timestamps to total seconds
# 3. Calculate the difference in seconds
# 4. Convert the difference back to days, hours, minutes, and seconds
# 5. Print the result

# Solution 1

# Input
initial_day = int(input().split()[1])

i_hours, i_minutes, i_seconds = map(int, input().split(":"))

final_day = int(input().split()[1])

f_hours, f_minutes, f_seconds = map(int, input().split(":"))

# Processing
initial_time_in_seconds = (
    initial_day * 86400 +
    i_hours * 3600 +
    i_minutes * 60 +
    i_seconds
)

final_time_in_seconds = (
    final_day * 86400 +
    f_hours * 3600 +
    f_minutes * 60 +
    f_seconds
)

time_difference = final_time_in_seconds - initial_time_in_seconds

days = time_difference // 86400
hours = (time_difference % 86400) // 3600
minutes = (time_difference % 3600) // 60
seconds = time_difference % 60

# Output
print(f"{days} dia(s)")
print(f"{hours} hora(s)")
print(f"{minutes} minuto(s)")
print(f"{seconds} segundo(s)")


# Solution 2
# Input
initial_day = int(input().split()[1])
i_hours, i_minutes, i_seconds = map(int, input().split(":"))

final_day = int(input().split()[1])
f_hours, f_minutes, f_seconds = map(int, input().split(":"))

# Processing
initial = (
    initial_day * 86400 +
    i_hours * 3600 +
    i_minutes * 60 +
    i_seconds
)

final = (
    final_day * 86400 +
    f_hours * 3600 +
    f_minutes * 60 +
    f_seconds
)

time_difference = final - initial

days, remainder = divmod(time_difference, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

# Output
print(f"{days} dia(s)")
print(f"{hours} hora(s)")
print(f"{minutes} minuto(s)")
print(f"{seconds} segundo(s)")