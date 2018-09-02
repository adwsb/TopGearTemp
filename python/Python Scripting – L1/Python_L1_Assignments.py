# 1. What will be the output of 'seclist' in print commands of below code?

mylist = range(4)
seclist = mylist
print seclist
mylist.append(4)
print seclist
seclist = mylist[:]
print seclist
mylist.append(5)
print seclist

# Ans:
# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]

##############################################################################

# 2. What is the output of following code:

def f(n):
	for x in range(n):
		yield x**3
	
for x in f(6):
	print x

# Ans:
# 0
# 1
# 8
# 27
# 64
# 125

##############################################################################

# 3. Write a program to receive a string from keybord and check if the string has two 'e' in the characters.
# If yes return True else False.

import sys

def check_E():
	inp = sys.argv[1]

	if inp.count('e') == 2:
		return True
	else:
		return False



##############################################################################

# 4. What is the output of following code:

counter = 1

def dolots(count):
	global counter
	for i in (1, 2, 3):
		counter = count + i
	
print dolots(4)
print counter

# Ans:
# None
# 7

##############################################################################

# 5. Write a code to read the data from input file called input.txt and count the number of 
# characters per line, number of words per line and write these into output file called as output.txt

import sys
filename = sys.argv[1]

def whatever():
	with open(filename,'r') as rfile:
		with open('output.dat','w') as wfile:
				for line in rfile:
					wfile.write(str(len(line)))
					wfile.write(str(len(line.split())))
			
##############################################################################

# 6. Create 3 Lists ( list1,list2,list3) with numbers and perform following operations
# a) Create Maxlist by taking 2 maximum elements from each list.
# b) Find average value from all the elements of Maxlist.
# c) Create a MinlIst by taking 2 minimum elements from each list
# d) Find the average value from all the elements of Minlist

list1 = [5,14,6,11,9,1,7,3,18]
list2 = [33,5,4,6,81,45,8,63,42,1]
list3 = [41,36,5,8,4,75,86,5,44,7]

list1.sort()
list2.sort()
list3.sort()

Maxlist = [list1[-2:], list2[-2:], list3[-2:]]
Maxlist = [item for sublist in Maxlist for item in sublist]
print(sum(Maxlist)/len(Maxlist))

Minlist = [list1[:2], list2[:2], list3[:2]]
Minlist = [item for sublist in Minlist for item in sublist]
print(sum(Minlist)/len(Minlist))

##############################################################################

# 7. Write program to convert prefix/net mask to IP
# eg: input:16 output: 255.255.0.0

import sys
Mask = int(sys.argv[1])

if Mask >= 0 and Mask <= 32:
	binstr = '1'*Mask + '0'*(32-Mask)
	IP = str(int(binstr[:8],2)) + '.' + str(int(binstr[8:16],2)) + '.' + str(int(binstr[16:24],2)) + '.' + str(int(binstr[24:],2))
	print(IP)  
else:
	print("Mask off limits")

##############################################################################

# 8. Create a suitable data construct to read the data from an xml document as shown below:
# <bookstore shelf="New Arrivals">
# <book category="COOKING">
# <title lang="en">Everyday Italian</title>
# <author>Giada De Laurentiis</author>
# <year>2005</year>
# <price>30.00</price>
# </book>
# <book category="CHILDREN">
# <title lang="en">Harry Potter</title>
# <author>J K. Rowling</author>
# <year>2005</year>
# <price>29.99</price>
# </book>
# <book category="WEB">
# <title lang="en">Learning XML</title>
# <author>Erik T. Ray</author>
# <year>2003</year>
# <price>39.95</price>
# </book>
# </bookstore>

import xml.dom.minidom
import sys

filename = sys.argv[1]

doc = xml.dom.minidom.parse(filename)
print(doc.nodeName)
print(doc.firstChild.tagName)

##############################################################################

# 9. Create a suitable object type and check for file size of 0 bytes of the directory contents as shown below

# 02/15/2016 10:49 PM 962 switchfinal.py
# 02/15/2016 10:49 PM 943 switchfinal.py.bak
# 01/27/2016 11:46 AM 15 t.py
# 03/31/2016 12:39 PM 840 t1.py
# 01/25/2016 10:34 AM 2,407 tc1.py
# 02/14/2017 09:13 AM 0 teat.py
# 03/15/2016 05:52 PM 5 tes.py

import sys
import os
import time
import datetime

dir_list = []
for name in os.listdir('.'):
	temp = []
	temp.append(str(datetime.datetime.strptime(time.ctime(os.path.getmtime(name)), "%a %b %d %H:%M:%S %Y")))
	temp.append(os.stat(name).st_size)
	temp.append(name)
	dir_list.append(temp)
print(dir_list)

print('Empty FIles:')
for i in dir_list:
	if int(i[1]) == 0:
		print(i[2])

##############################################################################

# 10.Create a suitable object type to eliminate the duplicate elements

mylist = set()
mylist.add(1)
mylist.add(2)
mylist.add(1)
mylist.add(3)
print(mylist)