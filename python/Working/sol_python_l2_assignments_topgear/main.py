# 1. Write a code to implement the package  below and distribute it.
# Mathnew package with following modules
# 1. sqroot
# 2. addition
# 3. subtraction
# 4. multiplication
# 5. division

from Mathnew.Mathnew import *

num1 = 4
num2 = 5

print(sqroot(num2))
print(addition(num1, num2))
print(subtraction(num1, num2))
print(multiplication(num1, num2))
print(division(num1, num2))
print("===")

# 2.  Given email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'
# write a regular  expression to extract 
# a. email id
# b. domain name
# c. time

import re

email='From abc.xyz@pqr.com Mon Dec 29 01:12:15 2016'
email_id = re.findall("[\w.]+@[\w].[\w]", email)
print(email_id)
domain_name = re.findall("@[\w]+.", email_id[0])
print(domain_name)
time = re.findall("[\d]{2}:[\d]{2}:[\d]{2}", email)
print(time)
print("===")

# 3.   Write a code to implement the following methods by defining a class called Mymath
# a) without __init__  
# 1. sqroot
# 2. addition
# 3. subtraction
# 4. multiplication
# 5. division

class Mymath:
	num1 = 20
	num2 = 5

	def sqroot(self):
		try:
			return math.sqrt(float(self.num1))
		except:
			print("Exception")

	def addition(self):
		try:
			return float(self.num1) + float(self.num2)
		except:
			print("Exception")


	def subtraction(self):
		try:
			return float(self.num1) - float(self.num2)
		except:
			print("Exception")


	def multiplication(self):
		try:
			return float(self.num1) * float(self.num2)
		except:
			print("Exception")


	def division(self):
		try:
			return float(self.num1) / float(self.num2)
		except:
			print("Exception")

	def setvalues(self,num11,num22):
		self.num1 = num11
		self.num2 = num22


testMath = Mymath()
testMath.setvalues(30,10)
print(testMath.sqroot())
print(testMath.addition())
print(testMath.subtraction())
print(testMath.multiplication())
print(testMath.division())
print("===")

# 4.  Write a code to implement the following methods by defining a class called Mymath
# a) with__init__  
# 1. sqroot
# 2. addition
# 3. subtraction
# 4. multiplication
# 5. division

class Mymath(object):

	def __init__(self,num11,num22):
		self.num1 = num11
		self.num2 = num22


	def sqroot(self):
		try:
			return math.sqrt(float(self.num1))
		except:
			print("Exception")

	def addition(self):
		try:
			return float(self.num1) + float(self.num2)
		except:
			print("Exception")


	def subtraction(self):
		try:
			return float(self.num1) - float(self.num2)
		except:
			print("Exception")


	def multiplication(self):
		try:
			return float(self.num1) * float(self.num2)
		except:
			print("Exception")


	def division(self):
		try:
			return float(self.num1) / float(self.num2)
		except:
			print("Exception")
	

testMath1 = Mymath(100,10)
print(testMath1.sqroot())
print(testMath1.addition())
print(testMath1.subtraction())
print(testMath1.multiplication())
print(testMath1.division())
print("===")

# 5.   Write a code to implement a child class called mathnew and 
# parent classes as sqroot,   addition,subtraction, multiplication and division. 
# Use the super() function to inherit the parent methods.

class sqroot:

	def __init__(self, num11):
		self.num1 = num11

	def sqroot(self):
		try:
			return(math.sqrt(self.num1))
		except:
			pritn("Exception")

class addition:

	def __init__(self, num11, num22):
		self.num1 = num11
		self.num2 = num22

	def addition(self):
		try:
			return(self.num1 + self.num2)
		except:
			print("Exception")

class subtraction:
	def __init__(self, num11, num22):
		self.num1 = num11
		self.num2 = num22

	def subtraction(self):
		try:
			return(self.num1 - self.num2)
		except:
			print("Exception")


class multiplication:
	def __init__(self, num11, num22):
		self.num1 = num11
		self.num2 = num22

	def multiplication(self):
		try:
			return(self.num1 * self.num2)
		except:
			print("Exception")


class division:
	def __init__(self, num11, num22):
		self.num1 = num11
		self.num2 = num22

	def division(self):
		try:
			return(self.num1 / self.num2)
		except:
			print("Exception")

class mathnew(sqroot, addition, multiplication, division, subtraction):
	def __init__(self, num11, num22):
		self.num1 = num11
		self.num2 = num22

	def showall(self):
		print(super().sqroot())
		print(super().addition())
		print(super().subtraction())
		print(super().multiplication())
		print(super().division())
		print("===")

mathobj = mathnew(16,10)
mathobj.showall()

# 6. Write a code to overload __add__ method to perform  2 x 2 matrix addition

class mathnew_AddOverload(sqroot, addition, multiplication, division, subtraction):
	def __init__(self, num11, num22):
		self.num1 = num11
		self.num2 = num22

	def addition(self):
		# function to get input
		mat1 = [[1,2],[3,4]]
		mat2 = [[5,6],[7,8]]
		return(mat1+mat2)

	def showall(self):
		print(super().sqroot())
		print(super().addition())
		print(super().subtraction())
		print(super().multiplication())
		print(super().division())
		print("overloaded :" + str(self.addition()))
		print("===")

mathobj_ov = mathnew_AddOverload(36,25)
mathobj_ov.showall()

# 7. Write a code to compare two string data based on the length of the string hint; __gt__ method

import operator

def strcmp(str1, str2):
	return(operator.__gt__(len(str1),len(str2)))

# 8. Create a class called Circle and write the methods to calculate the area and circumference of a circle given the radius.


class circle:

	def circumference(self,radius):
		return(2*3.14*radius)

	def area(self,radius):
		return(3.14*radius**2)

c5 = circle()
print(c5.circumference(5))
print(c5.area(5))
print("===")


# 9. Write a class called Circle and write the methods to calculate the area and circumference of the circle by initialing the radius of the circle. Hint __init__ method

class circle:

	def __init__(self, radius):
		self.radius = radius

	def circumference(self):
		return(2*3.14*self.radius)

	def area(self):
		return(3.14*self.radius**2)

c5 = circle(5)
print(c5.circumference())
print(c5.area())
print("===")

# 10. Create a class called First and two classes called Second  and Third which inherit from First. Create class called Fourth which inherits from Second and Third. Create a common method called method1 in all the classes and provide the Method Resolution Order

class first:
	def method1(self):
		print("first class")

class second:
	def method1(self):
		print("second class")

class third(first, second):
	def method1(self):
		print("third class")

obj = third()
obj.method1()