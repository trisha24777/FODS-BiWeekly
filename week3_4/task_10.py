def get_daily_temps():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    daily_temps = {}
    for day in days:
        while True:
            try:
                temp_str = input(f"Enter the average temperature for {day}: ")
                temperature = float(temp_str)
                daily_temps[day] = temperature
                break
            except ValueError:
                print("Invalid temperature. Please enter a numeric value.")
    return daily_temps
