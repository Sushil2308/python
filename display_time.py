import datetime, os

class TimeDisplay:
    
    @staticmethod
    def display_time():
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"Current Time: {current_time}")
