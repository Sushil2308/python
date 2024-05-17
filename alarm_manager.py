from alarm import Alarm
import datetime
import time


class AlarmManager:
    def __init__(self):
        self.alarms = []
        self.current_day = datetime.datetime.now().strftime('%a')
        self.running = True
    
    def alarm_triggred_check(self):
        while self.running:
            for alarm in self.alarms:
                if alarm.check_alarm_status():
                    self.play_sound()
                    print("Alarm triggered!")
            time.sleep(1)
    
    def create_alarm(self):
        try:
            alarm_time = input("Enter alarm time (HH:MM): ")
            alarm_days = input("Enter days for alarm (e.g., Mon, Tue, Wed): ")
            self.alarms.append(Alarm(alarm_time, alarm_days))
            print("Alarm created successfully!")
        except ValueError:
            print("Invalid time format. Please use HH:MM.")
    
    def snooze_alarm(self):
        alarm_to_delete = int(input("Enter position of alarm to delete: "))
        if len(self.alarms) < alarm_to_delete:
            print("Invalid position.")
            return
        tempAlarm = self.alarms[alarm_to_delete - 1]
        if not tempAlarm.check_alarm_status():
            tempAlarm.snooze_alarm()
    
    def delete_alarm(self):
        alarm_to_delete = int(input("Enter position of alarm to snooze: "))
        if len(self.alarms) < alarm_to_delete:
            print("Invalid position.")
            return
        del self.alarms[alarm_to_delete - 1]
        print("Alarm deleted.")


    def play_sound(self):
        print("Alarm alert!")

    def display_alarms(self):
        if not len(self.alarms):
            print("No alarms set.")
            return
        for i, alarm in enumerate(self.alarms):
            print(f"{i + 1}. Alarm Time: {alarm.time.time()}, Days: {alarm.day}, Snooze Count: {alarm.snooze_count}")
