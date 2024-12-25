import datetime
import time

ts = time.time()
# Datetime to string
str_time = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d_%H%M%S - Image List')
print(str_time)
