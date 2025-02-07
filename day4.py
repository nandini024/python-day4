# # Whyt Strings Are immmutable in Python:
# # 1. Memory Optimization
# # Strings in Python are stored in a pool (string interning) to optimize memory usage.
# # If strings were mutable, modifying one string could affect multiple references, leading to unintended side effects.

# s1 = "hello"
# s2 = "hello"
# print(s1 is s2)  # True (Both refer to the same memory location)
# print(id(s1))
# print(id(s2))

# # sets : A set in Python is an unordered collection of unique elements. It is defined using curly braces {} or the set() function.
# # Key Features of Sets
# # Unordered – No specific order of elements.
# # Unique Elements – Duplicates are automatically removed.
# # Mutable – You can add or remove elements.
# # Unindexed – No indexing like lists or tuples.
# # Supports Set Operations – Union, intersection, difference, etc.







# dic= {}
# print(type(dic))
# set={5}
# # print(type(set))  based on the values provied  in between { } Interrupter will decide the whether set or dictionary
# # DICTIONARY:
# # A dictionary in Python is a mutable, unordered collection of key-value pairs, where each key must be unique and immutable
# #  (like a string, number, or tuple). Dictionaries are optimized for fast lookups, insertions, and deletions using hashing.
# dic1={1:'nandini',2:"priya",5:"karthik"} 
# print(dic1) #{1: 'nandini', 2: 'priya', 5: 'karthik'}
# #if you give dublecate :
# dic2={1:'nandini',2:"priya",2:"ramya",5:"karthik"} 
# print(dic2[2])
# print(dic2) # if you give Different values for   same key it will take updated value for that key
# # If you assign different values to the same key in a dictionary, the last assigned value will overwrite the previous ones because dictionary keys must be unique.
# #Example -2
# dic3 = {1: "apple", 2: "banana", 2: "cherry", 3: "grape"}
# print(dic3[2])  

# # output:{1: 'nandini', 2: 'ramya', 5: 'karthik'}
# # cherry

# # None:The None keyword in Python is a data type and an object of the NoneType class. The None keyword is used for defining a null variable or an object in Python.
# #  None can be assigned to any variable, but new NoneType objects cannot be created. 
# atr1=None
# print(id(atr1))


# # TypeCasting:
# num1=5.9
# num1=int(num1)
# print(num1) #here num1=5
# num1=float(num1)#then float is apply to 5 then it will show 5.0
# print(num1)# it takes always the updated value

# #String to List :
# Str1=" hyy ..!karthik ....."
# print(list(Str1))  #o/p:[' ', 'h', 'y', 'y', ' ', '.', '.', '!', 'k', 'a', 'r', 't', 'h', 'i', 'k', ' ', '.', '.', '.', '.', '.']
# # we can't convert rane to String

# print(bool(-3)) #truthy values
# # Any values 

# print(bool(0)) #Falthy values
# print(bool(''))  #Falthy values
# print(bool([]))  #Falthy values

# #complex to booelan:
# print(bool(0+0j))  #falsy values


# # num1=5
# # print(float(num1))
# # print(num1)

# # n1=input("enter a number")
# # n2=input("enter another number") 
# print(n1+n2)
# print(type(n1)) # by defalut input will be String Type

# # # programme:2
# # m=input("enter A String")
# # m1=input("enter second String")
# # print(m+m1)
# # #programme -3
# # k=input("enter first String")
# # k1=input("enter second String")

# # print(k+k1)

# # Naming Conventions:
# #Pascal Case-manhumanbeing  -ManHumanBeing
# #Camel Case:manHumanBeing 
# #Snake-Case:man_human_being  all small but seperated by underscore

# # THere is no Constant Concept in Python Represent with Capital letter when you want to use some word as Const.

# #Try to give meaningful names to Variables

# # Type convertions:

# n1=3
# print(int(n1))
# print(n1)
# ini-int
n1=3
print(int(n1))
n1=int(n1)

# int-float
n1=3
print(float(n1))
n1=int(n1)
# int-str
n1=3
print(str(n1))
n1=int(n1)
# int-list:
n1=3
# print(list(n1))  false TypeError: 'int' object is not iterable
n1=int(n1)
# int-set
n1=3
# print(set(n1)) TypeError: 'int' object is not iterable
n1=int(n1)
# int-bool
n1=3
print(bool(n1)) #true
n1=int(n1)
# int-range:
n1=3
print(bool(n1))# true
n1=int(n1)
# int-complex:
n1=3
print(complex(n1))
n1=int(n1)

# Float Conversions :::
# float-int=true
n1=5.0
n1=int(n1)
print(n1)
# float-float
n1=5.0
n1=float(n1)
print(n1)

n1=5.0
n1=str(n1)
print(n1)

n1=5.0
# n1=list(n1) TypeError: 'float' object is not iterable
print(n1)
# f-tuple :
n1=5.0
# n1=tuple(n1) TypeError: 'float' object is not iterable
print(n1)
# f-bool
n1=5.0
n1=bool(n1)
print(n1)

n1=5.0
# n1=range(n1) TypeError: 'float' object cannot be interpreted as an integer
print(n1)
# f-complex
n1=5.0
n1=complex(n1)
print(n1)

