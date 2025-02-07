#Datatypes:Data types in Python are classifications of data items that define the type of data a variable can store. They help programmers specify what operations can be performed on a particular piece of data. 




#numeric:int,float,complex,boolean
#Sequence:List,Tuple,String,Range
#set
#dictionary
# None
# 3 ways to run a python code"

# way1:IDLE po CMD 
# Way2: Notepad
# Way 3:Development platforms

# DataType in python :
# Rules for Python variables: A variable name must start with a letter or the underscore character. A variable name cannot start with a number. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

#Complex Numbers:
cmp1=5+3j
cmp2=6-5j
print(cmp1 + cmp2)
print(cmp1 - cmp2)

print(cmp1/cmp2)
# print(cmp1%cmp2) Not working 
print(cmp1*cmp2)
# print(cmp1 // cmp2)  not working
print(cmp1 ** cmp2)

# Boolean -True/False
print(2<3)
print(5>=3)

bool=True
print(type(bool))
print(type(False))

print(int(True)) #HERE WE ARE CONVERTING  THE TRUE INTO INT I.E 1
print(int(False)) #HERE WE ARE CONVERTING  THE FALSE INTO INT I.E 0

#Sequence:List,Tuple,String,Range
# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:[]
list1=[1,2,3,4,5,[6,7,8,9],"python"]
print(type(list1))
print(list1[4])
print(list1[len(list1)-1])
print(list1[-1])
print(list1[2:3])
print(list1[3:2]) # direction flow wrong so we can give  print(list1[3:2:-1]) to reverse direse direction if u give -2 direction will chnage and it skips the one index.
print(list1[:])
print(list1[2:-2])
print(list1[-1:-5])
print(list1[2:8:2])
print(list1[-1:-5:-1])

#list of index of index:
print(list1[5][2])
#another way:
temp=list1[5]
print(temp[2])
#for loop:
for i in list1:
    print(i)
    # Changing  multiple list values:
    list1[3],list1[4]="hy",7
    list1[-3],list1[-4]="hloo",0
    # tuple is immutable BUT LIST is mutable
    # tuple is faster than List because immutable 
    # Syntax Difference
    tupl=(1,2,True,"python",5)
    print(tupl)
    tup1=(1,3)
    print(tupl[1])
    # tupl[2]="hieee" TypeError: 'tuple' object does not support item assignment because Tuple is immutable
    print(tupl[-1])
    print(tup1[2:5])

    #Range
    # print(range(0,100)) o/p is range(0, 100) so we need convert into tuple or list
    print(list(range(0, 100)))
    print(list(range(100,0))) #it gives [] so we can add -1
    print(list(range(100,0,-1))) # it will print 100-0
    print(list(range(100,0,-2))) #skips 1 number between all
    
    









