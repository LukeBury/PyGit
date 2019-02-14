__author__ = 'lukebury'

# Comment Comment Comment

print("Hellllooo!!!")

#----------------------------------------------------------------------------------------------------------------------
#                                                 Basics
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Basics ----------------------------------------")
'''

x= 10

y= 10.0
yy = float(10)

str = '\nHey'
strr = "\nOh, Hey"
strrr = "\nDon't\n"
print (str,strr,strrr)
print str,strr,strrr

x,y = 0,'O'
print(x," ",y)
'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 Lists
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Lists ----------------------------------------")
'''
# Lists can contain any type of variable, and as many as you wish

print("\n")
mylist = [3,4,5,"SD"]
mylist.append(2)
mylist.append("Luke")
print(mylist)
print mylist
print(mylist[0],"\n")
'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 Operators
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Operators ----------------------------------------")
'''
x = (3+3+3)/3.00
print(x)

# Remainder = %
rem = 11%3   # = 2
print rem
# Power = **
cub = 4**3
print(cub)

# Operators w/ Strings
helloworld = 'hello' + " " + "world"
print helloworld
# Operators w/ Lists
evens = [2,4,6]
odds  = [1,3,5]
all   = odds + evens
     # = [1,3,5,2,4,6]
print all
print("%s" %(evens))
'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 String Formatting and Manipulation
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- String Formatting and Manipulation ----------------------------------------")
'''
# %s - String (or any object with a string representation , like numbers
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot
# %x/%X - Integers in hex representation (lowercase/uppercase)

name = "Luke"
#print ("Hey, %s!" %name)
#^ prints: Hey, Luke!

age = 26
print("%s is %d years old." %(name,age))
#^ prints: Luke is 23 years old.

# Works with lists as well
#print("%s" %evens)
#^ prints: [2, 4, 6]

# String Length
#print(len(name))
#^ prints: 4

#print(name.index("k"))
#^ Prints location of the first "k"

#print(name.count("u")) #counts the number of "u's"

#print(name[2:3]) #prints the integers 2-3. If you want to start at the end, use a (-). Ex: -3 is the 3rd from the end
'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 Conditions
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Conditions ----------------------------------------")
'''
x=2
name = "Luke"
#print(x==2) prints out True
#print(x==3) prints out False
#print(x<3) prints out True

if name == "Luke" and x == 2:
    print("My name is %s and the number is %d" %(name,x))
if name == "Luke" or  x == 3:
    print("Either your name is %s or the number is 3" %name)

# the "in"
if name in ["Luke","Jake"]:
    print("Your name is either Luke or Jake\n")

# if
# elif
# else

# "not" inverts booleans. Ex: (not False) = True
'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Loops
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Loops ----------------------------------------")
'''
### For
for i in range(1,10):
    print(i)  #prints 1:9

for n in range(1,10,2):
    print(n)  #prints 1,3,5,7,9


### While
count = 0
while count <5:
    print(count)
    count += 1 #same as count = count + 1
#^: prints: 0;1;2;3;4


### Break
count = 0
while True:
    print (count)
    count +=1
    if count >=3:
        break
#^ prints: 0;1;2

'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Functions
#----------------------------------------------------------------------------------------------------------------------

print("\n\n---------------------------------- Functions ----------------------------------------")
'''
def MyFunc(arg1,arg2):
    print("The func shall be within you")
    print(arg1)
    print(arg2)

    return arg1+5  # Still not totally sure how to use this... this alone doesn't do anything

MyFunc(3,"Kdot")

# To declare a function which receives a variable number of arguments:
def MyFunc2(arg1, *args):
    print("First: %s" % arg1)
    print("Others: %s" % list(args))

MyFunc2("Hello","Luke","How's","It","Going?")
'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 Classes and Objects
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Classes and Objects ----------------------------------------")
'''
# Objects are an encapsulation of variables and functions into a single entity
# Objects get their variables and functions from classes
# Classes are essentially a template to create your objects

class Classy:
    var1 = "Sodak"

    def function(self,num):
        print("This is a message inside the class. Object%d" %num)

Object1 = Classy() # Now the variable 'Object1' holds an object of the class "Classy" that contains the variable and function defined within Classy
print(Object1.var1) # prints "Sodak"
Object1.function(1) # prints "This is a message inside the class. Object1"

Object2 = Classy() # This second object now has all the same vars and function given by Classy
Object2.var1 = "Nodak" # This object's "var1" has been changed from Sodak to Nodak
print(Object2.var1) # prints "Nodak"
Object2.function(2) # prints "This is a message inside the class. Object2"

