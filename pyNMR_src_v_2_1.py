import platform
import openpyxl

# Program version
proVer = '2.1'
rlsDate = '2021-09-06'

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

nmrMin = -0.5
nmrMax = 10.5
nmrSplit = 0.001
nmrFwhm = 0.01

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
		scaleMat = []
		for j in range(len(shielMat)):
			if shielMat[j][1] == eleSym:
				deltaScale = (float(shielMat[j][2]) - intercept) / slope
				scaleMat.append(deltaScale)
				print(f"  {format(str(shielMat[j][0]).rjust(3))}       {format(str(shielMat[j][1]).rjust(2))}         {format(str(round(deltaScale, 4)).rjust(9))}")
		print("-----------------------------------")

	print("\nA .txt file will be saved at same dictionary with the output file.")
	nmrTxt = open(f"{fileName[:-4]}_peak_info.txt", "w")
	nmrTxt.write("Saved with py.NMR by Zhe Wang\nHomepage: https://wongzit.github.io\n\n\n")
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

	if scaleFlag.lower() == 'y':
		while True:
			print("\n===============================================================")
			print("         Scaled NMR spectrum will be saved in .xlsx file")
			print("---------------------------------------------------------------")
			print(f"       1 - Spectrum range: from {nmrMax} to {nmrMin} ppm")
			print(f"       2 - Peak half-width at half height: {nmrFwhm} ppm")
			print("===============================================================")
			print("Press ENTER to use current setting, or input menu number")
			paraInp = input("  to modify the parameters: ")
			if paraInp == '':
				break
			elif paraInp == '1':
				while True:
					try:
						nmrMax, nmrMin = input("\nPlease specify the range from MAX to MIN:\n").split()
						nmrMax = float(nmrMax)
						nmrMin = float(nmrMin)
						if nmrMax < nmrMin:
							nmrInt = nmrMax
							nmrMax = nmrMin
							nmrMin = nmrInt
						elif nmrMax == nmrMin:
							nmrMax = 9.5
							nmrMin = -0.5
						break
					except ValueError:
						print("\nInput error, please input 2 numbers!")
						continue
			elif paraInp == '2':
				while True:
					try:
						nmrFwhm = input("\nPlease specify the half-width at half height:\n")
						nmrFwhm = float(nmrFwhm)
						break
					except ValueError:
						print("\nInput error, please input a number!")
						continue
			else:
				print("Input error, py.NMR will use default value.\n")
				break
		
		yAxMat = []
		xAx = round(nmrMin, 3)
		while xAx <= nmrMax:
			yAx = 0.0
			for m in range(len(scaleMat)):
				yAx += nmrFwhm / (6.283185306 * (xAx - scaleMat[m]) * (xAx - scaleMat[m]) + 1.570796327 * nmrFwhm * nmrFwhm)
			yAxMat.append(yAx)
			xAx = round(xAx + nmrSplit, 3)
		yAxRe = list(reversed(yAxMat))
		xAx2 = round(nmrMin, 3)
		xAxMat = []
		while xAx2 <= nmrMax:
			xAxMat.append(xAx2)
			xAx2 = round(xAx2 + nmrSplit, 3)
		xAxRe = list(reversed(xAxMat))
		outWB = openpyxl.Workbook()
		outWS = outWB.active
		outWS['A1'] = 'Chemical Shift (ppm)'
		outWS['B1'] = 'Intensity'
		excelDatas =[]
		for s in range(len(xAxRe)):
			excelData = []
			excelData.append(xAxRe[s])
			excelData.append(yAxRe[s])
			excelDatas.append(excelData)
		for line in excelDatas:
			outWS.append(line)
		outWB.save(f'{fileName[:-4]}_spectrum_data.xlsx')

print("\n*******************************************************************************")
print("")
print("                        Normal termination of py.NMR.")
print("")
print("*******************************************************************************\n")
