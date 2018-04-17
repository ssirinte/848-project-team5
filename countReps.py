import csv

prevAnalogVal = 0
analogVal = 0
maxOutput = 633
threshold = 550

with open('myoware_data/myoware_data_backpack.csv', 'r+') as file:
	myoware_data = []
	numReps = 0
	lineNum = 1
	startLineNum = 0
	endLineNum = 0
	for line in file:
		prevAnalogVal = analogVal
		analogVal = int(line.strip("\n"))
		if (analogVal < threshold and prevAnalogVal >= threshold):
			startLineNum = lineNum
			print("START VALLEY")
			print("Line #%d" % lineNum)
			print("Rep #%d" % numReps)
			print("Previous analogVal = %d" % prevAnalogVal)
			print("Current analogVal = %d" % analogVal)
			print("--------------")
		elif (analogVal >= threshold and prevAnalogVal < threshold):
			endLineNum = lineNum
			print("END VALLEY")
			print("Line #%d" % lineNum)
			print("Rep #%d" % numReps)
			print("Previous analogVal = %d" % prevAnalogVal)
			print("Current analogVal = %d" % analogVal)
			print("--------------")
			if ((endLineNum - startLineNum) > 50):
				print("VALLEY FOUND FROM: %d to %d", startLineNum, endLineNum)
				numReps += 1
		lineNum += 1
		myoware_data.append(analogVal)


# keep track of duration of curl, sampling rate, etc.
print("# of Total Reps = %d" % numReps)