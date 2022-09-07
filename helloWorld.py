print("Hello World! I am learning python!")

if 1>0:
    print("One is greater") #Standard indentation

if 5<10:
  print('10 is greater than 5') #less indentation

#You have to use the same number of spaces in the same block of code, otherwise Python will give you an error:
if 0<1:
    print('0 is less than 1')
    #print('Enter a bigger value') - this works
        #print('indentation error expected') #IndentationError: unexpected indent

##Multiline comment can be achieved by using multi-line string(three quotes). This will work if the string is not assigned to a variable. Else it won't

'''
This is a comment
written in
more than just one line
'''

#Python variable does not have a command to declare

name = "Anatu Green"
print(name)

#Variables do not need to be declared with any particular type, and can even change type after they have been set.

x = 12
x ="Twelve"
print(x) #X has been changed from number to string

#You can declare a variable with a type by CASTING

y = str("1000")
a = int(12)
print(y)
print(a)

#Get the type of y and a

print(type(y))
print(type(a))

#You can select a specific path of your code and click the run button (in VScode, top right play button) to run just that code

#Variables are case-sensitive

b = 100
B = 200
print(B)
print(b)

"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)

"""

'''
Python variables that have multiple words can be defined named using camelCase, PascalCase or snake_Case
'''

#Whith python, you can assign different values to different variables in a single line:

c, d, e = 'cee', 4, 2*2,

print(c) #cee
print(d) #4
print(e) #4

#Just like we do destructuring in javascript, we do unpacking in py

anatu = ['Green', 1993, '175cm']

anatu_name, anatu_DOB, anatu_height = anatu

print(anatu_name, anatu_DOB, anatu_height) #This also shows that you can print multiple things to the console at onnce

# Output Variables

say = "Python is awesome!"
print(say)

e = 'Today'
f = ' is'
g = ' beautiful'
h = e+f+g
print(h) #Today is beautiful. This is concatenation of strings in js

#Printing a string plus a number givves error
#print("Hello" + 1) #TypeError: can only concatenate str (not "int") to str

#But you can print different variables at once using comma to separate them. See line 81

#GLOBAL VARIABLES: These are variables created outside a function and therefore can be used anywhere in the code. eg:

myCity = 'Lagos'

def myFunction():
    print(myCity)

myFunction()

def _myCityMessage():
    print("My city is called" + ' ' + myCity)

_myCityMessage()

#If a global variable and a local variable (variable created inside a function) have same name, they will operate as two separate things but obviously the variable inside the function will be the preferred one for that function

def anotherFunc():
    myCity = 'Jos'
    print(myCity)

anotherFunc()

#You can also use the 'global' keyword to create a global variable inside a function so that it can be used inside it and outside

def globalEg():
    global myJob
    myJob = "Software engineer"
    print(myJob)

globalEg()

def myJobMessage():
    print("I love my job as a " + myJob)

myJobMessage() #I love my job as a Software engineer

#You can change the value of a global variabled inside a function

def change():
    global myJob
    myJob = 'Teacher'
    print(myJob)

change() #Teacher

#You can assign the same value to multiple variables

myFood = hisFood = herFood = "Plantain chips"

print(myFood) #Plantain chips
print(hisFood) #Plantain chips
print(herFood) #Plantain chips

print(type(myFood)) #<class 'str'>

# Data types in python include str, int, complex, float, list, tuple, range. dict, set, fronzenset, bool, bytes, bytearray, memoryview, nonetype
#In Python, the data type is set when you assign a value to a variable:

#You can specify the data type of a variable through casting, eg:

i = str('1')
j = int(100)
print(type(i), type(j)) #<class 'str'> <class 'int'>

#PYTHON NUMBERS: they are int, float and complex

k = 1233456889
l = -3459
m =0.34556
n= 1j
o = 23e2 #e for power of 10

print(type(k), type(l), type(m), type(n), type(o)) #<class 'int'> <class 'int'> <class 'float'> <class 'complex'> <class 'float'>

#Convert from one type to another: You can convert from one type to another using the float(), int() and complex() methods

p = float(k)
q = int(m)
r = complex(k)

print(p, q, r) # 1233456889.0 0 (1233456889+0j)

#Note: You cannot convert complex numbers into another number type:

#s = int(n)
#print(s) #TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'


#PYTHON RANDOM NUMBERS: You can import random as a built-in module in python to use and generate randome numbers

from ast import arg
from cgi import print_arguments
from copy import copy
from ctypes import addressof
from glob import glob
from itertools import count
from pprint import pprint
import random
from struct import calcsize
from telnetlib import PRAGMA_HEARTBEAT
import this
from turtle import Terminator, pen

print(random.randrange(1, 9))

#PYTHONG CASTING: You can use casting to convert one data type to another or to specify the type. eg:

s = str(1)
t = int("1")
u = float(2)
w = int(1.9)
print(type(s)) # 1 is supposed to be an int but now a string because of casting
print(type(t)) # int even though "1" is really a string originally
print(type(u)) #Now float even though 2 is int
print(w) # 1 - anything from the  dot is removed to create an int
# Let us try doing a calculation with s

# print(s - 2) #TypeError: unsupported operand type(s) for -: 'str' and 'int'
print(t - 1) # 0


# STRINGS

#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#'hello' is the same as "hello".
#You can display string literal in print

print("Hello Green")

#Assign a string to a variable

greet = 'Hello Green, How are you today?'
print(greet)

#You can assign a multiline string by using three quotes at the beginning and the end of the long string. Can be single quotes or double (''' or """)

greet2 = """
Today is a good day
to learn python.
This is a poem of tech!
"""

print(greet2)

# A string is an array. Remember that like every other prog lang, an array counting begins with zero. You can access the characters of a string like in normal array.
#Python does not have character data type.

string1 = 'Welcom to class!'
print(string1[1]) #m - This is get the second character of the str

#You can also get the characters in a range of indexes

print(string1[1:5]) #elco. The 5th char that constitutes the end of the range is not included thus the four characters

#Looping through a string: You can loop through a string to get each character of it in a different line:

for x in string1:
    print(x)

#To get the length of a string use len()  function

print(len(string1)) # Remember that in string1, the spaces are counted as chars too. So the answer is 16

#Check a string. You can check if a character or word is present in a word or sentence simply by using 'in' keyword

print('class' in string1) # True. Because this is a boolean issue

#Using the above in an if statement

if "class" in string1:
    print("Yea! Class is in the sentence") #Yea! Class is in the sentence

# CHECK IF NOT: We can also check to see if a character or word or phrase is in a string

txt = "I am learning Python and it is awesome so far!"
print("Python" not in txt) #false because Python is in the string
print("Python" in txt) #true
#Note that in the above, if you use python with small letter p, the first result will be true while the second will be false

if "Python" not in txt:
    print("The user is not learning Python")
else:
    print("The user is learning Python!")

print("Why not learn python") if "Python" not in txt else print("Bravo and goodluck in Py!") #If else shortcut

#Slicing a string: You can slice a string to return the characters that fall in a range. Use the array rule. first char is at 0 position

sliceTxt = txt[2:10]
print(sliceTxt) #am learn

#Slice to the end: By leaving out the end index, the string will be sliced to the end.
print(txt[2:]) #am learning Python and it is awesome so far!
#Slice to the beginning: Just the opposite of the above
print(txt[: 20]) #I am learning Python

#Negative indexing: You can use the minus sign to start the slicing from the end of the string

print(txt[-10:])

#We can also just cut from a point to another point negatively using neg indexing

print(txt[-10:-5])

#MODIFYING STRINGS IN PYTHON: Python has built-in methods for modifying strings

story = " Mary had a little LAMB! "

#to upper case
print(story.upper()) # MARY HAD A LITTLE LAMB!

#to lower case
print(story.lower()) # mary had a little lamb!

#Remove whitespace
print(story.strip()) #Mary had a little LAMB! Note that the space before and after the story has been removed. See output

#Replace string
print(story.replace("Mary", "John")) #John had a little LAMB!
print(story.replace("a", "o"))

#Convert everything to lower case then remove all a's
removeA = story.lower()
removeA = removeA.replace('a', 'o')
print(removeA) # mory hod o little lomb!

#Split a string based on  a specific separator: this will return an array with the separated parts of the string
print(story.split(' ')) #['', 'Mary', 'had', 'a', 'little', 'LAMB!', '']: Here we use empty space as the separator, we can also use comma or anything else, even a word

story2 = "we are good people, ain't we?"
print(story2.split(',')) #['We are good people', " ain't we?"]

print(story2.capitalize()) #This capitalizes the first char in a string

story2_Capital = story2.upper() #WE ARE GOOD PEOPLE, AIN'T WE?

print(story2_Capital) #This capitalizes the first char in a string

#Casefold will convert the string to lowercase like witj lower method
print(story2_Capital.casefold()) #we are good people, ain't we?

#Centralize the string. The center() method takes a required arguments that determines the space that the string will take up and then center in. You can also define the character to add in the empty spaces. This will be the second arguments in the center()
print(story2.center(100, '!')) #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!we are good people, ain't we?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# String Concatenation: This is addint two or more strings together using + operator

txt2 = "Hello"
txt3 = "Green"
txt4 ="Sup!"
concatTxt = txt2 + ' ' + txt3 + ' '+ txt4
print(concatTxt) #Hello Green Sup!. Note how I added spaces between them strings

#FORMATING IN PYTHON: Recall that normally you cannot add string and numbers. But with format() methode you can add a number to a string, you will have to add the placeholder where the number will be first using curly brackets {}

#Format can accept unlimited number of arguments but the placeholders will then be replaced in the order of the arguments put in the format

myAge =  29
expYears = 3
myIntro = "My name is Anatu and I am {} years old"
print(myIntro.format(myAge)) #My name is Anatu and I am 29 years old
myIntro2 = "My name is Anatu and I am {} years old. I have been programming for {} years now. But in total I have been in tech for about {} years so far"
print(myIntro2.format(29, expYears, 10)) # My name is Anatu and I am 29 years old. I have been programming for 3 years now. But in total I have been in tech for about 10 years so far

#You can use indexing to arrage where which number will be placed. This will override the normal way they are arranged consecutively

quantity = 12*2
quality_score = 90.2
price = 150
statement = "I am going to by {0} pieces of gold at ${2} each. The rated quality is {1}"
print(statement.format(quantity, quality_score, price)) #I am going to by 12 pieces of gold at $150 each. The rated quality is 90.2. Note that the index numbering follows how I arranged the variabes inside the format method, not how they in the order of their declaration

#Note that formating can be done with strings, floats and other data types as the variables. Even mathematical expressions to get the results printed out

#ESCAPE CHARACTER: The escape character is the \ followed by the illegal character you want to inser. Eg, normally putting a single or doouble quote inside a string that is created with single or double quote will give error unless escaped
# print("Hello world, he said. He just said "Hello World" ") #SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Hello world, he said. He just said \"Hello World\" ") #Hello world, he said. He just said "Hello World"

#Other examples of escape characters
print('It\'s going to be okay') #It's going to be okay
print("This's a \\ (backslash)") # A single backslash appears. Well, writing a single backslash does not really give an error
#New line in string
print("The escape character is the \ followed by the illegal \n character you want to inser. Eg, normally putting a single or doouble quote \n inside a string that is created with single or double quote will give error unless escaped")

#Carriage return
print("Welcome\rHome") #Welcome and home will be in two separate lines

#Tab space
print("Welcome\tHome")  #Welcome	Home

#Backspace: erases one character backwards (backspace)
print("Welcome \bWorld") #Welcome World

#Octal value: A backslash followed by three integers will give the octal value in string
txt_octal = "\142\145\154\154\157"
print(txt_octal) #bello

#Hex value: \ followed by x and a hex number will give the hex value
_hex = "\x48\x65\x6c\x6c\x6f"
print(_hex) #Hello

#Form field
print("Hello\fHello")

# PYTHON STRING METHODS: These are built in methods that work with strings in python. They include:
sampleText = "hello everyone! Welcome to Python!"
sampleTextCaps = sampleText.upper()
print(sampleTextCaps)
#Capitalize: Change the first character to a capital. If there are capitals in the body of the string, they get converted to small letters. If an number is the first char, nothing happens to it
print(sampleText.capitalize()) #Hello everyone! welcome to python!
someCaps = "Hello GREENBRAIN. How ARE You"
print(someCaps.capitalize()) #Hello greenbrain. how are you


