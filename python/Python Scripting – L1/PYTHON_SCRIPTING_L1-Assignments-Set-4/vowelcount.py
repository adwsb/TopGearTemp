import sys

filename = sys.argv[1]
with open(filename, "r") as f:
	inpstring = f.read()

def vowelCount(str):
	vowel = set("aeiouAEIOU")
	ctr = 0
	for alpha in str:
		if alpha in vowel:
			ctr += 1
	return ctr

words = inpstring.split()
maxVcount = 0


for i in words:
	if i.isalpha():
		if maxVcount < vowelCount(i):
			maxVcount = vowelCount(i)

for i in words:
	if vowelCount(i) == maxVcount:
		print(str(maxVcount)+ " " + i)
