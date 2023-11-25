def convert_to_24_hour(hour, minute, period):
    # Check if it's morning or afternoon (AM or PM)
    if period.lower() == "am":
        # If it's morning and the hour is 12, change it to 0
        if hour == 12:
            hour = 0
    else:
        # If it's afternoon and not 12 PM, add 12 to the hour
        if hour != 12:
            hour += 12

    # Combine the hour and minute and return as a 24-hour time string
    return f"{hour:02d}{minute:02d}"

# Example: Convert 8:30 AM to 24-hour format
result = convert_to_24_hour(8, 30, 'am')
print(result)