# STRing Convertions:
n1="Hello"
# n1=(int(n1))
# print(n1)
#  ValueError: invalid literal for int() with base 10: 'Hello'

# ftr-float:

n1="Hello"
# n1=(float(n1)) ValueError: invalid literal for int() with base 10: 'Hello'
print(n1)

n1="Hello"
n1=(str(n1))
print(n1)
# str-list:
n1="Hello"
# n1=(list(n1)) ['H', 'e', 'l', 'l', 'o'
print(n1)
# str-tuple:::
n1="Hello"
# n1=(tuple(n1))  ('H', 'e', 'l', 'l', 'o')
print(n1)
# str-bool 
n1="Hello"
n1=(bool(n1)) #true
print(n1)
# str-range:::
n1="Hello"
# n1=(range(n1)) #TypeError: 'str' object cannot be interpreted as an integer
print(n1)

# str-dic :::
n1="Hello"
# n1=(dict(n1)) #true ValueError: dictionary update sequence element #0 has length 1; 2 is required
print(n1)

# List Conversations:

list1=[1,2,5,6,["tyuj"],6]
# list1=(int(list1)) false
print(list1)
# float:
list1=[1,2,5,6,["tyuj"],6]
# list1=(float(list1)) false
print(list1)
# str :
list1=[1,2,5,6,["tyuj"],6]
list1=(str(list1))  #[1, 2, 5, 6, ['tyuj'], 6]
print(list1)

# tuple:
list1=[1,2,5,6,["tyuj"],6]
list1=(tuple(list1))   #true
print(list1)
# dict:
list1=[1,2,5,6,["tyuj"],6]
# list1=(dict(list1))  #false
print(list1)
#bool :
list1=[1,2,5,6,["tyuj"],6]
list1=(bool(list1))  #True
print(list1)
# set
list1=[1,2,5,6,["tyuj"],6]
# list1=(set(list1))  #false
print(list1)

# DICTIONARY CONVERTIONS
# INT:
dic={1:"ertyu",2:"ert",3:"ertyhu"}
# dic=(int(dic)) false
print(dic)
# float:
dic={1:"ertyu",2:"ert",3:"ertyhu"}
# dic=(float(dic)) false
print(dic)
#str
dic={1:"ertyu",2:"ert",3:"ertyhu"}
dic=(str(dic)) # true
print(dic)
#list
dic={1:"ertyu",2:"ert",3:"ertyhu"}
dic=(list(dic))  # true
print(dic)
#bool:
dic={1:"ertyu",2:"ert",3:"ertyhu"}
dic=(bool(dic))  # true
print(dic)
# complex
dic={1:"ertyu",2:"ert",3:"ertyhu"}
# dic=(complex(dic))  # false
print(dic)
# BOOLEAN CONVERSIONS:
#int
bool=True
bool=(int(bool)) #true
print(bool)
#float:
bool=True
bool=(float(bool)) #true
print(bool)
# str
bool=True
bool=(str(bool)) #true
print(bool)
#bool
bool=True
# bool=(bool(bool)) #true
print(bool)
# range
bool=True
bool=(range(bool)) #true
print(bool)
# complex
bool=True
bool=(complex(bool)) #true
print(bool)

# list
bool=True
# bool=(list(bool)) #false
print(bool)
# set
bool=True
# bool=(set(bool)) #false
print(bool)



#tuple
bool=True
# bool=(tuple(bool)) #false
print(bool)

# Range CONVERTIONS:
# Range-int:
r = range(5, 10)  # Range from 5 to 9
r = int(r[0])   # Get the first number (5) True
print(r)
# Range-float:
r = range(5, 10)  # Range from 5 to 9
r = float(r[0])   # Get the first number (5) True 5.0
print(r)
#range:bool:
r = range(5, 10)  # Range from 5 to 9
# r = bool(r)   #  false
print(r)
# RANGE-str:
r = range(5, 10)  # Range from 5 to 9
r = str(r)   # Get the first number (5) True
print(r)
# Range-list: 
r = range(5, 10)  # Range from 5 to 9
r = list(r)   #  true
print(r)
#Range -tuple:
r = range(5, 10)  # Range from 5 to 9
r = tuple(r)    #true
print(r)
print(r)
# range-complex:
r = range(5, 10)  # Range from 5 to 9
# r = complex(r)   #false
print(r)
# range-dict
r = range(5, 10)  # Range from 5 to 9
# r = dict(r)   #false
print(r)
#range-set
r = range(5, 10)  # Range from 5 to 9
r = set(r)  #true
print(r)


# COMPLEX CONVERTIONS:
# complex-String:
c = 3 + 4j
c = str(c)
print(c) 
# complex-int
c = 3 + 4j
# c = int(c) false
print(c) 
# complex-float
c = 3 + 4j
# c = float(c) false
print(c) 

# complex-bool:
c = 3 + 4j
# c = bool(c)   false
print(c) 
# complex-list:
c = 3 + 4j
# c = list(c)  false
print(c) 
# complex-dict:
c = 3 + 4j
# c = dict(c) # false
print(c) 
# complex-list:
c = 3 + 4j
# c = set(c)  false
print(c) 
# complex-list:
c = 3 + 4j
# c = tuple(c)  false
print(c) 


























