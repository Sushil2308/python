from display_time import TimeDisplay
from alarm_manager import AlarmManager
import threading

class AlarmClock:
    def __init__(self):
        self.time_display = TimeDisplay()
        self.alarm_manager = AlarmManager()
        self.runnung_alarm = True

    def run(self):
        # Create a thread to check for triggered alarms
        # That Will triggered the alarm in background
        alarm_check_thread = threading.Thread(target=self.alarm_manager.alarm_triggred_check)
        alarm_check_thread.start()
        try:
            # Main loop to get user input for create alarm , set snooze  and see alarms and can quit any alarm
            while self.runnung_alarm:
                self.time_display.display_time()
                user_input = input("Enter (c)reate, (s)nooze, (d)elete, (v) Display , or (q)uit: ").lower()
                if user_input == 'c':
                    # Create alarm
                    self.alarm_manager.create_alarm()
                elif user_input == 's':
                    #Snooze alarm
                    self.alarm_manager.snooze_alarm()
                elif user_input == 'd':
                    # Delete alarm
                    self.alarm_manager.delete_alarm()
                elif user_input == 'v':
                    # Display alarms
                    self.alarm_manager.display_alarms()
                elif user_input == 'q':
                    # Quit the program
                    self.alarm_manager.running = False
                    self.runnung_alarm = False
                else:
                    print("Invalid input. Please enter c, s, d, or q.")
        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting...")
            alarm_check_thread.join()
            self.alarm_manager.running = False
            self.runnung_alarm = False
            del self.alarm_manager
            del self.time_display
            exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Have a nice day!")
            alarm_check_thread.join()
            self.alarm_manager.running = False
            self.runnung_alarm = False
            del self.alarm_manager
            del self.time_display
            exit(0)

if __name__ == "__main__":
    clock = AlarmClock()
    clock.run()