#Casefold: Ccnverts string to small letters. It is more aggressive than the lower() method. It will convert more characters into lower case and will find more matches when two strings are compared.
print(sampleTextCaps.casefold())  #hello everyone! welcome to python!

#center(): We already discused this in line 328 or thereabouts

#count(): This method returns the number of times a specified value appears in a given string. Note that this is case-sensitive
#The syntax of count() is string.count(value, start, end). Value is a compulsory string to search for while start and end are optional and indicate the starting and ending positions of the search
print(sampleTextCaps.count('E')) #6
print(sampleTextCaps.count('e')) #0
print(sampleTextCaps.count('PYTHON')) #1
print(sampleText.count("e", 1, 10)) #3 search from position 1 to 10

#encode(): This will make a UTF-8 encoding of the given text. UTF-* is the default encoding when none is specified
txt_With_SpecialChar = "H€ll©"
print(txt_With_SpecialChar.encode()) #b'H\xe2\x82\xacll\xc2\xa9'

#endswith(): A boolean method to return true if a string ends with specified value. Syntax: string.endswith(value, start, end) just like in count
print("Hello".endswith('o')) #True
print("Hello".endswith('e')) #false

if "Hello".endswith("o"):
    print("Wow") #wow

inspire ='We are the world'
print(inspire.endswith("We", 3, 10)) #false: because starting to search at position 3 and ending at position 10, there is no "We"

#String expandTabs() method: This allows you to determin the amount of spacing after a tab. Sytax: string.expandtabs(tabsize)

toTab= "Hello\tEarth\tMy\tBeoved\tMother"
print(toTab.expandtabs(5)) #Hello     Earth     My   Beoved    Mother
print(toTab.expandtabs(2)) #Hello Earth My  Beoved  Mother

#Find(): This looks for the first occurence of a given value and returns the position where it is located. sytax: string.find(value, start, end). Start and end are optional or else, the search will begin at the beginning. -1 will return if the value searched for is not seen

hello = "Hello people of the world!"
print(hello.find('e')) #1
print("Anaturuchi".find('i', 2, 8)) #-1

#Format: This will format the specific value given to it and inserts it into the placeholder given in a string

toFormat = "Hello Green, can you wire me ${}?"
print(toFormat.format(20))
print(len(toFormat))

#NOTE:Python string formats will be continued later so as o count into our study. For now, let us continue with the normal study flow

#TOPIC:PYTHON BOOLEANS: Booleans represent true or false. You can evaluate any expression to return whether it is true or false
# We can use the various comparison operators including ==, >, <, <=, >=, != etc

print(len("Anaturuchi") > 20) #False
print(type("Hello") == int) #false
print(10 > 9) # True
print(1>=2) #False
print(1<=2) #True
print(1!=2) #True

#We can use if statements to get something done if a condition is met or not

if 10>90:
    print("Yes!")
else:
    print("No!") #No

#The above has a shortcut:

print("Yes Sir") if 10>20 else print("Damn!")

#NOTE: bool() function allows you to return whether a value is true or false

print(bool(20))
print(bool(-20))
print(bool(0))
print(bool("Hello"))

#Truety and falsy works in these ways in python:
# ALmost all values and datat types are true, except empty ones and zeros.
# Any string is true unless empty.
# Any number is true unless zero.
# Lists, tuple, dict, set are all true except empty ones.
# Remember that a string containing space only is not same as an empty one

print(bool(['Ana', 'Turu']))
print(bool(''))
print(bool(('Hello', "Mama")))
print(bool({1, 2, 3}))

#False values are empty data types, false, 0 and None:

print(bool(False), bool(None), bool(0), bool(''), bool(()), bool([]), bool({})) #False False False False False False False

#Falso is also returned when the donder method __len__ is used to return zero in an object
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print(myobj)
print(bool(myobj))

# A function can also be created to return boolean values

def myFunc():
    return True

print(myFunc())

#You can execute code based on the Boolean answer of a function:

if myFunc():
    print("Yes!!!")
else:
    print("No!!!")

#There are many built-in functions in python that return booleans: eg is isinstance()

print(isinstance(1, str)) #False. The function checks if the first argument has the data type specified using the second argument which has to be a datatype

#TOPIC: Python Operators

#These are used to perform operations using variables and values
# +, - , /, *,

#Python operators are divided into these groups:
'''
Arithemethic
Assignment
Comparison
Logical
Identity
Membership
Bitwise

'''