'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 Dictionaries
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Dictionaries ----------------------------------------")
'''
# Dictionaries are similar to arrays, but use keys instead of indexes.. but NOT ordered!!!
FavCol = {}
FavCol["Luke"] = "Yellow"
FavCol["Jake"] = "Dark Black"
FavCol["Connor"] = "Blue"
FavCol["Mac"] = 4336

print FavCol.keys()

print(FavCol)
#Could also do:
#FavCol = {
#    "Luke"   : "Yellow"
#    "Jake"   : "Dark Black"
#    "Connor" : "Blue"
#    "Mac"    : 4336
#}
'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Modules and Packages
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Modules and Packages ----------------------------------------")
'''
# Modules are Python files which implement a set of functions
# Modules are imported using the "import" command
# Ex: "import urllib"

# The "dir" and "help" functions are very important for exploring different modules

# Use "dir" to look for which functions are implemented in each module
# Ex: import urllib
#     dir(urllib)
import numpy
print dir(numpy)
# When you find the function in the module you want to use, use "help" to read more about it
# Ex: help(urllib.urlopen)

# To write your own Module, create a new .py file with desired Module name, then import it

'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Generators
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Generators ----------------------------------------")
'''
import random


def lottery(): # produces 6 numbers between 1 and 40, then 1 number between 1 and 15
    for i in range(6):
        a = random.randint(1,40)
    b = random.randint(1,15)
    return a,b

def lottery(): # produces 6 numbers between 1 and 40, then 1 number between 1 and 15
    for i in range(6):
        yield random.randint(1,40)
    yield random.randint(1,15)

for RandNum in lottery():
    print("And the next number is... %d!" %RandNum)
'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 List Comprehensions
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- List Comprehensions ----------------------------------------")
'''
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()  # words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
word_lengths = [] # initiating list
for word in words:
    if word != "the": # if the word is not "the"...
        word_lengths.append(len(word)) # word_lengths = [5, 5, 3, 5, 4, 4, 3]

# Shortening the process using List Comprehension
# Here, we get the length of each word that isn't "the"
word_lengths2 = [len(word) for word in words if word != "the"] # word_lengths = [5, 5, 3, 5, 4, 4, 3]

print word_lengths
print word_lengths2

'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Exception Handling
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Exception Handling ----------------------------------------")
'''
def Print_Number(n):
    print(n)

MyList = (1,2,3,4,5)

for i in range(11):
    try:
        Print_Number(MyList[i])
    except IndexError:           # for loop routes to here when index error is encountered
        Print_Number(0)
#^ Prints: 1;2;3;4;5;0;0;0;0;0;0
'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Sets
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Sets ----------------------------------------")
'''
# Sets are lists with no duplicate entries

print (set("my name is luke because luke is my name".split())) # Only prints unique words and seperates them

a = set(["Luke","Jake","Connor","Charlie","Taylor"])
b = set(["Jake","Charlie","Liz","Sarah"])

## intersection
print(a.intersection(b)) # Prints list with "Charlie" and "Jake", the common names

## symmetric_difference
print(a.symmetric_difference(b)) # Prints all names that are unique to one list or the other (not shared)

## difference
print(a.difference(b)) # Prints names in list a that are not also in b (basically just a portion of symmetric diff)

## union
print(a.union(b)) # Prints list of all names
'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Serialization (JSON)
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Serialization (JSON) ----------------------------------------")
'''
import json
json_string = json.dumps([1,2,3,"a","b","c"])

print(json_string)
'''
#----------------------------------------------------------------------------------------------------------------------
#                                                 Matrix
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Matrix ----------------------------------------")
'''

mat = [[0 for x in range(5)] for x in range (5)]
for i in range(5):
    print(mat[i])

print "\n"

print mat[2]
'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 Partial Functions
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Partial Functions ----------------------------------------")
'''
from functools import partial

def multiply(x,y):
    print(x)
    print(y)
    return x*y

dbl = partial(multiply,2) # to the function "multiply", pass "2" and whatever else is passed to "dbl" (4, below)
print(dbl(4))
'''

#----------------------------------------------------------------------------------------------------------------------
#                                                 Code Introspection
#----------------------------------------------------------------------------------------------------------------------
print("\n\n---------------------------------- Code Introspection ----------------------------------------")
'''
### list of functions and utilities for Code Introspection:
#help()
#dir()
#hasattr()
#id()
#type()
#repr()
#callable()
#issubclass()
#isinstance()
#__doc__
#__name__


'''













