# Getting  keys & values from user
def printperson(data):
    hkl = 0
    for kl, vl in data.items():
        if hkl < len(kl):
            hkl = len(kl)
    for k,v in data.items():
        if hkl == len(k):
            print(k, ":", v)
        else:
            space =''
            balance_ln = hkl-len(k)
            for xs in range(balance_ln):
                space += ' '
            print(k + space,':',v)


userdata = {}
e = 1
while e != '0':
    userkey = input("Enter key : ")
    uservalue = input("Enter value : ")
    userdata[userkey] = uservalue
    e = input("Enter 0 to end or any key to continue adding.....")
    
printperson(userdata)
    
    