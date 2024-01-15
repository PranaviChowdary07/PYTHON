# how to print keyarguments in dictionary type
def person(**data):
    for k,v in data.items():
        if k == 'fname' or k == 'lname':     # edit spaces for equal length
            print(k, ' :', v)
        elif k == 'age':
            print(k,'   :', v)
        else:
            print(k,':',v)
person(fname = 'Pranavi',lname = 'Kasthuri',age = 21,mobile =9053456)

# Getting data from user
def person1(**data):
    for k,v in data.items():
        if k == 'firstname':     # edit spaces for equal length
            print(k, '   :', v)
        elif k =='lastname':
            print(k,'    :',v)
        elif k == 'age':
            print(k,'         :', v)
        else:
            print(k,':',v)

e = 1
while e != '0':                                        # allow may user details
    fname =input("Enter first name: ")
    lname =input("Enter last name: ")
    age =input("Enter age: ")
    mobilenum= input("Enter mobile number: ")
    print(' ')                                      # use for line break
    person1(firstname=fname,lastname=lname,age=age,mobilenumber=mobilenum)
    e = input("Enter 0 to exit or any key to continue: ")
    print(' ')


    # Sending Dictionary as an Argument
    




    