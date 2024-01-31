import datetime  as dt 
pt = dt.datetime.now()   # present time
print(pt.weekday())      # need day 0 -6 = 0 is mon to 6 is sun
print(pt.ctime())        # current time

""" pt = dt.datetime(2021,1,31)   #-->if need any particular date
print(pt)
pt = pt.replace(year=2023,month=11,day=23)   -->Replace Method
print(pt) """


f1  = pt.strftime("%d-%m-%Y,%A")
print(f1)
print(pt.strftime("On %A"))


# if dont know date end like 17th 
x = ""
if pt.strftime("%d") == '01':
    x = 'st'
elif pt.strftime("%d") == '02':
    x = 'nd'
elif pt.strftime("%d") == '03':
    x = 'rd'
elif pt.strftime("%d") == '31':
    x = 'st'
else:
    x = 'th'

print(pt.strftime("%d" + x +" %b %Y"))
print(pt.strftime("at %I:%M: %S %p"))

#print(pt.year)   # only year print(pt.year)

 
""" Date & Time operations
 - Subtract

 EXAMPLE:  
from datetime import date
from datetime import datetime
d1 = date(2023, 12,12)
d2 = date(2022, 12,14)

print(d1 - d2)
dt1 = datetime(2023,11,12,0,0,0)
dt2 = datetime(2022,11,12,12,53,0)
print(dt1 - dt2)

"""

""" 
 Creating timedelta Objects

 from datetime import timedelta

 delta = timedelta(weels=2,days=2.hours=3)
 print(delta)  // multiply also
delta1 = delta * 3 or line by line 
print("Days: ",delta.days)
print("Seconds: ",delta.seconds)
print("Microseconds: ",delta.microseconds)
 OUTPUT:-
 16 days,3:00:00

 Days : 16
 Seconds :10800
 Microseconds:0
 """

