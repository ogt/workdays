from datetime import date, timedelta

# started from the code of Casey Webster at
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/ddd39a02644540b7

# Define the weekday mnemonics to match the date.weekday function
(MON, TUE, WED, THU, FRI, SAT, SUN) = range(7)
weekends=(SAT,SUN)


def networkdays(start_date, end_date, holidays=[]):
    '''
    NETWORKDAYS(start_date,end_date,holidays)

    Returns the number of whole working days between start_date and
    end_date (inclusive of both start_date and end_date). Working days
    exclude weekends and any dates identified in holidays. Use NETWORKDAYS
    to calculate employee benefits that accrue based on the number of
    days worked during a specific term.

    Start_date is a date that represents the start date.

    End_date is a date that represents the end date.

    Holidays is an optional list of one or more dates to exclude from
    the working calendar, such as state and federal holidays and floating
    holidays. The holiday list should not have duplicates.

    The function should work almost identically to the corresponding
    Networkdays function of Excel  (Analysis ToolPak)

    Note that just like in excel workday and networks days aren't
    "complimentary"  i..e if wdays = networkdays(d1,d2) you *cannot*
    infer that workday(d1,wdays) = d2 given that networkdays is returning
    the # of working days inclusive of d1 and d2. Excel apparently has
    chosen to facilitate common use cases and not to make the functions
    complimentary. We have followed to obey excel's conventions as
    opposed to come up with our own.
    Also start_date has to be less than or equal to end_date
    '''
    delta_days = (end_date - start_date).days + 1
    full_weeks, extra_days = divmod(delta_days, 7)
    # num_workdays = how many days/week you work * total # of weeks
    num_workdays = (full_weeks + 1) * (7 - len(weekends))
    # subtract out any working days that fall in the 'shortened week'
    for d in range(1, 8 - extra_days):
        if (end_date + timedelta(d)).weekday() not in weekends:
             num_workdays -= 1
    # skip holidays that fall on weekends
    holidays =  [x for x in holidays if x.weekday() not in weekends]
    # subtract out any holidays 
    for d in holidays:
        if d >= start_date and d <= end_date:
            num_workdays -= 1
    return num_workdays

def _in_between(a,b,x):
    #return cmp(a,x) * cmp(x,b) > 0
    return a <= x and x <= b or b <= x and x <= a


def workday(start_date,days, holidays=[]):
    '''
    WORKDAY(start_date,days,[holidays])

    Returns a number that represents a date that is the indicated number
    of working days before or after a date (the starting date). Working
    days exclude weekends and any dates identified as holidays. Use
    WORKDAY to exclude weekends or holidays when you calculate invoice
    due dates, expected delivery times, or the number of days of work
    performed.

    Start_date is a date that represents the start date.

    Days is the number of nonweekend and nonholiday days before or
    after start_date. A positive value for days yields a future date;
    a negative value yields a past date.

    Holidays is an optional list of one or more dates to exclude from
    the working calendar, such as state and federal holidays and floating
    holidays. The holiday list should not have duplicates.

    The function should work almost identically to the corresponding
    Workday function of Excel  (Analysis ToolPak)
    
    '''
    full_weeks, extra_days = divmod(days,7 - len(weekends))
    new_date = start_date + timedelta(weeks=full_weeks)
    for i in range(extra_days):
        new_date += timedelta(days=1)
        while new_date.weekday() in weekends:
            new_date += timedelta(days=1)
    delta = timedelta(days=1 * cmp(days,0))
    # skip holidays that fall on weekends
    holidays =  [x for x in holidays if x.weekday() not in weekends ]
    holidays =  [x for x in holidays if x <> start_date ]
    for d in sorted(holidays, reverse = (days < 0)):
        # if d in between start and current push it out one working day
        if _in_between(start_date, new_date, d):
            new_date += delta
            while new_date.weekday() in weekends:
                new_date += delta
    return new_date


'''
Examples

>>> workday(date(year=2009,month=12,day=25),1, [ date(year=2009,month=12,day=25)
] )
datetime.date(2009, 12, 28)
>>> workday(date(year=2009,month=12,day=25),1, [ date(year=2009,month=12,day=26)
] )
datetime.date(2009, 12, 28)
>>> workday(date(year=2009,month=12,day=25),1, [ date(year=2009,month=12,day=28)
] )
datetime.date(2009, 12, 29)
>>> workday(date(year=2009,month=12,day=29),-1, [ date(year=2009,month=12,day=25
)] )
datetime.date(2009, 12, 28)
>>> workday(date(year=2009,month=12,day=28),-1, [ date(year=2009,month=12,day=25
)] )
datetime.date(2009, 12, 24)
>>> networkdays(date(2009, 12, 24),date(2009, 12, 28))
3
>>> networkdays(date(2009, 12, 24),date(2009, 12, 28), [ date(year=2009,month=12
,day=25)] )
2
>>> networkdays(date(2009, 12, 25),date(2009, 12, 28), [ date(year=2009,month=12
,day=25)] )
1
>>> networkdays(date(2009, 12, 25),date(2009, 12, 27), [ date(year=2009,month=12
,day=25)] )
0
>>> 
'''
