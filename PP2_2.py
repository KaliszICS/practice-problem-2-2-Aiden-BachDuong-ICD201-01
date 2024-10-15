'''
    Lesson: If and Else Assignment
    Author: Aiden
    Date Created: October 15, 2024
    Date Last Modified: October 15, 2024
'''

def q1(): 
  #Write Assignment code here
  num = int(input("Input an integer: "))
  if num == 5:
    print("The number is Five")
  else:
   print("The number is not Five")

def q2(): 
  #Write Assignment code here
  num1 = float(input("Input a number: "))
  if num1 >= 1:
    print("Positive")
  else:
    print("Negative")

def q3(): 
  #Write Assignment code here
  num2 = int(input("Input an integer: "))
  if not num2%2:
    print("Even")
  else:
    print("Odd")

def q4(): 
  #Write Assignment code here
  word = input('Type "Hello": ')
  if word == "Hello":
    print("The word is Hello")
  else:
    print("The word is not Hello")



#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
q4()
'''