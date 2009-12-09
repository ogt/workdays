from datetime import date, timedelta

# started from the code of Casey Webster at
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/ddd39a02644540b7

# Define the weekday mnemonics to match the date.weekday function
(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)

def workdaysub(start_date, end_date, whichdays=(MON,TUE,WED,THU,FRI)):
    '''
    Calculate the number of working days between two dates inclusive
    (start_date <= end_date).

    The actual working days can be set with the optional whichdays
parameter
    (default is MON-FRI)
    '''
    delta_days = (end_date - start_date).days + 1
    full_weeks, extra_days = divmod(delta_days, 7)
    # num_workdays = how many days/week you work * total # of weeks
    num_workdays = (full_weeks + 1) * len(whichdays)
    # subtract out any working days that fall in the 'shortened week'
    for d in range(1, 8 - extra_days):
                if (end_date + timedelta(d)).weekday() in whichdays:
                                num_workdays -= 1
    return num_workdays

def workdayadd(start_date,work_days, whichdays=(MON,TUE,WED,THU,FRI)):
    '''
    Adds to a given date a number of working days 
    2009/12/04 for example is a friday - adding one weekday
    will return 2209/12/07
    >>> workdayadd(date(year=2009,month=12,day=4),1) 
    datetime.date(2009, 12, 7)
    '''
    weeks, days = divmod(work_days,len(whichdays))
    new_date = start_date + timedelta(weeks=weeks)
    for i in range(days):
        while new_date.weekday() not in whichdays:
            new_date += timedelta(days=1)
    return new_date
