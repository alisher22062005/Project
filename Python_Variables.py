#example1
x = 5
y = "John"
print(x)
print(y)

#example2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#example3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#exmaple3
x = "John"
# is the same as
x = 'John'

#example4
x = 5
y = "John"
print(type(x))
print(type(y))

#example5
a = 4
A = "Sally"
#A will not overwrite a


#exercice1
carname="Volvo"


#exercise2
x=50

#exercise3
x=5
y=10
print(x+y)

#exercise4
x=5
y=10
z=x+y
print(z)

#exercise5
x,y,z="Orange", "Banana", "Cherry"


#exercise6
x=y=z="Orange"

#exercise7
def myfunc():
    global x
    x="fantastic"

#Variable names

 #example1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#example2
2myvar = "John"
my-var = "John"
my var = "John"


#Assign Multiple Values

#example1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#example2
x = y = z = "Orange"
print(x)
print(y)
print(z)

#example3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables

#example1
x = "Python is awesome"
print(x)

#example2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#example3
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#example4
x = 5
y = 10
print(x + y)

#example5
x = 5
y = "John"
print(x + y)

#Global Varibales

#example1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#example2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#example3
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#example4
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)







    

  

