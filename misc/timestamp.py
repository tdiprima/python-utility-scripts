# Converts the current timestamp into a string in the format 'YYYYMMDD_HHMMSS - Image List' and prints it.
import datetime
import time

ts = time.time()
# Datetime to string
str_time = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S - Image List')
print(str_time)
