# Create a dictionary for time units
TIME_UNITS = {
    "day": 86400,  # 24 * 60 * 60
    "hour": 3600,  # 60 * 60
    "minute": 60   # 60
}

# Get the number of seconds from the user
seconds = int(input("Enter a number of seconds (0 - 8640000): "))

# Determine the number of days, hours, minutes and seconds
days, remaining_seconds = divmod(seconds, TIME_UNITS["day"])
hours, remaining_seconds = divmod(remaining_seconds, TIME_UNITS["hour"])
minutes, seconds = divmod(remaining_seconds, TIME_UNITS["minute"])

# Determine the correct word for days
if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

# Format the result with leading zeros for hours, minutes, and seconds
time_format = f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"

# Output the result
print(time_format)
