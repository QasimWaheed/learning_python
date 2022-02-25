import calendar
from datetime import datetime

c = calendar.TextCalendar(calendar.SUNDAY)
today = datetime.now()
st = c.formatmonth(today.year, today.month, 0, 0)
print(st)

hc = calendar.HTMLCalendar(calendar.MONDAY)

st = hc.formatmonth(today.year, today.month)
print(st)