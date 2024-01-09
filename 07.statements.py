# If statement
marks = 65
if marks >= 35:
 print("Pass")

# if else
marks = 55
if marks >= 35:
 print("Pass")
else:
 print("Fail")
 
 # elif 
marks = 45
if marks == 35:
  print("Promoted")
elif  marks > 35:
  print("Pass ") 
else:
  print("Fail")


# nested
marks = 85
if marks == 35:
  print("Promoted")
elif  marks > 35:
  print("Pass the exam!") 
  if marks >=75 and marks <= 85:
    print("You got good marks:",marks)
  elif marks >85 and marks <= 95:
    print("You got great marks:",marks)
  elif marks >95 :
    print("You are the best!:",marks)
  else:
    print("You got average marks:",marks) 

else:
  print("Fail",marks)
 
 