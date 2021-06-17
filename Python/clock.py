HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60


class Clock:
    day_hours = 24
    day_minutes = 60

    def __init__(self, hour, minute):
        self.hour = (hour + minute // MINUTES_PER_HOUR) % HOURS_PER_DAY
        self.minute = minute % MINUTES_PER_HOUR

    def __repr__(self):
        return f'Clock({self.hour:02d}, {self.minute:02d})'

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)