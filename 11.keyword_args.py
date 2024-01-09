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