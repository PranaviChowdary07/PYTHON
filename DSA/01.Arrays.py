import array as arr

# defining array
a = arr.array('d',[2,4.6,6.4])     #syntax : arr.array("datatype",[])
# Add the element
a.append(5.5)
# Extend the list
a.extend([3.5,2.2,1.1])
# Remove element
a.pop()   # It removes last element in list, but particular elemnt we use index "a.pop(2)""
print(a)