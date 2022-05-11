"""
started from the code of Casey Webster at
http://groups.google.com/group/comp.lang.python/browse_thread/thread/ddd39a02644540b7

"""

import datetime
from datetime import timedelta
from typing import List, Tuple

# Define the weekday mnemonics to match the date.weekday function
(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)

# Define default weekends, but allow this to be overridden at the function level
# in case someone only, for example, only has a 4-day workweek.
default_weekends = (SAT, SUN)


def networkdays(start_date: datetime.date,
                end_date: datetime.date,
                holidays: List[datetime.date] = None,
                weekends: Tuple[int] = default_weekends):
    """
    For each day in the range, if the day is not a weekend and not a holiday, add it to the count

    :param start_date: The first date in the range
    :type start_date: datetime.date
    :param end_date: The end date of the period
    :type end_date: datetime.date
    :param holidays: a list of dates (as datetime.date or datetime.datetime objects) to exclude from the set of valid
    business days
    :type holidays: List[datetime.date]
    :param weekends: A tuple of integers representing the days of the week that are not considered work days. The default is
    (5, 6), which means that Saturday and Sunday are not considered work days
    :type weekends: Tuple[int]
    :return: The number of working days between two dates.
    """
    delta_days = (end_date - start_date).days + 1
    full_weeks, extra_days = divmod(delta_days, 7)
    # num_workdays = how many days/week you work * total # of weeks
    num_workdays = (full_weeks + 1) * (7 - len(weekends))
    # subtract out any working days that fall in the 'shortened week'
    for d in range(1, 8 - extra_days):
        if (end_date + timedelta(d)).weekday() not in weekends:
            num_workdays -= 1
    if holidays:
        # skip holidays that fall on weekends
        holidays = [x for x in holidays if x.weekday() not in weekends]
        # subtract out any holidays
        for d in holidays:
            if start_date <= d <= end_date:
                num_workdays -= 1
    return num_workdays


def workday(start_date: datetime.date, days: int = 0, holidays: List[datetime.date] = None,
            weekends=default_weekends):
    """
    If the start date is a weekend, it will keep subtracting days until it is not a weekend.

    The function takes in a start date, a number of days, a list of holidays, and a list of weekends. The default weekends
    are Saturday and Sunday

    :param start_date: The date to start from
    :type start_date: datetime.date
    :param days: The number of days to add or subtract from the start date, defaults to 0 (optional)
    :param holidays: a list of dates that are holidays
    :type holidays: List[datetime.date]
    :param weekends: A list of integers representing the days of the week that are weekends. The default is [5, 6], which
    means Saturday and Sunday
    :return: the date of the next workday.
    """

    if days == 0:
        return start_date
    if days > 0 and start_date.weekday() in weekends:
        # If the start date is a weekend, it will keep subtracting days until it is not a weekend.
        while start_date.weekday() in weekends:
            start_date -= timedelta(days=1)
    elif days < 0:
        # If the start date is a weekend, it will keep subtracting days until it is not a weekend.
        while start_date.weekday() in weekends:
            start_date += timedelta(days=1)
    full_weeks, extra_days = divmod(days, 7 - len(weekends))
    new_date: datetime.date = start_date + timedelta(weeks=full_weeks)
    for i in range(extra_days):
        new_date += timedelta(days=1)
        while new_date.weekday() in weekends:
            new_date += timedelta(days=1)
    # to account for days=0 case
    while new_date.weekday() in weekends:
        new_date += timedelta(days=1)

    # avoid this if no holidays
    if holidays:

        def cmp(a, b) -> int:
            return (a > b) - (a < b)

        def _in_between(a, b, x) -> bool:
            return a <= x <= b or b <= x <= a

        delta = timedelta(days=1 * cmp(days, 0))
        # skip holidays that fall on weekends
        holidays = [x for x in holidays if x.weekday() not in weekends]
        holidays = [x for x in holidays if x != start_date]

        for d in sorted(holidays, reverse=(days < 0)):
            # if d in between start and current push it out one working day
            if _in_between(start_date, new_date, d):
                new_date += delta
                while new_date.weekday() in weekends:
                    new_date += delta
    return new_date
