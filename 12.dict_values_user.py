# Getting  keys & values from user
def printPerson(data):
    for k, v in data.items():
        print(k, ":", v)

userdata = {}
e = 1
while e != '0':
    userkey = input("Enter {key} : ")
    uservalue = input("Enter {value} : ")
    userdata[userkey] = uservalue
    e = input("Enter 0 to end or any key to continue adding.....")
    userdata += "{key: <10}: {value}\n"
printPerson(userdata)
    
    