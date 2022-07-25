
## Objective of the function --
'''
Write a function named add_time that takes in two required parameters and one optional parameter:

a start time in the 12-hour clock format (ending in AM or PM)
a duration time that indicates the number of hours and minutes
(optional) a starting day of the week, case insensitive
The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later,
it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week 
of the result. The day of the week in the output should appear after the time and before the number of days later.
'''

def add_time(time, duration, day=None):

    dur_in_mins = duration_convert(duration)
    pm = False

    # Convert time to 24-hour format, then into minutes for addition

    t_split = time.split(':')
    hour = int(t_split[0])
    mins = int(t_split[1][:-3])
    days_count = 0
    #print(mins)
    if 'PM' in time:
        hour = hour + 12

    start_time = (hour * 60) + mins
    new_time = start_time + dur_in_mins
    #print(new_time)

    new_hour = new_time // 60
    new_mins = new_time % 60
    if new_hour > 24:
        days_count = new_hour // 24
        new_hour = new_hour % 24

    if new_hour > 12:
        pm = True
        new_hour = new_hour - 12

    new_time_mins = int(new_hour)*60 + int(new_mins)
    #print(new_time_mins)

    if new_time_mins >= 720:
        pm = True

    if new_hour == 0:
        new_hour = 12
        pm = False

    if pm:
        time_print = f'{str(new_hour)}:{str(new_mins).rjust(2, "0")} PM'

    else:
        time_print = f'{str(new_hour)}:{str(new_mins).rjust(2, "0")} AM'

    #print(time_print)
    #print(days_count)

    if days_count != 0 and day == None:
        if days_count == 1:
            print(f'{time_print} (next day)')

        else:
            print(f'{time_print} ({days_count} days later)')

    elif days_count != 0 and day != None:

        new_day = day_calc(days_count, day.lower())
        if days_count == 1:
            print(f'{time_print}, {new_day} (next day)')

        else:
            print(f'{time_print}, {new_day} ({days_count} days later)')

    elif days_count == 0 and day != None:
        print(f'{time_print}, {day.lower().capitalize()}')
    
    else:
        print(f'{time_print}')

def duration_convert(duration):

    hour_mins = duration.split(':')
    print(hour_mins)

    #print(f'Duration variables: {hour_mins}')

    hours = int(hour_mins[0])
    mins = int(hour_mins[1])
    time_to_add = (hours * 60) + mins # All times to be added in minutes
    #print(f'Time for add in mins: {time_to_add}')

    return time_to_add

def day_calc(days_count, day):

    day_dict = {
        'monday':1,
        'tuesday':2,
        'wednesday':3,
        'thursday':4,
        'friday':5,
        'saturday':6,
        'sunday':7
    }

    day_sum = days_count + day_dict[day]
    day_int = day_sum % 7

    for k, v in day_dict.items():
        if v == day_int:
            new_day = k.capitalize()

    return new_day

def main():
    add_time("3:00 PM", "3:10")

if __name__ == '__main__':
    main()
