# Function to convert time from 12-hour format to 24-hour format
def convert_to_24_hour(hour, minute, time):
    # Check if the given time is in the evening ("pm") and not 12:00 pm
    if time == "pm" and hour != 12:
        # If yes, add 12 to the hour to convert to 24-hour format
        hour += 12
    # Check if the given time is in the morning ("am") and it's 12:00 am
    elif time == "am" and hour == 12:
        # If yes, set hour to 0 to convert to 24-hour format
        hour = 0
    
    # Return the time in 24-hour format as a formatted string
    return f"{hour:02}{minute:02}"

# Example usage of the function with 12:30 am and 12:30 pm
print(convert_to_24_hour(12, 30, "am"))  
print(convert_to_24_hour(12, 30, "pm"))
