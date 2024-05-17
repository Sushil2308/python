from display_time import TimeDisplay
from alarm_manager import AlarmManager
import threading

class AlarmClock:
    def __init__(self):
        self.time_display = TimeDisplay()
        self.alarm_manager = AlarmManager()

    def run(self):
        alarm_check_thread = threading.Thread(target=self.alarm_manager.alarm_triggred_check)
        alarm_check_thread.start()

        while True:
            self.time_display.display_time()
            user_input = input("Enter (c)reate, (s)nooze, (d)elete, (v) Display , or (q)uit: ").lower()
            if user_input == 'c':
                self.alarm_manager.create_alarm()
            elif user_input == 's':
                self.alarm_manager.snooze_alarm()
            elif user_input == 'd':
                self.alarm_manager.delete_alarm()
            elif user_input == 'v':
                self.alarm_manager.display_alarms()
            elif user_input == 'q':
                break
            else:
                print("Invalid input. Please enter c, s, d, or q.")
        alarm_check_thread.join()

if __name__ == "__main__":
    clock = AlarmClock()
    clock.run()
