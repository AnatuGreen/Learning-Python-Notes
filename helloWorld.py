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

from copy import copy
from pprint import pprint
import random
from struct import calcsize
import this

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

