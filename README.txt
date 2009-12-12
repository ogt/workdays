========================================================
Function Definition
========================================================

NETWORKDAYS(start_date,end_date,holidays)

Returns the number of whole working days between start_date and end_date
(inclusive of both start_date and end_date). Working days exclude
weekends and any dates identified in holidays. 

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
complimentary. We have followed to obey excel's conventions as opposed
to come up with our own.  Also start_date has to be less than or equal
to end_date

-------------------------------------------------------

WORKDAY(start_date,days,[holidays])

Returns a number that represents a date that is the indicated number
of working days before or after a date (the starting date). Working
days exclude weekends and any dates identified as holidays.

Start_date is a date that represents the start date.

Days is the number of nonweekend and nonholiday days before or after
start_date. A positive value for days yields a future date; a negative
value yields a past date.

Holidays is an optional list of one or more dates to exclude from
the working calendar, such as state and federal holidays and floating
holidays. The holiday list should not have duplicates.

The function should work almost identically to the corresponding Workday
function of Excel  (Analysis ToolPak)

========================================================
Examples
========================================================

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

