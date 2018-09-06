import math

def sqroot(num):
	try:
		return math.sqrt(float(num))
	except:
		print("Exception")

def addition(num1, num2):
	try:
		return float(num1) + float(num2)
	except:
		print("Exception")


def subtraction(num1, num2):
	try:
		return float(num1) - float(num2)
	except:
		print("Exception")


def multiplication(num1, num2):
	try:
		return float(num1) * float(num2)
	except:
		print("Exception")


def division(num1, num2):
	try:
		return float(num1) / float(num2)
	except:
		print("Exception")

