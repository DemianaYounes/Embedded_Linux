#!/usr/bin/python3

#Print Test
print("Full Name:Demiana")
print("Faculty:HTI")

#Variables Test
x=5
print(type(x))  
x="Demiana"
print(type(x))
x=3.5
print(type(x)) 
print(id(x))  #id print address of the variable

#Comma Operator
x,y,z=1,2,3
print(x)
print(y)
print(z)
x,_,z=5,6,7  # (_) to ignore 
print(x)
print(z)

#Task 
num1=10
num2=3
print("Sum="+str(num1+num2))
print("Sub="+str(num1-num2))
print("Div="+str(num1/num2))
print("Mul="+str(num1*num2))

#Data Types
#complex
x=5+6j
print(type(x))
#bool
print(10>9)
print(bool("Demiana"))
print(bool(20))
print(bool(True))
print(1>2)
print(bool(0))
print(bool(False))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool([]))
#List (collection-ordered-mutable)
x=["Demiana",1,6,9]  #Different data type
print(x)
print(type(x))
print(x[0:2]) #Slicing  
print(x[0:4:2]) #jumb by 2
print(x[-1])
#Tuple (collection-ordered-unchangeable(immutable))
x=("Jojo",4,6,"Koko",10,12)
print(x)
print(type(x))
print(x[0])
print(x[2:4]) #Slicing
print(len(x[0]))
#Dictionary (Keys:Values)
Dict={
    "Brand":"Ford",
    "Electric":"False",
    "Year":1964,
    "Colors":["Red","White","Blue"]
}
print(type(Dict))
print(Dict)
print(Dict.keys())
print(Dict.values())
print(Dict["Brand"])
print(len(Dict))
#Set (Unordered-Mutable-Don't allow duplicated value)
settest={"Red",1,"Demiana"}
print(type(settest))
print(settest)
print(len(settest))


#Range
i=0
for i in range(5):
    print(i)
for i in range(0,4,2):
    print(i)

x=list(range(0,10))
print(x)

#Convert string to list
name="Demiana"
print(list(name))

#Input
name=input()
print("My name is "+name)
value=int(input("PLease enter the value: "))  
print("value=",value)
print("value="+str(value))
print(f"value={value}")
print("value="+format(value))


#Arithmetic
x=3
y=2
print(x//y) #Floor

#Membership Operation
print(1 in [1,2,3])  #in
print(5 in [1,2,3])  
print(5 not in [1,2,3])  #not in
#Indentity Operations
a=[10]
b=[10]
print(id(a))
print(id(b))
if a is b:
    print("a is b")
if a==b:
    print("a equal to b")

#If Condition
a=200
b=300
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a and b are equal")
#Shorthan if ..... else
a=300
b=200
print("A") if a>b else print("B")
#Ternary
a=2
b=330
print("A") if a>b else print("=") if a==b else print("B")
#Nested if
x=41
if x>10:
    print("Above ten")
    if x>20:
        print("and also above 20!")
    else:
        print("and also not above 20!")


#Task(2)

#Loop
#While Loop 
i=0
while i<5:
    print(i)
    i+=1
#Break and Continue
i=0
for i in range(0,10):
    if i%2==0:
        break
    print(i,"odd")

for i in range(0,10):
    if i%2==0:
        continue
    print(i,"odd")

#else in for loop
for i in range(0,5):
    print(i)
else:
    print("Finally Finished")

#Shorthand for
[print(i) for i in range(3) if i%2==0]
[print(i) for i in "jojo"]
print()

#Reverse string
name="demiana"
#sloution in c style
for i in range(len(name)):
    print(name[-1-i])
print()
#sloution in Python style
txt=name[::-1]
print(txt)

#Time Now Task
import datetime
now=datetime.datetime.now()
print("Current date and time: ")
print(str(now)[0:-7])

#pyfiglet task
#pip install pyfiglet
#import pyfiglet
#result=pyfiglet.figlet_format("Demiana Younes")
#print(result)

########################################################Task Session1 ########################################################
#Task1
x=[4,4,6,7,4,4,2]
Count_of_Four=x.count(4)
print(f"The number of 4s in the list is:{Count_of_Four}")

#Task2
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels
Letter=input("Enter the letter:")
for i in range(len(Letter)):
    if is_vowel(Letter[i]):
        print(f"{Letter[i]} is vowel") 
    else:
        print(f"{Letter[i]} is not vowel") 
    
#Task3
import os
def access_environment_variables():
    # Access the 'OS' environment variable
    os_env=os.environ.get("OS","Not Defined")
    print(f"OS: {os_env}")
    # Access the 'PATH' environment variable
    path_env=os.environ.get("PATH","Not Defined")
    print(f"PATH: {path_env}")
if __name__=="__main__":
    access_environment_variables()

#Task4
import calendar

def print_calender(year,month):
    try:
        #Print the calendar for the specified month and year
        cal=calendar.TextCalendar()
        print(cal.formatmonth(year,month))
    except Exception as e:
        print(f"An error occured: {e}")

if __name__=="__main__":
    # Input year and month from the user
    try:
        year=int(input("Enter the year (e.g., 2025): "))
        month=int(input("Enter the month (1-12): "))
        if 1<=month<=12:
            print_calender(year,month)
        else:
            print("Invalid month! Please enter a value between 1 and 12.")
    except ValueError:
        print("Invalid input! Please enter numeric values for year and month.")

#Task5
import math

def Calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * radius**2
if __name__=="__main__":
    try:
        radius=float(input("Enter the radius of the circle: "))
        if radius<0:
            print("Radius cannot be negative. Please enter a positive value.")
        else:
            area=Calculate_circle_area(radius)
            print(f"The area of the circle with radius {radius} is: {area:.2f}")
    except ValueError:
        print("Invalid input! Please enter a numeric value for the radius.")



#Task6
from gtts import gTTS
import vlc

# Convert text to speech
myobj = gTTS(text="Good Morning Jojo", lang='en', slow=True)

# Saving the converted audio in a .mp3 file
myobj.save("Welcome.mp3")

# Playing the converted file
p = vlc.MediaPlayer("./Welcome.mp3")
p.play()

# Allow the audio to play for a certain duration before closing the program
while True :
    pass 

