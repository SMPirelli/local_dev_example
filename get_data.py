import datetime as dt

def add_numbers(num_one, num_two):
    return num_one + num_two

def get_time_string():
    time_now = dt.datetime.now()
    time_string = dt.datetime.strftime(time_now, "%Y-%m-%d %H:%M:%S")

    return time_string


