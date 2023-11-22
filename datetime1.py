from datetime import datetime as dt
import pytz 
# print(dt.now())

# tz_NY = tz.timezone('America/New_York')
# print(dt.now(tz_NY))
  
import calendar
# while 1:
#     year=int(input("Enter year: "))
#     if year<1970:
#         print("Please enter year after 1970")
#     else:
#         break
# while 1:
#     month=int(input("Enter month: "))
#     if month<1 or month>12:
#         print("Please enter month between 1 and 12")
#     else:
#         break

# print(calendar.month(year,month))

# timezones = pytz.all_timezones
# print(timezones)
# for i in range (len(timezones)):
#     zone=timezones[i]
#     tz=pytz.timezone(zone)
#     print(dt.now(tz))
# print(calendar.calendar(2023))
 
#%%
import numpy as np
a=np.array([[1,2],[3,4]])
print(np.sum(a,axis=0))

# %%