#Arithmetic operators include: +, -, /, *, % (modulo),** (exponentiation), // (Floor division)
#Modulo returns the remainder of dividing the int or float at the right side by the int or float at the left of it
print(100%1000)
#Exponentiation raises the number or float at the left by the numer or float at the right
print(15**2) #15 raised to power 2
#Floor division: // : This will return the result of a division rounded off to the nearest whole number
print(10.5//10) #1.0
print(11/6) #1.8333333333333333
print(11//6) #1

# Python Assignment Operators: These are used to assign values to variables. They include
# =, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=

num = 10
num+=12 #ie: num=num + 12 this aplies to other below
print(num)
num-=12
print(num)
num*=2
print(num)
num/=2
print(num)
#etc
num**=2
print(num)

num2 = 10
num2&=4 #Bitwise AND operator Read here: https://www.geeksforgeeks.org/python-bitwise-operators/#Bitwise_AND_operator
print(num2) #0
num2 |=10 #Bitwise or
print(num2) #10

num3 = 10
num3^=2 #Bitwise xor ^ operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.

print(num3) #8

# Python Comparison Operators: Are used to compare values.
# == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), <=(less than or equal to)


#Python Logical Operators: Logical operators are used to combine conditional statements:

xx = 10
yy = 5

print(xx>yy and yy<xx) #True: and Returns True if both statements are true
print(xx > yy or yy > xx) #True : or Returns True if one of the statements is true
print(not(xx>yy and yy<xx)) #False: The not will reverse the boolean that is returned inside it after an operation or comparison
print(not(xx>yy)) #False

#Python Identity Operators: is and is not: These are used to check if objects are the same. Not if they are equal, but if they are actually the same objects

aa = ['Ana', 'Green']
bb = ['Ana', 'Green']
cc = bb

print(aa is bb) #False. Because 'is' is not the same thing as == which checks if the two objects are of the same contents in same order
print(cc is bb) #True. Because cc is same as bb having been assigned bb. So both them are occupying same space in the memory
print(aa is not bb) #True. Opposite of is. See the reason of the above case

# Python Membership Operators: 'in' and 'not in' Use to check if a specified value or values appear in an object
print('Ana' in aa) #True
print('Aba' in aa) #False
print('Green' not in aa) # False because Green is in aa

# SUBTOPIC: Pytgon Bitwise operators: These are used to compare binary numbers. SO they first convert the given numners into binary then compare and then operates based on the results: & (AND), | (OR), ^ (XOR), ~ (NOT), << (Zero fill left shift), >> (Signed right shift)


#TOPIC: Python Lists. List are just like Arrays in Javascript. They are used to store a collection of data like Tuple, set and dictionary. They are created using square brackets
fruitList = ["Apple", "Banana", "Watermelon" ]
print(fruitList)

#List items are ordered and zero-indexed. They are changeable and allow duplicate values. We can chnage , add, remove items from list. Lists can have multiple items of the same value. This does not matter because each item is indexed specially

fruitList += ['Orange', "Apple"]
print(fruitList) #['Apple', 'Banana', 'Watermelon', 'Orange', 'Apple']
print(fruitList[0], fruitList[4]) #Apple Apple

#We can see the length of the list (how many items in it)
print(len(fruitList)) #5

#List can contain any data type and can contain multiple datat types

list1 = ['abc', 123, 20.3, True, False, fruitList] #['abc', 123, 20.3, True, False, ['Apple', 'Banana', 'Watermelon', 'Orange', 'Apple']]
print(list1)

print(type(list1)) #<class 'list'> #Python lists have the type list

#List constructor: list() can be used to create a list

constList = list(('Peter', 'Gregory', 'Obi'))
print(constList) #['Peter', 'Gregory', 'Obi']

repeat = ["I will be wealthy"]
repeat *=10
print(repeat)

#Python list is one of the 4 data collection data types in pythn. The remaining are:
# Tuple: Ordered, unchangeable and allows dulicates. made of circular brackets.
# Set: A collection that is unordered, unchangeable and unindexed. No duplicate members allowed. Items can be added or removed wherever you want
# Dictionary: ordered and changeable. No duplicates. Python 3.6 and earlier, dict was unordered

#SUBTOPIC:  Accessing List Items: the first item has index of zero

myValuables = ["Phone", "Laptop", "Solar"]
print(myValuables[0]) #Phone

# Items can also be accessed through Negative indexing that is starting from the end. In this case, the last element has index of -1 and so on
print(myValuables[-1]) #Solar

#A range of items can be accessed. A new list will be returned with the elements in the range
print(myValuables[0:2]) #['Phone', 'Laptop']. Note that the item represented by the upper index selected will not be shown. So 0:2 means items 0 and 1, item 2 not inclusive. The search will start at index 0 (included) and end at index 2 (not included).

# Leave out the first value in the range to start from the beginning.
print(myValuables[:2]) #['Phone', 'Laptop']

#Leave out the end value to tage the range to the end

print(myValuables[0:]) #['Phone', 'Laptop', 'Solar']

#Negative index can be specified to start the search at the end. The index item at the right will not be returned

print(myValuables[0:-1])#['Phone', 'Laptop']

#CHeck if an item exists: This is a bool function and we use in

print("Phone" in myValuables) #True
print("Whale" in myValuables) #False

#SUBTOPIC:Changing List Items: A single item or range of items can be changes

fruitList = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruitList[0] = 'berry'
print(fruitList) #['berry', 'banana', 'cherry', 'orange', 'kiwi', 'mango']

#A range of items can be changed: You indicate a range and assign to a new list according to how you want the item to be replaced
print(fruitList[0:3])
fruitList[0:3] = ['Lemon', 'Tigernut', 'Blueberry']
print(fruitList) #['Lemon', 'Tigernut', 'Blueberry', 'orange', 'kiwi', 'mango'] The first three get replaced
#If more items are inserted than are replaced, the additional items will take the places of the other items before them while the other items will then follow
thisList = ["Joe", "Tony", "Mike", "Green", "Hilary"]
print(thisList[4]) #Hilary is currently in position 4
thisList[1:3] = ['Obama', 'Trump', 'Clinton', 'COnfuscius']
print(thisList) #['Joe', 'Obama', 'Trump', 'Clinton', 'COnfuscius', 'Green', 'Hilary']
print(thisList[4]) # COnfuscius is now in 4. Green and hilary are now 5 and 6

#If you add less items than replaced, the others will move accordingly

thisList2 = ["Joe", "Tony", "Mike", "Green", "Hilary"]
thisList2[0:3] = ["Saddam", 'Obasanjo']
print(thisList2) #['Saddam', 'Obasanjo', 'Green', 'Hilary'] - This shows that Mike has now been deleted because its range was taken but nothing was put in it.

#SUBTOPIC: Insert New Item: We can insert items in specific indexes without deleting existing items using insert() method

thisList2.insert(0, "Bidden",)
print(thisList2) #['Bidden', 'Saddam', 'Obasanjo', 'Green', 'Hilary']

#SUBTOPIC: ADDING LIST ITEMS: The methods to add items to a list include append() - to the end, insert() - to any valid index, extend() - Add from other lists. We have already looked at insert

stationary = ['Pen', 'Pencil', 'Compass', 'Books']
stationary.append('Plainsheets')
print(stationary) #['Pen', 'Pencil', 'Compass', 'Books', 'Plainsheets']
stationary.remove(stationary[4]) #- ['Pen', 'Pencil', 'Compass', 'Books']- Just removing the last added item
print(stationary)

otherItems = ['Schoolbag', 'Food flask'] #New list to entend with
stationary.extend(otherItems)
print(stationary) #['Pen', 'Pencil', 'Compass', 'Books', 'Schoolbag', 'Food flask'] - The elements are added to the end of the list

#The extende() can add other iterables like sets, dict, tuple etc, not just lists

#SUBTOPIC: Removing List Items: The methods used are remove(), pop(), del, clear()

#remove() will remove the item at the specified item, identified by itself, not by index or you can make it remove by index by feeding it with the argument that contains the list with index
stationary.remove('Pen')
print(stationary) #['Pencil', 'Compass', 'Books', 'Schoolbag', 'Food flask']
#OR:
stationary.remove(stationary[0]) #Remove by index
print(stationary) #['Compass', 'Books', 'Schoolbag', 'Food flask']

#pop() is the simpler way to remove a specific index. It accepts one argument

stationary.pop(0)
print(stationary) # ['Books', 'Schoolbag', 'Food flask']

#pop() will remove the last item on the list if no index is given

#del will remove the specified index also

del stationary[0]
print(stationary) #['Schoolbag', 'Food flask']
newItems = ['Pen', 'Pencil', 'Compass', 'Books']

stationary.extend(newItems)
print(stationary) #['Schoolbag', 'Food flask', 'Pen', 'Pencil', 'Compass', 'Books']

#del can also delete the entire list

listToDel = ["Abc","Def",'Ghi']
print(listToDel)
del listToDel
# print(listToDel) #NameError: name 'listToDel' is not defined

listToClear = ["Abc","Def",'Ghi']
#clear() will clear the lsit
listToClear.clear()
print(listToClear) # []

#SUBTOPIC: LOOPING LISTS: We can loop through lists to end up with some results, like getting the individual items one after another

listToLoop = [100,200,300,400,500]
print(listToLoop)

#Using for loop
for x in listToLoop:
    print(x) #Each item gets a new line. We can even perform actions to the loop:
    #print(x * 2) for example

#We can also loop through a list using the indexs
listToLoop2 = ["Nurse", 'Doc', "Welder", 'Engineer']
for i in range(len(listToLoop2)): #You are telling python to loop through the listToLoop2 by looking at the range of indexes that make up the list. If i (the iterator) is within the range of 0 to 3, then the following action will happen
    print(listToLoop2[i])

#Using While Loop: You can use while loop to loop a list by giving the iterator a value. Then giving the condition that as long as is true, the loop will keep happening. Let us use listToLoop2 again
listToLoop3 = ["Nurse", 'Doc', "Welder", 'Engineer']
i = 0 #Starting at the beginning of the list indexes
while i<len(listToLoop3): #Since list is zero-indexed but the length of the loop is not, the 4 is the answer and the loop with count from 0-3
    print(listToLoop3[i])
    i+=1 #At each loop, increment i by 1, if not i will remain 1 and this will cause an infinite loop

#List comprehension can give us shorter syntax:


#SUBTOPIC: List comprehension: This gives us a very short syntax for looping lists. eg:
[print(x) for x in listToLoop3] #Gives us the loop result that we used 2 lines in previous for loop or 4 lines in while loop for

#Let us even do something funnier, say we have a list of  names and we just want to filter out names that have the a specific letter and  traditionally we will do this:

listOfNames = ["Gerard", "Matthew", 'Mike', "Nelson", "Job"]
for x in listOfNames:
    if 'a' in x:
        print(x) #Gerard and Matthew got printed in two diff lines

#List comprehension says: We can use shorter syntax to achieve creating of new list with selected items from another list. For example, to create a new list from an existing one based on certain criteria,

namesComp = [x for x in listOfNames if 'a' in x]
print(namesComp) # ['Gerard', 'Matthew'] - filtered the listOfNames based on which items contain 'a'.

#This is the normal way to do same thing we just did with newComp:

namesCompNorm = []

for x in listOfNames:
    if 'a' in x:
        namesCompNorm.append(x)
        print(namesCompNorm)

#Note that the new list is a new one and the old list remains unchanged and valid.

#The condition that we used in our list comprehension is not compulsory to use. But when it is used, it evaluates and filters out the items that are true to the condition.

proLangs = ['Python', 'Java', 'Javascript', 'Golang']
newProg = [x for x in proLangs]
print(newProg)

#You can use the range() function to create an iterable like a list, tuple, set etc

newIterable = [x for x in range(12)]
print(newIterable) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#Adding a condiition

newIterable = [x for x in range(20) if x >= 10]
print(newIterable) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19] - Note that since it is a range the last item in the range is not included, if I wanted 20 to be included I would have made the 5range to stop at 21.

#The expression in a list compression is the first part which is the current item but will also be the result of the operation. X is our expression above but it can also be mani0pulated to give certain outcome

newProg = [x.upper() for x in proLangs] #This iterates over the lst and returns the x in capital letters
print(newProg)  #['PYTHON', 'JAVA', 'JAVASCRIPT', 'GOLANG']

#We can aalso return whatever we want after the looping
print(['Hello' for x in proLangs]) #['Hello', 'Hello', 'Hello', 'Hello']

#We can also apply a condition that checks for something and if the condition is not met another thing is returned

newListProg = [x if x!='Python' else "HTML" for x in proLangs]
print(newListProg) #['HTML', 'Java', 'Javascript', 'Golang'] - We just told pythin to loop through the list and return everything that is not Python and replace what is python with HTML

#SUBTOPIC: SORTING LISTS: Lists cn be sorted in a vaiety of ways.

phoneMakers = ["Xiaomi", 'Tecno', 'Infinix', 'Acer', 'Samsung', 'Huawei', 'Poco' ]
phoneMakers.sort()
#Sorting alphabetically: This is the default when list is sorted with the sort() method. Also, the items that start with capital letters are sorted  first so if you mix capital and small lettered items and then sort, it might lead to unexpectes results.
print(phoneMakers) # ['Acer', 'Huawei', 'Infinix', 'Poco', 'Samsung', 'Tecno', 'Xiaomi']
#Note that you have to sort outside before printing in this case
phoneMakers2=['A', 'a', 'bb', 'BB', 'c', 'C']
phoneMakers2.sort()
print(phoneMakers2) #['A', 'BB', 'C', 'a', 'bb', 'c'] the ones whose names started with capitals have been sorted first then forllowed by the others.

#Sorting in reverse order:
phoneMakersCopy = phoneMakers.copy()
phoneMakersCopy.sort(reverse=True)
print(phoneMakersCopy) #['Xiaomi', 'Tecno', 'Samsung', 'Poco', 'Infinix', 'Huawei', 'Acer']

#sorting integers

intList = [1,3, 7, 5, 6, 9, 20, 10]
intList.sort()
print(intList) #[1, 3, 5, 6, 7, 9, 10, 20]
intList.sort(reverse=True)
print(intList) #[20, 10, 9, 7, 6, 5, 3, 1]

#Customize sorting function: You can customize your own function and use it in sorting the function and

def myFunct(n):
    return abs(n-10) #We will use this as the argument to sort the list based on how close the numbers are to 10

intList.sort(key = myFunct)
print(intList) #[10, 9, 7, 6, 5, 3, 1, 20]

#SUBTOPIC:Sorting wihout following case sensitiveNESS: Normally the sorting of strings will follow case, sorting the strings that start with cpitals first. But this cn be overridden
sortNoCase = ['A', 'a', 'bb', 'BB', 'c', 'C']
sortNoCase.sort(key=str.lower)
print(sortNoCase) #['A', 'a', 'bb', 'BB', 'c', 'C'] - You can use a better usecase for this like list of food and names etc

#SUBTOPIC: Sorting list in rever order without following the order of first alphabets. You just want to reverse the list according to how it was ordered:

fruitList2 = ["banana", "Orange", "Kiwi", "cherry"]
fruitList2.reverse()
print(fruitList2) #['cherry', 'Kiwi', 'Orange', 'banana']

#SUBTOPIC: Copy Lists: You can make a copy of a list, not refrence so that the new list that copy is not affected by the changes in the copied list

originalList = ["Adaora", 'Chika', "Chidinma", "Mercy", 'Ekene']
print(originalList) #['Adaora', 'Chidi', 'Chidinma', 'Mercy', 'Ekene']
refList=originalList
print(refList) #['Adaora', 'Chidi', 'Chidinma', 'Mercy', 'Ekene']
#The contents of refList will always change according to whatever happens to originalList. But we can make complete copies of originalList that does not mirror it automtically. We use copy() method or we use the list constructor list()

copyOriginal = originalList.copy()
print(copyOriginal) #['Adaora', 'Chika', 'Chidinma', 'Mercy', 'Ekene']
copyByConst = list(originalList) #['Adaora', 'Chika', 'Chidinma', 'Mercy', 'Ekene']

#SUBTOPIC: Joining Lists: We can join lists with + operator

joinedList = copyOriginal + copyByConst
print(joinedList) #['Adaora', 'Chika', 'Chidinma', 'Mercy', 'Ekene', 'Adaora', 'Chika', 'Chidinma', 'Mercy', 'Ekene']

'''
#Lists cannot be multiplied:
multipliedList = [2,4,6] * [2,5,9]
print(multipliedList) #TypeError: can't multiply sequence by non-int of type 'list'
'''

#Lists can also be joined by looping through the existing list and appending each item to the new list. List can also be joined by extending. entend() is originall;y used to add items from one list to another

newList = [20, 39, 450]
for x in originalList:
    newList.append(x)

print(newList) #[20, 39, 450, 'Adaora', 'Chika', 'Chidinma', 'Mercy', 'Ekene']

newList2 = [25, 100, 419]
newList2.extend(newList)
print(newList2) # [25, 100, 419, 20, 39, 450, 'Adaora', 'Chika', 'Chidinma', 'Mercy', 'Ekene']

print(newList2.count('Mercy')) #1

#SUBTOPIC: List Mehodes: They include:
# count(), extend(), list(), copy(), sort(), remove(), pop(), append(), clear(), index(), insert(), reverse()

#TOPIC: TUPLE
#Tuple is another of the four collecton data types in pythoon. It is made of round brackets. It can contain a combination of data types. Tuple cannot be changed, ie no direct addition, removal or replacedment of items. Tuples are indexed from zero so they allow duplicates. Tuple is ordered.\
#Since tuples are ordered, they can allow duplicate values
#type() method can be used to get the data type of tuple just like others

thisTuple = ('Tuple', 'Set', 'List', 'Dictionary', 'Set', 2, True)
print(thisTuple) #('Tuple', 'Set', 'List', 'Dictionary', 'Set', 2, True)

#if a tuple contains just one item, a comma has to come after it if not python will not see it as a tuple but as a string.
singleTuple = ('Single')
print(type(singleTuple))  #<class 'str'>
singleTuple = ('Single',)
print(type(singleTuple))  #<class 'tuple'>

#Finmd the length of tuple:
print(len(thisTuple)) #5

#tuple() constructor can be used to create topple but recall that the items will be encircled with douple brackets

tupleConstr = tuple(("Hello", 123, 'World'))
print(tupleConstr) #('Hello', 123, 'World')
print(type(tupleConstr)) #<class 'tuple'>

#SUBTOPIC: ACCESSING TUPLE ITEMS: They can be accessed the same way we access list items by referring to their index positions or range

print(tupleConstr[0]) # Hello
print(tupleConstr[0:2]) #('Hello', 123)

#negative indexing to access items: Thids is to start at the end of the list to make the access. The item at the end in this case is index -1
print(tupleConstr[-1]) #'World'
#-tive index range
print(tupleConstr[-3:-1]) #('Hello', 123) #Started -3 (included) and ended at -1(excluded)

#SUBTOPIC: Range of Indexes. You can filter a range of indexes

fruitTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruitTuple[0:4]) #('apple', 'banana', 'cherry', 'orange') - The search began at 0 9included) anad stops at 4 (excluded)

print(fruitTuple[3:]) #('orange', 'kiwi', 'melon', 'mango')
#Started at the fourth item(inclusive) an ended at the last item in the list
print(fruitTuple[:3]) # - started at the beginning of the list and stoped at the fourth (non included)

print(fruitTuple[-3:-1]) #Sarch from the end of the tuple. In this case, from the 3rd last item (included) to the first last item (excluded). Recall that  in negative indexing, the first item from the extreme of the list or tuple haas the position -1.

#In the issue of ranges, just recall that the index on the left will be included bu the index in the right will not be incluluded

print(fruitTuple[0:3]) #('apple', 'banana', 'cherry')
print(fruitTuple[1:4]) #('banana', 'cherry', 'orange')
print(fruitTuple[3:5]) #('orange', 'kiwi')

#SUBTOPIC: Checking if an item exists in a tuple is done using the in keyword

print('kiwi' in fruitTuple) # True

if 'mango' in fruitTuple:
    print("Hurray, you can et mango from the bassket!") #Hurray, you can et mango from the bassket!

