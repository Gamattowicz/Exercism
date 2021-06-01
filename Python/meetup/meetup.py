from calendar import Calendar, day_name
from datetime import date


def meetup(year, month, week, day_of_week):
    days = [(y, m, d) for y, m, d, wd in Calendar().itermonthdays4(year,month)
            if m == month and day_name[wd] == day_of_week]
    if week == 'teenth':
        for y, m, d in days:
            if 10 < d < 20:
                day = date(y, m, d)
    elif week == 'last':
        day = date(days[-1][0], days[-1][1], days[-1][2])
    else:
        try:
            day_index = int(week[0]) - 1
            day = date(days[day_index][0], days[day_index][1], days[day_index][2])
        except IndexError:
            raise MeetupDayException('Wrong date')

    return day


class MeetupDayException(Exception):
    pass