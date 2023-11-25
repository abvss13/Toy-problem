def convert_to_24_hour(hour, minute, period):
     if period.lower() == "am":
        if hour == 12:
            hour = 0