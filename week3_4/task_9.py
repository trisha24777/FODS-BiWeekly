def add_daily_temp(daily_temps, temperature, day_of_week):
    if day_of_week not in daily_temps:
        daily_temps[day_of_week] = temperature
    return daily_temps