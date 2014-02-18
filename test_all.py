# tests are courtesy of github user @petef4

from datetime import date
from workdays import workday


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
