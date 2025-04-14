# Function to get daily temperatures for each day of the week
def get_daily_temps():
    # List of days in a week
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    # Dictionary to store the daily temperatures
    daily_temps = {}

    # Loop through each day in the days list
    for day in days:
        # Continue asking for input until a valid temperature is entered
        while True:
            try:
                # Ask the user to input the average temperature for the current day
                temp_str = input(f"Enter the average temperature for {day}: ")
                
                # Convert the entered string to a float (temperature)
                temperature = float(temp_str)
                
                # Add the day and its corresponding temperature to the dictionary
                daily_temps[day] = temperature
                
                # Exit the loop after a valid temperature is entered
                break
            except ValueError:
                # If the input cannot be converted to a float, show an error message
                print("Invalid temperature. Please enter a numeric value.")
    
    # Return the dictionary containing all the daily temperatures
    return daily_temps

# Call the function to get the temperatures for the week
daily_temps = get_daily_temps()

# Print the dictionary with all the daily temperatures
print(daily_temps)
