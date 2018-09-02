import sys
filename = sys.argv[1]

with open(filename,"r") as infile:
	for line in infile:
		if line.strip():
			sys.stdout.write(line)
