# Create set to use {}-->curly braces

flowers = {'Lilly','Rose','Jasmine','Lotus'}
print(flowers)

# Diff Data types
n = {"Pranavi",4,True,"Lavanya"}
set = {"Pranavi",4,True,"Pavan",4}  # Don't allow duplicate values
print(set)
print(len(set))
print(len(n))

        # Dictionary
person = {"name":"Pranavi","age":21,"mobile":'741411'}
print(person['name'])                # How to cal values
person ["mobile"] = 74141123         # Change values
person ["frnd"] = "Lavanya"
            # update,Add
person.update({"name":"Sujith"}) 
person.update({"mail":"pranavi143@gmail.com"}) 
    # Remove methods
person.pop("mail")  
person.popitem()  # without key remove value but it remove last value
print(person)

person1 = {'name': 'Sujith', 'age': 21,"lastname":"Kumar", 'mobile': 74141123, 'frnd': 'Lavanya', 'mail': 'pranavi143@gmail.com'}
del person1 ["lastname"]   #use del keyword
# del person1  -->it completly delete when print it shows person1 is not defined
print(person1)

p ={"name":"Pranavi","Hero":"Ram"}
p.clear() # no delete but do empty
print(p)

print(person.keys())   # Only keys will be print
print(person.values())  # Only values