#TOPIC: Updating tuples: Tuples cannot be directly changed and items cannot be directly removed., We can however achieve this by converting the tuple to list, editing it and then converting back to tuple

tupleToChange = ("apple", 1000, "cherry", 300, "kiwi", "melon", "mango")
converterList = list(tupleToChange)
print(converterList) # ['apple', 1000, 'cherry', 300, 'kiwi', 'melon', 'mango'] - converted
converterList[0] = 'Orange'  #changing the list
tupleToChange=tuple(converterList) # Converting back to tuple
print(tupleToChange) #('Orange', 1000, 'cherry', 300, 'kiwi', 'melon', 'mango')

#SUBTOPIC: Add items to tuple: Recall that we cannot directly update tuple so we have to use one of these ways to add items to tuple:

#Convert then append
convert2 = list(tupleToChange)
convert2.append('Ben')
tupleToChange = tuple(convert2)
print(tupleToChange) #('Orange', 1000, 'cherry', 300, 'kiwi', 'melon', 'mango', 'Ben')

#Tuples can be added using the +.

tuple01 = (12, 34, 56, 78, 78)
tuple02 = ("vegie", "Groundnut")
addition = tuple01 + tuple02
print(addition) #(12, 34, 56, 78, 78, 'vegie', 'Groundnut')

#We can convert tuple to list to enable us to remove an item just like we did with appending

convert3 = list(addition)
convert3.pop() #Remove the last item or give this an index to pop
print(convert3) #[12, 34, 56, 78, 78, 'vegie']
convert3.remove(78) #Remove 78 specifically
addition = tuple(convert3)
print(addition) #(12, 34, 56, 78, 'vegie') - The first occurence of 78 removed

'''
#Completey delete tuple

del addition
print(addition) #NameError: name 'addition' is not defined
'''
#TOPIC: Unpack Tuples: This will bring out the individual items of a tuple and assign them to the specified variables. It is like destructuring in Js
#Creating a tuple is packing a tuple

pack = ('Cat', "Rat", 'Bat', 'Brat')
one, two, three, four = pack
# or (one, two, three, four) = pack
print(one) #Cat
print(four) #Brat

pack2 = ('Terminator', 'Tenat', 'Metime')
'''
Trying to unpack with less number of variables than the hunber of items to unpack will give error unless * asterisk is used to make a list from the excess items.
(mov1, mov2) = pack2
print(mov1) # ValueError: too many values to unpack (expected 2)
'''
(mov1, *otherMovs) = pack2
print(mov1, otherMovs) #Terminator ['Tenat', 'Metime']

#If you add the * to a variable that is not the last variable on you unpacking list, then it will become the list containing the items untill the number of items left will individually match the number of variable left to the right and those will be assigned accordingly

pack3 = (1,2,3,4,5,6,7,8,9,0)
(one, two, *others, secondoTheLast, last) = pack3
print(one, two) #1 2
print(others) #[3, 4, 5, 6, 7, 8]
print(secondoTheLast, last) #9,0

#TOPIC: LOOPING THROPUGH TUPLES: This is done using the for and while loops

pack4 = (100,200,300,400,500,600,70.0,800,)

for x in pack4:
    if x> 100:
        print(x)
'''
200
300
400
500
600
800
'''
#You can also use while loops

l = 0
while l<len(pack4):
    print(pack4[l])
    l+=1 #increment by 1 after each loop
#the above gives us the same result as seen in the previous loop

#We can decise to loop via the range of indexes

print(range(len(pack4))) # range(0,8) understanding what hapens when you invoke range .

for i in range(len(pack4)):
   print(pack4[i])

'''
100
200
300
400
500
600
70.0
800
'''
#Joining Tuples: You can join two0 or more tuples toget5her using the = operator:

tuple_1 = ('Tuple',)
tuple_2 = ('Set', False)
tuple_3 = (True, 25)
all_tuples = tuple_1 + tuple_2 + tuple_3
print(all_tuples) # ('Tuple', 'Set', False, True, 25)

#Multiply Tuple: Yopu can multiple the items in a tuple to get a tuple with multiple items

multi_tuple = (tuple_1 *2)+(tuple_2 *3)
print(multi_tuple) # ('Tuple', 'Tuple', 'Set', False, 'Set', False, 'Set', False)

#Tuple Methods: They are two: count(), returns the number of occurences of a specified item; and index(), returned the position where an items that is searched in a tuple is located (the first occurence)
print(multi_tuple.count('Set')) # 3
print(multi_tuple.index(False)) # 3

#NOTE: I finished the lesson on Tuples 8: 10am, 01/09/2022 and started that of sets\

#TOPIC: SETS
#Sets are the third type of collection data types that we have been learning, starting from lists. tuple, sets and dictionary.
#Sets are unordered, no duplicates, unindexed, unchantgeable (but you can remove and add items). Sets are created with curly brackets
#Set items can appear in different orders in different times  and they cannot be accesed by index or key

set_1 ={'Hello', "Ana", 'Ana', 1, 2, True, False, 0.22, (20, 'Anime', 55)}
print(set_1) # {False, 1, 2, 'Ana', 0.22, (20, 'Anime', 55), 'Hello'} - To show that set does not allow duplicates, only one 'Ana' was printed
#Set can contain different data types
#Once a set is created you cannot change the items directly from it but u can add or remove items
#If you write duplicate values in a set, the first will be used and the rest will be discarded
#Set could not contain a list as it returned the error: TypeError: unhashable type: 'list. But it contains a tuple

print(type(set_1)) # <class 'set'> - using type() to confirm the datat type of set

print(len(set_1)) #7 : using len() to confirm the length of a set

set_2 = set((12, 23, 45, 56)) # can use  set({12, 23, 45, 56})
print(set_2, type(set_2)) #  {56, 12, 45, 23} <class 'set'> - Using the set constructor to create a set and confirming the type


#SUBTOPIC: Accessing Set Items:
#There is no accesing via index or key since set is not indexes. But we can use for loop to loop through the set or check if an item is in it by using the in keyword.

thisSet = {"Maria", "Magareth", 'Philo', 'Eucharia'}

for x in thisSet:
    print(x)
    '''
Magareth
Philo
Eucharia
Maria
    '''

for x in thisSet:
    if 'a' in x:
        print('This name' + ' ' + x + ' ' + 'contains "A"')

        '''
This name Maria contains "A"
This name Magareth contains "A"
This name Eucharia contains "A"
        '''

#Once a set is created you can only add new items to it but cannot change the items

#SUBTOPIC: Add Set Items: The add() method is used to add items to sets

thisSet2 = {"Maria", "Magareth", 'Philo', 'Eucharia'}
thisSet2.add("Mercy")
print(thisSet2) # {'Eucharia', 'Philo', 'Magareth', 'Maria', 'Mercy'}. This takes one argument only

#SUBTOPIC: Adding items from another set by using the update method

thisSet2.update(thisSet)
print(thisSet2) #{'Eucharia', 'Magareth', 'Maria', 'Mercy', 'Philo'}
# Remember that set does not allow duplicates that is why even by adding other items from another set, those identical items were not inclded in the updated set.
# The items to be added using update can be other iterable objects like tuple, dict or list

tuple_4 = ('Tuple', 'Set', False, True, 25)
list_1= ["Mango", "Ant"]

thisSet2.update(tuple_4) #Updating set with tuple = {False, 'Set', True, 'Tuple', 'Philo', 'Magareth', 'Eucharia', 'Maria', 25, 'Mercy'}
print(thisSet2)

thisSet2.update(list_1) #Set and list
print(thisSet2) # {False, 'Maria', True, 'Tuple', 'Set', 'Eucharia', 'Mango', 'Magareth', 'Philo', 'Ant', 'Mercy', 25}

#SUBTOPIC: Removing set items: Set items can be removed using the remove() or discard(). This is not with index but by refering to the values directly. Since set allows no duplicates, this is straightforward pretty

thisSet2.remove(25)
print(thisSet2) # {False, True, 'Set', 'Philo', 'Maria', 'Mercy', 'Mango', 'Eucharia', 'Ant', 'Tuple', 'Magareth'}

thisSet2.discard('Mango')

print(thisSet2) # {False, True, 'Ant', 'Maria', 'Magareth', 'Mercy', 'Set', 'Philo', 'Tuple', 'Eucharia'}

# The diff betwn remove and discard is that in remove, if the item specified is not a member of the set, an error will be raised but if the item is not present in discard(), no error will be raised and nothing will happen

#We can also use pop() to remove the last item. The retun value is the popped item.

thisPop =thisSet2.pop()
print(thisPop) #False - because the returned value of a pop is the removed item

#del is used to delete the set entirely
del thisList2
# print(thisList2) # NameError: name 'thisList2' is not defined. Did you mean: 'thisSet2'?

#SUBTOPIC: Joining Sets: union() method can be used to join two sets and return one that contains everything. update() can be used to insert items from one set to another

thisSet3 = {1, 2, 3}
thisSet4 = {4, 6, 7, 8}
ThisSet5 = {9,10,11}

finalSet = thisSet3.union(thisSet4)
print(finalSet) #{1, 2, 3, 4, 6, 7, 8}
finalSet.update(ThisSet5)
print(finalSet) # {1, 2, 3, 4, 6, 7, 8, 9, 10, 11}

#SUBTOPIC: Intersection_update() method will retain only the items present in both sets

List3 = ["Mary", 'Matter', 'Miliano', 'Jude']
set4= {"Mary", 'Jude', 'Marvey', 2022, 2025}
set4.intersection_update(List3)
print(set4) #{'Mary', 'Jude'}

#the ordinary intersection() will return a new set that can be an intersection of two sets or other object iterables. Only items present in both will be returned

setInt = set4.intersection(List3)
print(setInt) #{'Jude', 'Mary'}

#symetric_difference_update() will keep only the non-duplicate items present in both


set3 = {"Mary", 'Matter', 'Miliano', 'Jude'} #Even if this is a list or tuple it will still work
set4= {"Mary", 'Jude', 'Marvey', 2022, 2025}

set4.symmetric_difference_update(set3)
print(set4) #{'Miliano', 'Marvey', 'Matter', 2022, 2025}

#symmetric_difference() method will return a set of items that are not present in both object iterables
#The difference between it and the former is that it will return an entirely new set while that of update will just update

symSet = set4.symmetric_difference(set3)
print(symSet) # {'Jude', 2022, 2025, 'Mary', 'Marvey'} - remember that set4 is already updated before here

#SUBTOPIC: SET METHODS: They include:
# add() - add elements to the set
# remove() - remove specified element from the set
# clear() - empty the set
# copy() - Make a copy of the set
# difference() - returns a new set that contains the elements in one set that are not preesent in another set, eg:

setA = {'A', "B", 'C', 'E'}
setB = {'A', 1, 2, 'C'}
setC = setA.difference(setB)
print(setC) #{'E', 'B'}

# difference_update() - removes the items in this set that are present in the other set or iterable object
setA.difference_update(setB)
print(setA)
# discard() -  removes a specified item
# intersection: Returns a set with the items that are present in this set and the other
# intersection_update() -  removes the item that is present in this set but not present in the other set
# isdisjoint() - returns true if the two sets have an no intersection and false if they do
setA = {'A', "B", 'C', 'E'}
setB = {'A', 1, 2, 'C'}
print(setA.isdisjoint(setB))
# issubset() - returns true if all the elements in this set are present in the comparing set and false if not
# issuperset() - returns true if all the elements in another set are present in this set
# pop() removes a random element from the set and returns it.
# remove() - reoves the specified element and
#Symmetric_difference() - returns a new set that contains items from both sets that are not present in both sets
# symmetric_difference_update() - inserts the symm diff from this set to another set
# union() m- returns a set containing the union of two sets
# update() - update a set with another set or other iterable


#NEW TOPIC: PYHTON DICTIONARIES:
# Dict is a data collection type in python. It is created with curly brackets and has key:value pairs.
#Dict is ordered, the items are changeable and do not allow duplicates. The keys are strings while the values can be any datat types
#Each key, value pair are divided by comma. We can also add, remove or change items in the dict

dict1 = {
'name': 'Green',
'name': 'Anatu',
'age': 29,
'city': 'Ontario',
'profession': 'dev',
'hobbies': ['Gaming', 'Running', 'Movies'],
}

