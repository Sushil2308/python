import datetime
from datetime import timedelta

class Alarm:
    def __init__(self, time, day, snooze_count=0):
        self.time = datetime.datetime.strptime(time,'%H:%M')
        time = time.split(':')
        self.ctime = self.multiply_time(int(time[0]), int(time[1]))
        self.day = day
        self.snooze_count = snooze_count

    def multiply_time(self, hour:int, minute:int)->int:
        return int(hour) * 60 + int(minute)


    def check_alarm_status(self):
        current_time = datetime.datetime.now()
        if self.day == datetime.datetime.now().strftime('%a') and self.ctime <= self.multiply_time(current_time.hour, current_time.minute):
            return True
        return False
 
    def snooze_alarm_time(self):
        if self.snooze_count < 3:
            self.snooze_count += 1
            self.ctime += 5
            self.time = self.time + timedelta(minutes=5)
            print(f"Alarm snoozed. Next alert in 5 minutes ({self.snooze_count}/3 snoozes used).")
            return True
        else:
            print("Maximum snooze limit reached. Alarm will not snooze again.")
            return False

 

 