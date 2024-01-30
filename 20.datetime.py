import datetime  as dt 
pt = dt.datetime.now()   # present time
#pt = dt.datetime(2021,1,31)   -->if need any particular date


f1  = pt.strftime("%d-%m-%Y,%A")
print(f1)
print(pt.strftime("On %A"))


# if dont no date end like 17th 
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