print(dict1) # {'name': 'Anatu', 'age': 29, 'city': 'Ontario', 'profession': 'dev', 'hobbies': ['Gaming', 'Running', 'Movies']}
# In the above we see that the name whose first alphabet is A is chosen over the one that starts with G. So when there is a duplicate, the item that has the higher order will be chosen. If int, the bigger number will be chosen. Duplicates are not allowed in dict
print(len(dict1)) # The length of a dict. 5 is the answer because the 'name' duplicate is ignored
print(type(dict1)) # type of dictionary is 'dict'

#SUBTOPIC: Accessing Dict Items: We can use square brackets to access items by referring to the key or we use the get() method
print(dict1['city']) # Ontario
print(dict1.get('name')) # Anatu

# Get Keys: key() is used to get the list of all the  keys in a dict. It is a view of the dict. so any changes made to the dictionary will reflect on the keys

print(dict1.keys())  # dict_keys(['name', 'age', 'city', 'profession', 'hobbies'])

dict1['eye-color'] = 'brown'
print(dict1.keys())  # dict_keys(['name', 'age', 'city', 'profession', 'hobbies', 'eye-color']) - updated keys

# Get dict values: values() will return a list of the values in the dict
print(dict1.values()) # dict_values(['Anatu', 29, 'Ontario', 'dev', ['Gaming', 'Running', 'Movies'], 'brown'])
#Just like keys, the list will be updated when changes are made to the dictionary

dict1['Fav-color'] = 'Green'

print(dict1.values()) # dict_values(['Anatu', 29, 'Ontario', 'dev', ['Gaming', 'Running', 'Movies'], 'brown', 'Green'])

#Get items: items() will return a list of the items (key,value pairs) in a dict as individual tupes in a single list. This again is a view of the dict and will change when the dict is updated

print(dict1.items()) # dict_items([('name', 'Anatu'), ('age', 29), ('city', 'Ontario'), ('profession', 'dev'), ('hobbies', ['Gaming', 'Running', 'Movies']), ('eye-color', 'brown'), ('Fav-color', 'Green')])

# Check for items: We use the 'in' keyword to check using the item key

print('name' in dict1, 'car' in dict1) # True , False

#Change item: changing is done by referring to the key of the item

dict1['city'] = 'Lagos'
print(dict1) # {'name': 'Anatu', 'age': 29, 'city': 'Lagos', 'profession': 'dev', 'hobbies': ['Gaming', 'Running', 'Movies'], 'eye-color': 'brown', 'Fav-color': 'Green'}

#Update a list: update() method is used to update (add) key-value pairs into a dict. The argument must be a dict, ie, i a curly bracket

dict1.update({'salary': 150000, 'status': 'single'})

print(dict1) #{'name': 'Anatu', 'age': 29, 'city': 'Lagos', 'profession': 'dev', 'hobbies': ['Gaming', 'Running', 'Movies'], 'eye-color': 'brown', 'Fav-color': 'Green', 'salary': 150000, 'status': 'single'}

#Adding tems to dict: you can use the update() method as dicuyssed or simply assigning an index key and value to the dictionary as seen.

dict1['language'] = 'Python'

#Remove items from Dict: There are different ways to get this done.
# pop() - this will remove the specified item when fed the key name

dict1.pop('salary')
print(dict1) # salary removed
# dict1.pop() - TypeError: pop expected at least 1 argument, got 0 - pop in dict requires a keyname

# popitem() - remove the last item in the dict

dict1.popitem()
print(dict1) # removed language

## del keyword removes the specified key item. It can also delete the entire dict

del dict1['profession']
print(dict1) # {'name': 'Anatu', 'age': 29, 'city': 'Lagos', 'hobbies': ['Gaming', 'Running', 'Movies'], 'eye-color': 'brown', 'Fav-color': 'Green', 'status': 'single'}

dict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del dict2
# print(dict2) - NameError: name 'dict2' is not defined. Did you mean: 'dict'?

## looping through a dict: this can be done using the for loop:

dict3 = {
'name': 'Green',
'age': 29,
'city': 'Ontario',
'profession': 'dev',
'hobbies': ['Gaming', 'Running', 'Movies'],
} # repeated dic1 for easy assess

for x in dict3:
    print(x) # prits all the keys one by one

for x in dict3:
        print(dict3[x]) #prints all the values

# You cn use the values() mthod to return the dict values via looping:

for x in dict3.values():
    print(x)  #prints the values one line at a time

#You can use keys() to also return keys
for i in dict3.keys():
    print(i) #prints the keys one line at a time

# use items() method to loop through the items

for j in dict3.items():
    print(j)
'''
('name', 'Green')
('age', 29)
('city', 'Ontario')
('profession', 'dev')
('hobbies', ['Gaming', 'Running', 'Movies'])
'''

#SUBTOPIC: Copying dict: you cannot just copy a dict by doing dict2 = dict1 as dict2 will simply be a view of dict1 and reflect its chnages. You can however make a copy by using the copy() methode or create a new dict from another using the dict() method
# Example of trying to copy one dict to another using just =

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964} - a view of thisdict. Now let us make chnages to the mirrored dict
thisdict['founder'] = 'henry ford'
print(thisdict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'founder': 'henry ford'}
print(mydict) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'founder': 'henry ford'}

#let us now make a real copy where the copied dict chnages will not affect the new dict

dict4 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict5 = dict4.copy()
print(dict5) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964} - copied
dict4['founder'] = 'henry ford'
print(dict4) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'founder': 'henry ford'}
print(dict5) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964} - unaffected by changes to dict4

# Make a copy using dict()
dict6 = dict(dict4)
print(dict6) # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'founder': 'henry ford'} - took the latest form where 'founder' has been added to dict4

#SUBTOPIC: Nesting Dicts: When a dict is contained in another dict it is called nested dictionaries

myFriends = {
    'friend1': {
        'name': 'Dami',
        'age': 26,
        'location': 'Ogun'
    },
    'friend2': {
          'name': 'Charles',
        'age': 30,
        'location': 'Lagos'
    }
}

print(myFriends) # {'friend1': {'name': 'Dami', 'age': 26, 'location': 'Ogun'}, 'friend2': {'name': 'Charles', 'age': 30, 'location': 'Lagos'}}

#you can add different dicts into one

student1 = {
    'name': "Abiola",
    'classes': ['Geo', 'Computer', 'literature'],
    'age': 12
}
student2 = {
    'name': "Abiola",
    'classes': ['Phy', 'Chem', 'Eng'],
    'age': 14
}
student3 = {
    'name': "rAMOTU",
    'classes': ['Inter', 'Computer', 'Maths'],
    'age': 9
}

allStudents = {
    'student1': student1,
    'student2': student2,
    'student3': student3
}

print(allStudents) # {'student1': {'name': 'Abiola', 'classes': ['Geo', 'Computer', 'literature'], 'age': 12}, 'student2': {'name': 'Abiola', 'classes': ['Phy', 'Chem', 'Eng'], 'age': 14}, 'student3': {'name': 'rAMOTU', 'classes': ['Inter', 'Computer', 'Maths'], 'age': 9}}

#SUBTOPIC: Dict methods:
# clear() - removes all the elements from a dict
# copy() - make a copy of the dict
# pop() - remove a specified item using the key
# popitem() - remove the last item in the dict
# dict() - copy a dictionary
# items() - return the list of items. Each key-value pay is a tuple and everything is in a single list
# keys() - returns a list of the keys that make a dict
# values() - returns a list of the values that make a dict
# get() - returns the value of the specified key
# update() -  updates the dictionary with the provided key-value pair
#fromkeys() - used to add multiple key-value pair to a dict at once. The values may be the same or none at all. The keys are required while the values are optional and when nopt included return 'none'.

emptyDict = {} # this is seen as an empty dict by python
print(type(emptyDict))
addkeys = ("student4", 'student5', 'student6')
#addvalues = ('James', 'John', 'June')

allstudentupdated =  emptyDict.fromkeys(addkeys)
print(allstudentupdated) # {'student4': None, 'student5': None, 'student6': None}

#setdefault() - this method returns the value(s) of the items with the specified keys. If the key does not exist, insert the key with the specified value

setDef = allstudentupdated.setdefault('Student7', 'Adams')
print(setDef) # Adams is returned because the setdefault() uses the second argument as the value and the first as the key. If there was no value assigned, 'None' will be returned.


##NEW TOPIC: PYTHON IF ELSE:
# In python the usual conditionals are accepted: == (equals to), != (not equal), > (greater than), >= (greater than or equals to), < (less than), <= (less than or equals to), !< (not less than), !> not greater than.

# the conditionals are usually used in conjuction with if statement or loops. The if statement is writen with if to evaluate a condition and then do something based on whether the evaluation returns positive or negative.

case1 = 23
case2 = 28
case3 = 23
if case1>case2:
    print("case one is greater than case 2")
else: # adding else
    print('Case two is greater')

# Indentation: Python relies on Indentation (the white space before a line of code) so if the print above was without indentation, an error will be returned. Also, if the else was indented above to be in the same line with print, an error will ensue.

# Elif is used to tell pythin that if the previous condition is not met, try this one
if case1>case2:
    print("case one is greater than case 2")
elif case1 == case3:
    print('case1 is equal to case three instead') # case1 is equal to case three instead

# Else: the else keyword will capture anything that was not captured by the previous conditions. else can be used with or without elif

case4 = True
case5 = False
if case4 == False:
    print('case4 is false')
elif case5 == True:
    print("case5 is False")
else:
    print('No condition was met') # No condition was met

#There are shorthands for if...else statements called ternary operators or Conditional expressions

print('Bool pass') if case4 == False else print("bool failed") # bool failed

#or for a sinle line of code

if type(case4) == bool: print('This is a bool data type') #This is a bool data type

# multiple if..else statements can also be writen in a single line

num1 = 10
num2 = 20
num3 = 30

# if num1 > num2: print('num1 is greater than num2') if num2 > num1: print('num2 is greater than num1') - wont work

print('num1 is greater than num2') if num1 > num2 else print('num2 is greater than num1') if num2 > num1 else print('No condition passed')
# num2 is greater than num1

#The And and Or keywords are logincal keywords used in combining conditional statements

if num1<num2 and num2< num3:
    print('There is a serial pattern') # There is a serial pattern

if num2>num1 or num3>num2:
    print(num2, "is in the middle") # 20 is in the middle

#Nested if statements: this is when if statements are nested to another if staement to achieve the desired goal

num4 = 30
if num4>1:
    print('num4 is greater than 1')
    if num4>20:
        print('also greater than 20')
        if num4>=30:
            print('num4 is also equal to or greater than 30')
        else:
                print("this is the end")

'''num4 is greater than 1
also greater than 20
num4 is also equal to or greater than 30
'''

# The Pass statement is used when you want your if statement to be empty and not eturn anything because normally and if statement cannot be just empty

if num4 < 100:
    pass #Nothing happens and no error is printed

if num4<100: print("hi") #ternary op or conditional expression

##NEW TOPIC: PYTHON WHILE LOOPS: There are two primitive looping commands in py:
#for loops
#while loops
#While loops will execute a command or set of commands as long as a condition is true. It usually starts with an iterator (usually called i) and at the end of each loop, a specified number is added to the i. When another loop occurs, it checks if i has reached the limit set. This is to avoid infinite loops. the while lop requires an indexing variable to be set at the beginning such as i = 0.

it = 1
while it<5:
    print('While loop is running', it)
    it +=1

#Break statement is used to stop the loop even if the while loop is running

i = 0
while i<10:
    print('i is till less than 10')
    if i == 5:
        print("Let us stop here at i == 5")
        break
    i += 1
'''
Result:
i is till less than 10
i is till less than 10
i is till less than 10
i is till less than 10
i is till less than 10
i is till less than 10
Let us stop here at i == 5
'''
#The continue statement will stop the current iteration and continue with the next. So if 1,2,3,4,5 where to be printed in the loop and I setcontinue at when i == 2, afte 1 is printed, two will be skipped and then 3 will be printed and then the others:

i = 5
while i>0:
    i -=1
    if i == 3:
        continue
    print(i, 'is still greater than 0')

'''
Result:
4 is still greater than 0
2 is still greater than 0
1 is still greater than 0
0 is still greater than 0
'''

#Else statement: With this we can do something when the while condition is no longer true

i = 0
while i < 5:
    print(i)
    i +=1
else:
    print('i is no longer less than 5')

