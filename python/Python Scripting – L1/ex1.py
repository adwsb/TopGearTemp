import sys
inp = int(sys.argv[1])

whole = inp//10
frac = inp%10

for i in range(whole):
	sys.stdout.write(' '*9 + str(i+1))

print()

for i in range(whole):
	sys.stdout.write("1234567890")

for i in range(frac):
	sys.stdout.write(str(i+1)) 
