
import webbrowser
import validators
import time


def print_prompt():
    print("\nPython Browser Alarm Clock\n")
    print("1 - Enter Youtube URL")
    print("2 - Enter the time for the alarm to go off.")


def get_url():
    user_url = input("\nEnter URL : ")

    if is_youtube(user_url):
        return user_url
    else:
        print("\nNot Youtube URL")
        return get_url()  # Calls itself until valid input.


# Returns duration in seconds.
def calculate_duration(in_hour, in_minutes):
    alarm_duration = ((in_hour * 60) + in_minutes) * 60

    if in_hour >= 0 and in_minutes >= 0:
        return alarm_duration
    else:
        print("\nInvalid Time!")
        return get_time()  # Calls itself until valid input.


def get_time():
    alarm_hour = float(input("\nEnter in how many hours the alarm should go off. : "))
    alarm_minute = float(input("And how many minutes? : "))

    duration = calculate_duration(alarm_hour, alarm_minute)
    return duration


# Checks if the URL input includes a https prefix. If not, one is prepended.
def include_https(in_url):
    if in_url[0:7] != "https://":
        return "https://" + in_url
    else:
        return in_url


# Checks if URL is to youtube
def is_youtube(in_url):
    domain = in_url.split("//")[-1].split("/")[0]

    if domain.lower() == "www.youtube.com" or domain.lower() == "youtube.com":
        return True
    else:
        return False


def open_url(in_url):
    time.sleep(get_time())  # Freezes remaining code from running until time is reached.

    in_url = include_https(in_url)   # Includes https:// prefix if needed.
    is_url = validators.url(in_url)  # Checks if URL is valid. Returns boolean.

    if is_url:
        webbrowser.open(in_url, new=0, autoraise=True)
    else:
        print("Invalid URL")


def run_again():
    user_choice = input("Run Again? (Y/N) : ")

    if user_choice.upper() == "Y":
        return True
    else:
        return False


def main():
    run = True

    while run:
        print_prompt()
        open_url(get_url())
        run = run_again()  # Boolean. Scripts end when false.


main()  # Runs program