## NEW TOPIC: PYTHON FOR LOOPS: The for loop in pythoin is used to loop over a collection datat type. That is iterating over a sequence like tuple, dict, list or set or even a string. We can use the for loop to execute a set of statements, one for each item in the collection being looped over


announcement = '''Python is fun to learn!
Your kids can learn Python

'''
for x in range(4):
    print(announcement)

'''
Result:

Python is fun to learn!
Your kids can learn Python


Python is fun to learn!
Your kids can learn Python


Python is fun to learn!
Your kids can learn Python


Python is fun to learn!
Your kids can learn Python

'''

cars = ['Jeep', 'Tesla', 'Benz', 'Honda', 'Nord', 'Innoson']

for x in cars:
    print('This car is a', x )

    '''
This car is a Jeep
This car is a Tesla
This car is a Benz
This car is a Honda
This car is a Nord
This car is a Innoson
    '''

#Looping through a string: Strings contain a sequence of characters so they are iterable objects.

string = "AnatuGreen"
for x in string:
    print(x) #prints each alphabet separately

# We can stop the for loop before it loops through the object by using the Break Statement:

for x in string:
    print(x)
    if x == 'G':
        break # prints and stops at G

#Date: 03-sept, 2022 continuation of study

# For loop continue statement: We can use this to skip the current iteration of the loop and continue to the next

for x in string:
    if x == 'e':
        continue
    print(x)

    '''
A
n
a
t
u
G
r
n
    '''

# For loop range() frunction: This is used to do something several times while a range is running from one number to an end. The loop stops running before the upper floor of the range is reached. That means that a range from 0 to 3 is 0,1,2. 3 Excluded. We can add a range starting number and ending number but if only one parameter is provided, then it will be the ending while 0 will be the starting point by default

for i in range(5):
    print(i) # prints 0-5

for i in range(2,8):
    print(i) # prints a loop of 2-7

#We can add a third parameter to specify the number by which the range will increment. The default is 1

for a in range(10,20,2):
    print(a)

    '''
10
12
14
16
18
    '''

#Else in if: This is used to specify what block of code to execute when the loop is done.
for x in range(2,10,2):
    print(x)
else:
    print('Loop is complete')

    '''
2
4
6
8
Loop is complete
    '''

#The else will not work if the loop is broken with a break

for x in range(5):
    if x == 3: break
    print(x) # 0-2 printed
else:
    print('WE are done')  # Not printed because the loop already broken  by break

# Nested for Loops: This is a loop inside another loop. The inside lops will be executed one

for x in range(1,3):
    for y in 'ABC':
        print(x,y)

'''
printed:
1 A
1 B
1 C
2 A
2 B
2 C
'''

# Pass statement: This can be used to tell python to do nothing in a loop. This is used because for loop like while loop cannot be  left empty

for x in range(1,3):
    for y in 'ABC':
        pass #Nothing

# NEW TOPIC: PYTHIN FUNCTIONS

# A function is a block of code that runs only when called and which can have parameters passed into it. It can accept data (parameters) and can return data as a result of running.

# functions are created using the def keyword

announce = '''All kids should learn coding!
'''
def print_announce():
    print(announce * 3) # Creating the function

print_announce() # Calling the function

'''Result:
All kids should learn coding!
All kids should learn coding!
All kids should learn coding!
'''

# SUBTOPIC: Py function arguments: Data called arguments can be passed into a function on creation  inside the parentheses after the name of the function. You can add as many names as you wish but separated by commas. In the normal computing palance, what is put in the brackets after the name of the function, at creation are called Parameters. They are like placeholders that can then be replaced by real data when the function is called. This real data are known as Arguments. Arguments are usually shortened as args in py docs.
# Again, parameters are variables that can be replaced by ral values (arguments) when a function is called

def addition(num1, num2): # Parameters are defined and will be replace by arguments when function is called
    print(num1+num2)

addition(20,30) # 50 - the function simply takes the arguments and do the calculation that it was crated to perform

# Let us create a function that checks if you can enter a website or not and returns a message based on arguments passed

def adult_checker(name,age):
    if age>=18:
        print("Hi", name, "you are", age, " and an adult so you can proceed. Play safe!")
    else:
        print('Hey there', name, "Sorry, you are", age, "you not old enough to visit this site. Try again when you are 18")

adult_checker("Green", 17) # Hey there Green Sorry, you are 17 you not old enough to visit this site. Try again when you are 18
adult_checker("John", 25) # Hi John you are 25  and an adult so you can proceed. Play safe!

# Number of args: By default, an error will emerge if you try to call a function with more or less number of arguments compared to the number of parameters it was created with/.

def thisfunction(par1, par2):
    print('Hello', par1, par2)

thisfunction('Green') # TypeError: thisfunction() missing 1 required positional argument: 'par2'

#Subtopic: Arbitrary Arguments, *args: You can add the * just bfeore the parameter in an argument if you do not know how many arguments it will be receiving in the future. The function will therefore rcv a tuple of arguments which which to process.

def addition_Func(*args):
    print(sum(args)) # Using the sum method to add all arbitrary numbers that will be specified

addition_Func(50,100,200,300) # 650

#Subtopic: Keyword Arguments: you can send arguments as key-value pairs so that the order of the arguments do not maatter when calling the function. In this case, each parameter is a key and the value that you will want to replace it with when the function is called is the value.
#Keyword arguments are shortened as 'kwargs' in py

def bids(bid1, bid2, bid3):
    print("We have the following bids so far:", bid1, ', ', bid2, ' ,', bid3)

bids(bid3=100, bid1=200, bid2=500) # We have the following bids so far: 200 ,  500  , 100
#Note how in the above the order of the args did not matter since the function was provided with the keywords

#Subtopic: Arbitrary Keyword arguments: **kwargs: If you don't know how many arbitrary keywords that will bve needed in the function in the future, you can use ** before the single parameter name in the function creation. This will make it so that the function will receive a dictionary of arguments and the items of the dictionary can be accessed according to their keys.

def students(**detail):
    print("This student's first name is:", detail['fname'])
    print("This student's last name is:", detail['lname'])

students(fname="Andrew", lname='James')

'''
Result:
This student's first name is: Andrew
This student's last name is: James

'''

#Subtopic: Default parameter value: This is a way to give a default parameter that will serve as an arg if the function is eventually called without an argument. For example:

def my_Country(country="Nigeria"): # Giving the default value so Nigeria will be country if no arg is entered when the function is called
    print("My country is:", country)

my_Country() # My country is: Nigeria
my_Country("Canada") # My country is: Canada because Canada has been fed in.

#Subtopic: Pass a list as an argument: List, tuples, set, numbers, floats etc can be passed into a function and be treated as the normal way other data are done

myList = ["Damola", 'Damiloloa', 'Tolu', 'Marvey']
def myFunction(names):
        print("Names of people:", names)

myFunction(myList) # Names of people: ['Damola', 'Damiloloa', 'Tolu', 'Marvey']

myList = ["Damola", 'Damiloloa', 'Tolu', 'Marvey']
def myFunction(names):
    for x in names:
        print(x)

myFunction(myList) #Loops through and prints each name

#Subtopic: Return a value: You can return a value directly from a function by using the return keyword

def retFunc(x):
    return 20*x

print(retFunc(10)) # 200

#Subtopic: Pass statement: Use this when you want a function definition to do nothing, to be empty

def empty():
    pass

empty() # Nothing happens

#Subtopic: Python Function recursion: This is when a defined function calls itself. This is a maths and programmatic concept where a function loops through data to reach an outcome. This should be writen carefully to avoid writing one that causes an infinite loops that takes all the system resources or crashes the application or system.

#Recursion has its advantages and disadvantages but you may never need to use it as you can use a loop for easier understanding and maintaining of code

def my_recursion(i):
    if i>0:
        result = i + my_recursion(i-1)
        print(result)
    else:
        result = 0
    return result

print('\n\nRecursion example with results')

my_recursion(10)


#NEW TOPIC: PYTHON LAMBDA:
#A lambda is a small anonymous function that can accept unlimited number of arguments but can only have one expression.

#Syntax:  lambda arguments: expression. The function will execute the expression and return the result as its outcome

x = lambda a : a **2
print(x(2))


# The below lambda function accepts 3 args to see which one is larger and returns the largest
larger=lambda a,b,c: a if a>b and a>c else b if b>a and b>c else c if c>a and c>b else print("end")

print(larger(20,15,30)) #30

# We can also use lambda inside a higher-order function to briefly perform a role

# This program below will double each item in a list. This program makes use of the map function which takes in the lambda function and a list as arguments

my_List = [2,4,3,5,7,8,9]

double_list = list(map(lambda x: x *2, my_List))
print(double_list) # [4, 8, 6, 10, 14, 16, 18]

#This function below will sort a list of words based on thier lengths

my_Words = ['Elephant', 'Bee', 'hipopotamus', 'Ant', "Goat", "Tiger"]
my_Words.sort() # Default sorting is by alphabetical order: ['Ant', 'Bee', 'Elephant', 'Goat', 'Tiger', 'hipopotamus']
print(my_Words)
my_Words.sort(key = lambda i: len(i)) #Sorting by length of each word. i serving as an iterator
print(my_Words) # ['Ant', 'Bee', 'Goat', 'Tiger', 'Elephant', 'hipopotamus']

# The use case of Lambda varies based on your need and expertise but just know that if you need a single line expression to run for a short time under an anonymous (unnamed) function, then lambda is your guy. It is not meant to be reused, just on the go basis. More on python lambda here: https://www.programiz.com/python-programming/anonymous-function

#NEW TOPIC: PYTHON ARRAYS: python does not have a built-in array type but lists serve the purpose instead. You can also import Numpy library or similar libraries to use arrays. Everything in this topic is same as what we have learnt under lists so just review that. For refreshment, here are array(list) methods and their functions
# append() - Add an element at the end of the array
# clear() - Delet all items from the array
# copy() - Create a copy o an array that does not mirror it's parent's changes
# count() - Returns the number of times the specified value appears in the list
# extend() - add elements from another list or other iterables into another list, at the end of
# index() - Returns the index of the first elemt with the specified value
# pop() - Removes the element that has the specified index or removes the last element if no index is given
# remove() - Removes the first specified element whose value is fed in as an arg of the remove method
# reverse() - Reverse the order of the list
# sort() - sort the list

# NEW TOPIC: PYTHON CLASSES AND OBJECTS;
# Python is an object-oriented prog language. Meaning that almost all the elements that make up Python mimick real life objects. They have their own independent properties and methods
# A class is like an blueprint for the creation of something, an constructor from which objects are built.The class will specify the properties and the behaviours expected of the object or objects that vcan be created from it. The user can now adopt the class to built/construct any number of instances of that class. Each of those instances are called an object.
# OOp allows us to have better organized code and reusable codes
#When working with objects, variables are called attributes and functions are vcalled methods
#It alows us to organize organize related data together and practise the DRy methode of coding


# Creating A class; this is done using the class keyword

class myClass:
    name = 'Anaturuchi'
    age = 29
    sex = 'male'
    def check_adult_or_minor(me):
        if me.age >=18:
            print('This student', me.name, 'is', me.age, ' or more and an adult')
        else:
            print("Student is", me.age, 'therefore a minor')

#In the above, we have created a class and given it some default atributes, name, age, sex. We also gave it some a method called check_adult_or_minor with an arg called 'self' or 'me' which can be any word really but self is used conventionally, it points to the individual instance where this class will be used in the creation of an object. With these we can create objects from this single class, as many as we want and they will inherit these properties and method(s) and we can modify each according to the object we create but they will act in the expected fashion as the class they are created from.

#We can see from the above that we can just create the class and assign attributes and methods to it that can be replicably used in the objects created from the class but this is not a good practise:


myObj = myClass()
myObj.name = "Chinaza"
myObj.age = 18
check_age = myObj.check_adult_or_minor() # This student Chinaza is 18  or more and an adult

#The above way of assigning attributes to a class is not the best and is discouraged
# Built in _init_() function: We use this function to assign values to object properties or define other operations that need to run when an object is created from the class

class person:
    #Create a method that initializes the various data, attributes, for a user
    def __init__(self, age, name, address, DOB):
        self.name = name
        self.age = age
        self.address = address
        self.DOB = DOB
#Create a second method that prints a statement about the person
    def print_user_info(self):
        if self.age and self.name and self.address and self.DOB:
            print(self.name, 'is', self.age, 'years old and lives in', self.address,'born', self.DOB)

