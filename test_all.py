# tests are courtesy of github user @petef4

from datetime import date
from workdays import workday
from workdays import networkdays


def test_monday():
    assert workday(date(2014, 2, 17), -1) == date(2014, 2, 14)
    assert workday(date(2014, 2, 17), 0) == date(2014, 2, 17)
    assert workday(date(2014, 2, 17), 1) == date(2014, 2, 18)
    assert workday(date(2014, 2, 17), 2) == date(2014, 2, 19)
    assert workday(date(2014, 2, 17), 3) == date(2014, 2, 20)
    assert workday(date(2014, 2, 17), 4) == date(2014, 2, 21)

    assert workday(date(2014, 2, 17), 5) == date(2014, 2, 24)
    assert workday(date(2014, 2, 17), 6) == date(2014, 2, 25)


def test_friday():
    assert workday(date(2014, 2, 21), -1) == date(2014, 2, 20)
    assert workday(date(2014, 2, 21), 0) == date(2014, 2, 21)

    assert workday(date(2014, 2, 21), 1) == date(2014, 2, 24)
    assert workday(date(2014, 2, 21), 2) == date(2014, 2, 25)
    assert workday(date(2014, 2, 21), 3) == date(2014, 2, 26)
    assert workday(date(2014, 2, 21), 4) == date(2014, 2, 27)
    assert workday(date(2014, 2, 21), 5) == date(2014, 2, 28)

    assert workday(date(2014, 2, 21), 6) == date(2014, 3, 3)


def test_saturday():
    assert workday(date(2014, 2, 22), -1) == date(2014, 2, 21)
    assert workday(date(2014, 2, 22), 0) == date(2014, 2, 22)
    assert workday(date(2014, 2, 22), 1) == date(2014, 2, 24)
    assert workday(date(2014, 2, 22), 2) == date(2014, 2, 25)
    assert workday(date(2014, 2, 22), 3) == date(2014, 2, 26)
    assert workday(date(2014, 2, 22), 4) == date(2014, 2, 27)
    assert workday(date(2014, 2, 22), 5) == date(2014, 2, 28)

    assert workday(date(2014, 2, 22), 6) == date(2014, 3, 3)


def test_workday():
    holidays = [date(2015, 9, 7)]
    weekends = (0, 5, 6)

    # test 0 days (so that it act the same as Excel)
    assert workday(date(2015, 8, 23)) == date(2015, 8, 23)
    assert workday(date(2015, 8, 23), weekends=weekends) == date(2015, 8, 23)

    # test with non-zero day on weekend
    assert workday(date(2015, 8, 23), days=1, weekends=weekends) == \
           date(2015, 8, 25)

    # test with holiday
    assert workday(date(2015, 9, 4), days=1, holidays=holidays) == \
           date(2015, 9, 8)

    # test non-zero workday solo, with holidays, with weekends, and both
    assert workday(date(2015, 8, 24), 10) == date(2015, 9, 7)
    assert workday(date(2015, 8, 25), 10, weekends=weekends) == \
           date(2015, 9, 10)
    assert workday(date(2015, 8, 24), 10, holidays=holidays) == \
           date(2015, 9, 8)
    assert workday(date(2015, 8, 25), 10, holidays=holidays,
                   weekends=weekends) == date(2015, 9, 10)


def test_networkdays():
    # test standard networkdays with no holidays or modified weekend
    assert networkdays(date(2015, 8, 1), date(2015, 9, 30), holidays=[]) == 43

    # test with USA's Labor Day
    holidays = [date(2015, 9, 7)]
    assert networkdays(date(2015, 8, 1), date(2015, 9, 30),
                       holidays=holidays) == 42

    # test with short work week (Friday's off as well)
    weekends = (4, 5, 6)
    assert networkdays(date(2015, 8, 1), date(2015, 9, 30), holidays=[],
                       weekends=weekends) == 35

    # test with holidays and short work week
    weekends = (4, 5, 6)
    assert networkdays(date(2015, 8, 1), date(2015, 9, 30), holidays=holidays,
                       weekends=weekends) == 34

    # test with overlapping holiday and weekend
    weekends = (0, 5, 6)
    assert networkdays(date(2015, 8, 1), date(2015, 9, 30), holidays=holidays,
                       weekends=weekends) == 34
