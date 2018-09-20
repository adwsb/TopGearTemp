import sys
filename = sys.argv[1]
Width = int(sys.argv[2])

with open(filename,"r") as ifile:
	with open("output.txt","w") as ofile:
		
		for line in ifile:
			N = len(line.split())
			N_Alpha = 0
			
			for i in line.split():
				N_Alpha += len(i)

			N_Space = Width - N_Alpha
			N_Word_Spacing = N_Space/N
			N_Extra_Spacing = N_Space%N

			Opstring = ""

			print(N_Alpha, N_Space)

			for i in range(N):
				Opstring = Opstring + line.split()[i]
				Opstring = Opstring + ' '*int(N_Word_Spacing)

				if N_Extra_Spacing > 0:
					Opstring = Opstring + ' '
				N_Extra_Spacing -= 1

			ofile.write(Opstring + '\n')



