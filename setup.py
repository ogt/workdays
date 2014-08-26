from distutils.core import setup

setup(name='workdays',
      version='1.4',
      description="Workday date utility functions to extend python's datetime",
      author='Odysseas Tsatalos',
      py_modules=['workdays'],
      url='http://github.com/ogt/workdays',
      download_url = 'http://github.com/ogt/workdays/tarball/master',
      author_email='odysseas@tsatalos.com',
      keywords = ['python', 'datetime', 'workdays', 'excel' ],
      classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
          ],
      long_description = """
    Extend python datetime with excel-like workday addition/subtraction
    functionality:

    NETWORKDAYS(start_date,end_date,holidays)

    Returns the number of whole working days between start_date and
    end_date (inclusive of both start_date and end_date). Working days
    exclude weekends and any dates identified in holidays. Use NETWORKDAYS
    to calculate employee benefits that accrue based on the number of
    days worked during a specific term.

    WORKDAY(start_date,days,[holidays])

    Returns a number that represents a date that is the indicated number
    of working days before or after a date (the starting date). Working
    days exclude weekends and any dates identified as holidays. Use
    WORKDAY to exclude weekends or holidays when you calculate invoice
    due dates, expected delivery times, or the number of days of work
    performed.

    This module has similarities with the BusinessHours module - you may
    want to check it out as well to see which one better fits your needs.
""",
      )

