import sys
n = int(sys.argv[1])
coef = []

def binomialCoeff(n, k) :
    res = 1
    if (k > n - k) :
        k = n - k
    for i in range(0 , k) :
        res = res * (n - i)
        res = res // (i + 1)
    return res

def genPascal(n) :
    for line in reversed(range(0, n)):
        for i in range(0, line + 1) :
        	coef.append(binomialCoeff(line, i))

def printPascal(coef, n):
	ctr = 0
	for i in reversed(range(1, n+1)):
		for j in range(0, n-i+1):
			sys.stdout.write(" ")
		for k in range(0, i):
			sys.stdout.write(str(coef[ctr]) + " ")
			ctr += 1
		print()


genPascal(n)
printPascal(coef, n)
