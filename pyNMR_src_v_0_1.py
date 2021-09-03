import platform

# Program version
proVer = '0.1'
rlsDate = '2021-09-03'

# Platform determination
osVer = platform.system()

# Program information section
print("*******************************************************************************")
print("*                                                                             *")
print("*                                 p y . N M R                                 *")
print("*                                                                             *")
#print(f"*     =================== Version {proVer} for Source Code ===================     *")

if osVer == 'Darwin':
	print(f"*     ====================== Version {proVer} for macOS ======================     *")
elif osVer == 'Windows':
	print(f"*     ================ Version {proVer} for Microsoft Windows ================     *")
else:
	print(f"*     ====================== Version {proVer} for Linux ======================     *")

print(f"*                          Release date: {rlsDate}                           *")
print("*                                                                             *")
print("*           NMR scaling tool, developed by Zhe Wang. Online document is       *")
print("*          available from GitHub (https://github.com/wongzit/pyNMR).          *")
print("*                                                                             *")
print("*                             -- Catch me with --                             *")
print("*                         E-mail  wongzit@yahoo.co.jp                         *")
print("*                       Homepage  https://wongzit.github.io                   *")
print("*                                                                             *")
print("*******************************************************************************")
print("\nPRESS Ctrl+c to exit the program.\n")

# Input file specification
print("Gaussian output file:")
if osVer == 'Windows':
	fileName = input("(e.g.: C:\\pyNMR\\examples\\benzene.log)\n")
	if fileName.strip()[0] == '\'' and fileName.strip()[-1] == '\'':
		fileName = fileName.strip()[1:-1]
	elif fileName.strip()[0] == '\"' and fileName.strip()[-1] == '\"':
		fileName = fileName.strip()[1:-1]
	else:
		fileName = fileName.strip()
else:
	fileName = input("(e.g.: /pyNMR/examples/benzene.log)\n")
	if fileName.strip()[0] == '\"' and fileName.strip()[-1] == '\"':
		fileName = fileName.strip()[1:-1]
	elif fileName.strip()[0] == '\'' and fileName.strip()[-1] == '\'':
		fileName = fileName.strip()[1:-1]
	else:
		fileName = fileName.strip()

with open(fileName, 'r') as outFile:
	outLines = outFile.readlines()

shielLine = []
for line in outLines:
	if 'Isotropic =' in line and 'Anisotropy =' in line:
		shielLine.append(line.strip())

shielMat = []
for i in shielLine:
	shielEle = []
	shielEle.append(i.split()[0])
	shielEle.append(i.split()[1])
	shielEle.append(i.split()[4])
	shielMat.append(shielEle)

# User determine: elements
eleSym = input("\nPlease specify the element (case-sensitive): ")

eleFlag = 0

for k in range(len(shielMat)):
	if shielMat[k][1] == eleSym:
		eleFlag = 1
	
if eleFlag == 0:
	print(f"\nDid not find element {eleSym}, program termination.\n")
else:
	print("\n  No.      Atom       Sigma (ppm)")
	print("-----------------------------------")
	for j in range(len(shielMat)):
		if shielMat[j][1] == eleSym:
			print(f"  {format(str(shielMat[j][0]).rjust(3))}       {format(str(shielMat[j][1]).rjust(2))}         {format(str(shielMat[j][2]).rjust(9))}")
	print("-----------------------------------")

if eleFlag == 1:
	scaleFlag = input("\nApply scaling fator? (y/n): ")

	if scaleFlag.lower() == 'y':
		while True:
			try:
				slope, intercept = input("\nPlease specify the slope and intercept:\n").split()
				slope = float(slope)
				intercept = float(intercept)
				break
			except ValueError:
				print("\nInput error, please input 2 numbers!")
				continue
	elif scaleFlag.lower() != 'n':
		print("\nInput error, program quit.")

	if scaleFlag.lower() == 'y':
		print("\n  No.      Atom       Delta (ppm)")
		print("-----------------------------------")
		for j in range(len(shielMat)):
			if shielMat[j][1] == eleSym:
				deltaScale = (float(shielMat[j][2]) - intercept) / slope
				print(f"  {format(str(shielMat[j][0]).rjust(3))}       {format(str(shielMat[j][1]).rjust(2))}         {format(str(round(deltaScale, 4)).rjust(9))}")
		print("-----------------------------------")

	printFlag = input("\nSave NMR data to .txt file? (y/n): ")

	if printFlag.lower() == 'y':
		nmrTxt = open(f"{fileName[:-4]}.txt", "w")
		nmrTxt.write("py.NMR, by Zhe Wang\nHomepage: https://wongzit.github.io\n\n\n")
		nmrTxt.write("  - Magnetic Shielding Tensors -\n-----------------------------------\n")
		nmrTxt.write("  No.      Atom       Sigma (ppm)\n-----------------------------------\n")
		for l in range(len(shielMat)):
			if shielMat[l][1] == eleSym:
				nmrTxt.write(f"  {format(str(shielMat[l][0]).rjust(3))}       {format(str(shielMat[l][1]).rjust(2))}         {format(str(shielMat[l][2]).rjust(9))}\n")
		nmrTxt.write("-----------------------------------\n\n\n")
		if scaleFlag.lower() == 'y':
			nmrTxt.write("     - Scaled Chemical Shift -\n-----------------------------------\n")
			nmrTxt.write("  No.      Atom       Delta (ppm)\n-----------------------------------\n")
			for m in range(len(shielMat)):
				if shielMat[m][1] == eleSym:
					deltaScale = (float(shielMat[m][2]) - intercept) / slope
					nmrTxt.write(f"  {format(str(shielMat[m][0]).rjust(3))}       {format(str(shielMat[m][1]).rjust(2))}         {format(str(round(deltaScale, 4)).rjust(9))}\n")
			nmrTxt.write("-----------------------------------\n\n")
		nmrTxt.close()
	elif printFlag.lower() == 'n':
		print("\nProgram quit.")
	else:
		print("\nInput error, program quit.")

print("\n*******************************************************************************")
print("")
print("                        Normal termination of py.NMR.")
print("")
print("*******************************************************************************\n")
