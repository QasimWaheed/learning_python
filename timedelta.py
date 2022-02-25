from dataclasses import replace
from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta


now = datetime.now()

print("one year from now it will be:", str(now + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be " + str(now + timedelta(days=2, weeks=3)))

today = date.today()

afd = date(today.year, 4, 1)

if afd < today:
    print("April Fool's day already went by %d days ago" %((today-afd).days))
    afd = afd.replace(year = today.year+1)

time_to_afd = afd-today
print("It's just ", time_to_afd.days, "days until April Fool's Day")  