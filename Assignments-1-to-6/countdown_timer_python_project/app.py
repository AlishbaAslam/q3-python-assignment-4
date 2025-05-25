import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_format = f'{mins:02d}:{secs:02d}'
        print(timer_format, end='\r')  # Print on the same line
        time.sleep(1)
        seconds -= 1

    print("Time's up! \a")  # \a is the beep sound in terminal (may or may not work depending on system)

if __name__ == "__main__":
    try:
        user_input = int(input("Enter the time in seconds for countdown: "))
        countdown_timer(user_input)
    except ValueError:
        print("Please enter a valid integer number of seconds.")