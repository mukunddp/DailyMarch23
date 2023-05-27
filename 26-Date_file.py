import datetime
import time
import calendar
# time stamp
time_stamp = time.time()
# print(time.strftime("%d/%m/%Y, Time: %I:%M:%S %z"))

print(datetime.datetime.fromtimestamp(time_stamp))

print(calendar.calendar(2023,3))