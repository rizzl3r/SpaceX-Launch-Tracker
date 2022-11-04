import datetime
import time
 
# assigned regular string date
date_time ="2022-11-03T23:51:17.663Z"
 
# print regular python date&time
print("date_time =>",date_time)
 
# displaying unix timestamp after conversion
print("unix_timestamp => ",
      (time.mktime(date_time.timetuple())))