# create yet another method that checks whether or not the person is an adult or minor
    def check_adult(self):
        if self.age >=18:
            print('This person', self.name, 'is', self.age, 'and an adult')
        else:
            print("Person is", self.age, 'therefore a minor')


#Creat an object from this class above
p1 = person(29,'Anat', "Lagos Nigeria", "7/3/1993") # Notice how the attributes are arranged in order as in the class

infoPrint = p1.print_user_info() # Anat is 45 years old and lives in Lagos Nigeria born 7/3/1993
print(p1.name)
print(p1.address)
print(p1.DOB)
print(p1.age)
p1.check_adult() #This person Anat is 29 and an adult

# So the __ini_- function called each time an object is created with the class.

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def calPerimeter(self):
        return self.a + self.b + self.c # The method should return the result of the sum of all three
        #This can also be perimeter = self.a + self.b + self.c , return perimeter


Tri_Obj = Triangle(200,300,200)
ObjPer =Tri_Obj.calPerimeter()
print(ObjPer)

#Date: 05/Sept,2022

#Subtopic: Object Methods: Objects can contain methods as created at the class level. The method is a function that is located inside an object and belongs to it. We have seen examples in the calPerimeter above and others.

#Subtopic: The self parameter. This is first parameter in the class method (object method). It is used to refer to this current instance of the class and used to access the variables (attributes) that belong to that class. The name 'self' is not mandatory, it can be anything you like but just make sure that it is the first parameter in your __init__() method.

#Subtopic: Modifying object properties: This is done by making reference to the property using the object name and assigning the new value. eg:

thisInstance = Triangle()
thisInstance.a = 500 # We have modified the value of side a ro 500

# Subtopic: Deleting Object Properties: This can be done using the del keyword:
#del object.property

class thisClass:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def myInfo(self):
        print("My name is", self.name, "My height is", self.height, 'cm')

myObject = thisClass("Green","175")
myObject.myInfo()


class mySavings:
    def __init__(me,income,expenses):
        me.income = income
        me.expenses = expenses

    def balance(self):
        return self.income - self.expenses

mySavingsInfo = mySavings(150000,50000)
myBalance = mySavingsInfo.balance()
print(myBalance) # 100000

print(myBalance)
#Delete the object mysavingsInfo

del mySavingsInfo

#Subtopic: The pss statement: Class definitions can't be empty without causing an error so we use pass statement when we want it empty

class mySelf:
    pass

#NEW TOPIC: PYTHON INHERITANCE:
# inheritance allows us to copy(inherit) all the methods and attributes of another class. The parent class it tyhe one being inherited from, also called base class while the child class is the inheritor, aka, derived class

#Subtopic: Create a Parent/base class: Any class can be an parent so the same syntax of creating any other class works.
#Eg: Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName, self.lastName)

#Use the Person class to create an object, and then execute the printname method:

PersonObj = Person("matthew", "Green")
PersonObj.printName() #matthew Green

#Subtopic: Create a child class: To do this we send the parent class as a parameter to the child class on creation

class ChildOfPerson(Person):
    pass # Pass used because of not wanting to add anything yet

#Use the Student class to create an object, and then execute the printname method:

ChildsObj = ChildOfPerson("Anatu", "Green")
ChildsObj.printName()

#Adding __init__() in the child class: When this is done, the child class no longer inherits the properties of the parent. eg;

class Child2OfPerson(Person):
    def __init__(self,salary, rent):
        self.salary = salary
        self.rent = rent

    def message(self):
        print("The salary is okay ") if self.salary > self.rent else print("get a new job or relocate")

rentObject = Child2OfPerson(100, 150)
rentObject.message() # get a new job or relocate

# The above shows that using the __init__ the second child class has created a different set of properties and method for itself and no longer relates  with what the parent has even though still bearing the parent's name so to say. The child's init overides the parent's inheritted init function

#Subtopic: Overriding a parent's init method and still inheriting it: After we have initially overiddent the __init__ method of the parent class in a child class, we can still bring that method into use. The reason for this could be that we still have something to do with the parent's init method and we just do not want to repeat ourselves (DRY) in the child class. Two ways of doing this is via direct calling of the parent's init again under the chil'd init or using super() function in the child, in which case we won't need to use the name of the parent and all attributes and methods get imported.
#Eg: The let us look at child 3 of person

class Child3OfPerson(Person):
    def __init__(self,salary, rent, firstName, lastName): #The init of the child overiding that of the parent
        Person.__init__(self, firstName,lastName) #Note that the attribute names have to be in the child's init name if not it will be saying undefined
        self.salary = salary
        self.rent = rent


    def message(self):
        print("The salary of", self.firstName, self.lastName, "is okay ") if self.salary > self.rent else print(self.firstName, self.lastName,"needs to get a new job or relocate")

rentObject = Child3OfPerson(100, 150, "John", "Wick")
rentObject.message() # John Wick needs to get a new job or relocate

#Inn the above we have seen the power of a child overidding and still inheriting the the init function of his parent.

#Subtopic: Using the super() function: The child class can use the super() function to inherit all the properties and methods of her parent class without you writing the name of the parent. Again let us create a new child class again from the 'Person'

class ThirdChild(Person):
    def __init__(self, firstName, lastName, distance):
        super().__init__(firstName, lastName)
        self.distance = distance

    def record(self):
        print("The runner", self.firstName, self.lastName, 'holds a record of', self.distance, 'km')

runnerObj = ThirdChild("Tobi", "Amusan", 100)
runnerObj.record() # The runner Tobi Amusan holds a record of 100 km

#Subtopic:Add Properties. We can add properties to the class: self.propertyname = value. The value cannot be a variable name unless you will add it to the parameters of the __init__(). It can be other things like string, numbers, lists, tuple etc. Note that the property added this as will not be able to be included as an argument when an object is created from the child class:
'''
class FourthChild(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.bid = 1000

    def personBid(self):
        print(self.firstName, 'bidded', self.bid)

bidDisplay= FourthChild("mike", "jagger", 10000)
bidDisplay.personBid()

Resulting error: TypeError: FourthChild.__init__() takes 3 positional arguments but 4 were given

'''
#But we can:

class FourthChild(Person):
    def __init__(self, firstName, lastName):
        super().__init__(firstName, lastName)
        self.bid = 1000

bidDisplay= FourthChild("mike", "jagger")
print(bidDisplay.bid) # 1000

#So if we wanted self.bid to work with the objects created from FourthChild, we would have just added 'bid' as a variable in the __init__() of it.

#Subtopic: We have also seen that we can easily add one or multiple methods to the parent or the childresn classes. We havedone that severally so no need to repeat an example. Just remeber that the method being added must have the 'self'(or whatever name you choose) parameter and that all references to the __init__ parameters must be in the form of 'self.parameter'. eg:
'''
def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

'''
#Also note that if the name of the method created in the child is exactly same as a method in the parent, the child's will override that of the parent.

#End of topic

#NEW TOPIC: PYTHON ITERATORS: An iterator is an object that contains a countable number of values. It is an object that can be iterated on, meaning you can go throught it back and forth severally. You can go through all the values. The word iterate is usually used to refer to when you go over something again and again to achieve a given result.

#In py, an iterator implements the iterator protocol. The iterator protocol is made up of __iter__() methode and __next__() method.

#Iterator Vs Iterable: Strings, lists, tuples, sets, dict are all iterable objects. They are containers that are iterable and can get an iterator form. They all containa iter() method used to get an iterator.
#eg, run an iterator for the iterable object list

myList = ["Lady", 'In', "Red", "Is", "Dancing", "With", 'Me'] #Iterable
myIterator = iter(myList)

print(next(myIterator)) #Lady
print(next(myIterator)) #In
print(next(myIterator)) #Red
print(next(myIterator)) #Is
print(next(myIterator)) #Dancing

#Subtopic: Loopint through an Iterator: As we covered before now we can use the for loop to loop through an iterable object of any type. We can also use the while loop

for x in myList:
    print(x) # prints each word of myList in a separate line. This works for string too. Iteration does not work on int or float

myNumber = 7035719745

for x in myNumber:
    print(x) # TypeError: 'int' object is not iterable

# The for loop works in the background by creating an iterator object and executes the next method for each loop.


#Subtopic: How to Create an Iterator: To create an object or class as an iterator, you have to implement the iter and next methods on the object.
# #The __iter__() object will act like the __init__() method to do some operations but will always return the iterator object itself
#the __next__() method will do operations but must return the next item in the sequence

#eg: Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        a = self.x
        self.x +=1
        return a

myClass = MyNumbers()
myiter = iter(myClass)

print(next(myiter)) #1
print(next(myiter)) #2
print(next(myiter)) #3

# Subtopic: StopIteration: If you keep making prints as seen above or use a for loop, the iteration will become infinite, we use StopIteration statement to prevent this. We can do this by setting a condition inside the next method to tell the program at what point to stop the iteration:

class MyNumbers:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        a = self.x
        self.x +=1
        if a <=5:
            return a
        else:
            raise StopIteration


myClass = MyNumbers()
myiter = iter(myClass)

print(next(myiter)) #1
print(next(myiter)) #2
print(next(myiter)) #3
print(next(myiter)) #4
print(next(myiter)) #5
print(next(myiter)) #  raise StopIteration StopIteration


 #NEW TOPIC: PYTHON SCOPE: Scoping is the phenomemon where a variable is available to use only in/from the region where it was created.
 # Local scope: A variable created inside a function is only available inside the function

def myScope():
    scopeName = "Local"
    print(scopeName)

myScope() # Local

def myScope2():
    print(scopeName) #"scopeName" is not defined

#Subtopic: Function inside a function: When a function is resident inside another function, it can access the variables inside the parent. eg:
def myScope(): #parent
    scopeName = "Local" #local var
    def childFunc(): #Child funct
        print(scopeName)
    childFunc() # Calling the child function inside the parent

myScope() # "Local"

#Subtopic: Global Variable: This a variable create dwithin the main body of the python code. It is available to use from anywhere in the program, both locally and globally.

globalVar = 2022

Dob = 1993-globalVar
print(Dob) #-29 - global availaibility

def calcDOB():
    year = 1995
    print(globalVar - year) # making calculation with local and global vars
calcDOB() # 27

#Subtopic: Naming local and global variables: If you name a global and a local variable with the same name, py will treat them as two different vars. The one outside will only apply to outside and the one inside the function(local) will be available inside as usual and overwrite the external

sex = 'male'

def sexPrinter():
    sex = ['Female', 'Male']
    print(sex)

sexPrinter() # ['Female', 'Male'] - prints the local

print(sex) # male - prints the global

# Subtopic: Global Keyword: The keyword 'global' is used to indicate that a variable is global if you are stuck inside a local scope but just need to create a global variable from there. You first declare the variable as global before going on the next line to assign a value to it

def globTest():
    global glob
    glob = 100
    print(glob)

globTest() #100

print(glob) #100 - showing that glob is now global

#You can use the 'global' keyword to also make changes to a global variable inside a function (local scope)

def globTest2():
    global glob
    glob = 200
    print(glob)

globTest2() # 200
print(glob) #200 - Note how the global varible's value has now been changed because of that chnage we made inside the function above using the keyword

#NEW TOPIC: PYTHON MODULES:
# a module in py is same as a library as seen in Javascript for example. It is a package, a file containing functions by you or other people that you will like to use in you program.

#Subtopic: Creating a Module; To do this, simply save the function(s) with the extension .py
# I have saved this as a module
def GreetMe():
    print("helo Mr Green, you will be a great programmer, build great stuff and be super rich")

#Subtopic: To use A module: Simply import the module name without the .py and call the function inside it using the module name: Syntax: module_name.function_name(arg) - *argument if any. If there was a param in the function and you do not add an argument when calling it, error will print

import GreetMe

GreetMe.Greet("Mr Green") # Hello Mr Green, you will be a great programmer, build great stuff and be super rich

#Subtopic: Variables in modules:
# A module can contain functions and usually do, but they can also contain no functions and rather contain any other data type like lists, sets, dicts, tuples etc. Strings and numbers are not callable and will return error
import Variables
'''
Variables.proclaim() #TypeError: 'str' object is not callable
Variables.number() #TypeError: 'str' object is not callable
'''
var = Variables.Dictionary['name'] # Accessing dictionary items from the
print(var) # Green

# You can name the module as you wish but it must end in .py

#Subtopic: Re-naming a module: A module can be imported using an alias using 'as' keyword

