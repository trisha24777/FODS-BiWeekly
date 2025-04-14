# Function to add a daily temperature to the dictionary
def add_daily_temp(daily_temps, temperature, day_of_week):
    # Check if the day_of_week is not already in the dictionary
    if day_of_week not in daily_temps:
        # If the day is not in the dictionary, add the temperature for that day
        daily_temps[day_of_week] = temperature
    # Return the updated dictionary of daily temperatures
    return daily_temps

# Initialize an empty dictionary to store the temperatures for each day
daily_temps = {}

# Add temperature for Monday (temperature = 25)
add_daily_temp(daily_temps, 25, "Monday")

# Attempt to add temperature again for Monday, but it will not overwrite because it's already there
add_daily_temp(daily_temps, 25, "Monday")

# Print the daily temperatures dictionary to show the result
print(daily_temps)
