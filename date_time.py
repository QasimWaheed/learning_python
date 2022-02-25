from datetime import datetime
from datetime import date

# date object
todayDateTime = datetime.now()
print(todayDateTime.date())
todayDate = date.today()
print(todayDate)
# datetime object 
print(todayDateTime.now())

# time object
print(todayDateTime.time())

# current year
print(todayDateTime.strftime("Current Year is: %Y"))
print(todayDateTime.strftime("Current Year is: %y"))

# current day string format
print(todayDateTime.strftime("Today day is: %A"))
print(todayDateTime.strftime("Today day is: %a"))

# current month string format
print(todayDateTime.strftime("Current month is: %B"))
print(todayDateTime.strftime("Current month is: %b"))

# current date
print(todayDateTime.strftime("Today date is: %D"))
print(todayDateTime.strftime("Today date is: %d"))

# local date and time
print(todayDateTime.strftime("Current date and time is: %c"))
# local date
print(todayDateTime.strftime("Current date is: %x"))
# local time
print(todayDateTime.strftime("Current time is: %X"))
# Time formating
print(todayDateTime.strftime("%I:%M:%S %p"))
print(todayDateTime.strftime("%H:%M"))