import Alias as MyAlias
MyAlias.Alias() #This is a module to be imported as an alias

#Subtopic: Built-in modules: There are built-in modules in Python that can be imported anywhere and anytime you want.

import platform

x= platform.system()
print(x)

#Subtopic: Using the dir() Function: The dir() function is built-in py and will list all the function or variable names in a module.

print(dir(platform)) # list too long to post here

print(dir(Variables))

#Subtopic: Import from module: You can choose to import only part of a module by using the 'from' keyword while importing

from GreetMe import Greet

Greet("Dami") # Hello Dami you will be a great programmer, build great stuff and be super rich

#Notice that when you use from to import a module you do not use the module name to refer to the function or other objects you imported as it will give error

#NEW TOPIC: PYTHON DATES: python does not have date as a data type but a module called 'datetime' is built in that can be imported and used to display the desired time or date.

import datetime
x = datetime.datetime.now()
print(x) # 2022-09-05 21:11:17.791924 # the date contains year, month, day, hour, minute, second, and microsecond.

#There are different methods used with the datetime module to produce diffeent date items. eg

x = datetime.datetime.now()
print(x.day) #6
print(x.month) #9
print(x.year) #2022
print(x.day,'-', x.month,'-',x.year) # 6 - 9 - 2022

#Subtopic: Create a date object: We can use the date() class constructor from the datetime module to create a specific date. This requires 3 parameters of year, month and day

a = datetime.datetime(2019,12,25)
print(a) # 2019-12-25 00:00:00 - the house, min, sec, microsecond, timezone can also be specified but are 00-00-00 and none when not specified

#Subtopic: The strftime() method: This is a built-in method for formating the datetime object into a readable format. It takes the 'format' parameter:

a = datetime.datetime(2022,9,5)
print(a.strftime("%A")) #Monday
print(a.strftime("%B")) #September

# Date Legal Format Codes: There are different codes that can work the strftime method to produce desired date objects. Reference: https://www.w3schools.com/python/python_datetime.asp

import datetime
d  = datetime.datetime.now()
print(d.strftime('%X')) # '%a' - short form of day of the date


print(d.strftime('%a')) # Tue - short form of day of the date
print(d.strftime('%A')) # Tuesday - Full form of day of the date
print(d.strftime('%b')) # Sep - short form of month of the date
print(d.strftime('%B')) # September - full form of day of the date
print(d.strftime('%c')) # Tue Sep  6 02:13:57 2022 - local version of date and time
print(d.strftime('%C')) # 20 - century
print(d.strftime('%d')) # 06 - full numerical value of day
print(d.strftime('%D')) # 09/06/22 - MM/DD/YY format
print(d.strftime('%e')) # 6 - short form of the day in number
print(d.strftime('%E')) # Invalid
print(d.strftime('%f')) # 903301 (random) - Microsecond as a decimal number, zero-padded on the left.
print(d.strftime('%F')) # 2022-09-06 - YYYY-MM-DD
print(d.strftime('%g')) # 22 - short form of year  in number
print(d.strftime('%G')) # 2022 - full year in number
print(d.strftime('%h')) # Sep - short form of month of the date
print(d.strftime('%H')) # 'Sep - short form of month of the date
print(d.strftime('%i')) # invalid
print(d.strftime('%I')) # 02- Hour (12-hour clock) as a zero-padded decimal number.
print(d.strftime('%j')) # 249 - Day of the year as a zero-padded decimal number.
print(d.strftime('%J')) # invalid
print(d.strftime('%k')) # invalid
print(d.strftime('%K')) # invalid
print(d.strftime('%L')) # invalid
print(d.strftime('%l')) # invalid
print(d.strftime('%m')) # 09 - Month as a zero-padded decimal number.
print(d.strftime('%M')) # 35 - Minute as a zero-padded decimal number.
print(d.strftime('%-M')) # 35 - Minute as a zero-padded decimal number.
print(d.strftime('%n')) # Empty space
print(d.strftime('%N')) # invalid
print(d.strftime('%o')) # invalid
print(d.strftime('%O')) # invalid
print(d.strftime('%p')) # invalid
print(d.strftime('%p')) # AM - AM or PM
print(d.strftime('%P')) # invalid
print(d.strftime('%q')) # invalid
print(d.strftime('%Q')) # invalid
print(d.strftime('%r')) # 02:41:33 AM - HH:MM:SS AM/PM
print(d.strftime('%R')) # 02:43 - HH:MM
print(d.strftime('%s')) # invalid
print(d.strftime('%S')) # 19 - second
print(d.strftime('%t')) # space
print(d.strftime('%T')) # 02:45:12 -  HH:MM:SS
print(d.strftime('%u')) # 2 - Week day - ISO 8601 weekday (1-7)
print(d.strftime('%U')) # 36 - Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.
print(d.strftime('%v')) # invald
print(d.strftime('%V')) # 36 - same as %U
print(d.strftime('%w')) # 2 - ? for now
print(d.strftime('%W')) # 36 -Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.
print(d.strftime('%x')) # 09/06/22 - MM/DD/YY
print(d.strftime('%X')) # 03:07:38 - Local value of time. Depends on your location, the server may show different based on its location
print(d.strftime('%y')) # 22 - Year, short version, without century
print(d.strftime('%Y')) # 2022 - Year, full version
print(d.strftime('%z')) # UTC offset - No print
print(d.strftime('%Z')) # Timezone - no print

# NEW TOPIC: Python Math: Python has built-in math functions and  module for various mathematical operations

minCheck = min(1,2,3,500,8,4,2,6)
maxCheck = max(1,2,3,500,8,4,2,6)
print(minCheck) # 1 - returns the smallest
print(maxCheck)# 500 returns the largest
print(min(1,2,3,500,8,4,2,6)) # 1 is also correct

x = abs(-12.05)
print(x) # 12.05 - returns the absolute positive value of the number

print(pow(2,3)) # - 2*2*2:  pow() raises the first arg by the power of the second

#Subtopic: Python Math Module: this is a mathematic module that extends tha maths functions. Import to use

import math

print(math.sqrt(20)) # 4.47213595499958 - square root of the number
print(math.ceil(4.47213595499958)) # 5 - ceil rounds a number (float) to its nearest whole integer
print(math.floor(4.47213595499958)) # 4 - floor rounds the number (float) down to its nearest int
print(math.pi) # 3.141592653589793 - eturns the value of pi

# Full math module reference: https://www.w3schools.com/python/module_math.asp

# NEW TOPIC: PYTHON JSON:
#JSON is a text format syntax for storing and exchanging data. It is writen with Javascript object notation. So Python has the json module that can be imported for the use of json data.JSOn stands for javascript object notation
import json

#Subtopic: Parse JSOn - Converting JSON to Python and Python to JSON
#You can parse a JSON string to python using json.loads() - this will create a dictionary
#You can convert python set, tuple, dict, list, string, float, int, boolean to json using json.dumps()

#a JSON string:
j = '{"foods":"[Garri, Rice]", "sex": "Male", "house":"bungalow", "number":1234}'

#Convert to python

p = json.loads(j)
print(p) # '[Garri, Rice]', 'sex': 'Male', 'house': 'bungalow', 'number': 1234}
print(p["house"]) # bungalow

#Subtopic: Convert Python to Json string

py2JSOn = json.dumps(p)
print(py2JSOn) # {"foods": "[Garri, Rice]", "sex": "Male", "house": "bungalow", "number": 1234}

import json
# These Py data types can be converted to JSON strings;
print(json.dumps('Hello World')) # "Hello World" - str to string (note the double quotes is compulsory for json strings)
print(json.dumps(12345)) # 12345 - int to number
print(json.dumps(100.5))# 100.5 -  float to number
print(json.dumps([12, 'John', "Rabit", "Jesus"]))# list to array - [12, "John", "Rabit", "Jesus"]
#print(json.dumps({'Maths', 'Eng', 'Biology'}))# set causes error so cannot be converted
print(json.dumps(('goat', 'Ram', 'Cow', 'Cat')))# tuple to array - ["goat", "Ram", "Cow", "Cat"]
print(json.dumps({'Status': 'Single', 'Number': 7035719745, 'age':29}))# dict to object - {"Status": "Single", "Number": 7035719745, "age": 29}
print(json.dumps(True))# True - true (note the small letter T to suite Javascript notation)
print(json.dumps(False))# False - false
print(json.dumps(None))# None - null

#Subtopic: Format Result of Conversion of Python to Json:
# If you stringify a long set of data into JSON, everything is packed into a single line which will be too hard to read by humans. Since JSON is supposed to be self-defining(human-readable), this is not good practise. We can format the string to be able to read them easily.

import json
#Define a py dict and stringify it for an example
z =  {
"name":"Anatu",
"Friends": ["Charles", "Fred", "Bernie"],
"Phone-Number": 7035719745,
"height":174.5,
"hobbies": ('Reading', 'Movies')
}
zjson = json.dumps(z) # Stringify
print(zjson)
# {"name": "Anatu", "Friends": ["Charles", "Fred", "Bernie"], "Phone-Number": 7035719745, "height": 174.5, "hobbies": ["Reading", "Movies"]}

#The above has no indentations and line breaks. Now format using the 'indent' keyword parameter to add indentation.

zjson = json.dumps(z, indent=2)
print(zjson)

'''
Result:

{
  "name": "Anatu",
  "Friends": [
    "Charles",
    "Fred",
    "Bernie"
  ],
  "Phone-Number": 7035719745,
  "height": 174.5,
  "hobbies": [
    "Reading",
    "Movies"
  ]
}
'''
# Custom separators can also be added as a parameter after the indent param to

zjson = json.dumps(z, indent=2, separators=(';','='))
print(zjson)

'''
{
  "name"="Anatu";
  "Friends"=[
    "Charles";
    "Fred";
    "Bernie"
  ];
  "Phone-Number"=7035719745;
  "height"=174.5;
  "hobbies"=[
    "Reading";
    "Movies"
  ]
}

'''

#Sorting the json string result: You can also sort the string items using the 'sort_keys' parameter

zjson = json.dumps(z, indent=2, separators=(';','='), sort_keys=True)
print(zjson)

#NEW TOPIC: PYTHON RegEx: RegEx (regular Expression) is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains a specified search pattern

#Subtopic: Regex Module: This is built-in module that can be imported to work with regular expressions

import re

txt = " And who are you the proud lord said that I must bow so low"

txtreg = re.findall("or",txt)
if txtreg:
    print(txtreg)
else:
    print("No match")

#Subtopic: RegEx Functions: These are built-in functions in the re module to allow us search a string for a match. The functions are : findall(), search(), split(), sub().

# Subtopic: Metacharacters: Characters with special meaning. Reference: https://www.w3schools.com/python/python_regex.asp#findall

#Subtopic: Special sequences: A special sequence is \ forllowed by a character. It has special meaning in regex. Reference: https://www.w3schools.com/python/python_regex.asp#findall


#NEW TOPIC: PYTHON PIP: This is the package manager for python modules/packages just like we have npm in javascript. PIP is included by default in py 3.4+.

#A package contains all the files you need for the usage of a module. Modules are python core libraries you can include in your project to perform certain tasks based on the functions in them already.

# To check if pip is installed, pip --version in termianl # pip 22.2.1 from C:\Python310\lib\site-packages\pip (python 3.10)

#Download and install pip if not in your system: If you do not have PIP installed, you can download and install it from this page: https://pypi.org/project/pip/

#Downloading a python pip package for use: Go to the directory on your PC for  for python scripts and open the command line and do : pip install package_name

#eg: C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
#or in my case: C:\Windows\System32\cmd.exe
#Or just open terminal anywhere and install
#Using an installed package is same thing as we have done in modules. refer to the function inside the module by the module name. We have installed CamelCase so let us try it.
import camelcase

x = "hello world, i am learning python"
c = camelcase.CamelCase()
print(c.hump(x)) #Hello World, I Am Learning Python

#Find packages to install in pypi.org

#uninstalling a package can be done in terminal from anywhere or from the folder of installation: pip uninstall package_name

#Check the list of packages installed on your system by: pip list

#NEW TOPIC: PYTHON TRY EXCEPT

# Try block lets you test a block of code for errors
# except block lets you handle the error
# else block lets you execute a code when THERE IS NO ERROR

#Subtopic: Exception handling: When an error/exception occurs while python is running through your code, python will usually stop at the point of the error but you can set it up to
