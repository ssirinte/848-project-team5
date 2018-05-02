import csv
import serial
import threading

outputVar = [0,1,2]

def repsCount(var):
	prevAnalogVal = 0
	analogVal = 0
	maxOutput = 633
	threshold = 450

	ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
	myoware_data = []
	numReps = 0
	lineNum = 1
	startLineNum = 0
	endLineNum = 0

	prevAnalogVal2 = 0
	analogVal2 = 0
	numReps2 = 0
	lineNum2 = 1
	startLineNum2 = 0
	endLineNum2 = 0
	print("hello I am running")

	while True:
		line = (ser.readline())
		prevAnalogVal = analogVal
		vals = line.strip('\n').split(',')
		analogVal = int(vals[0])
		bpm = int(vals[1])
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
				print("VALLEY FOUND FROM: %d to %d" % (startLineNum, endLineNum))
				numReps += 1
				print("Current heartrate: %d" % bpm)


		if (analogVal2 < threshold and prevAnalogVal2 >= threshold):
			startLineNum2 = lineNum2
		elif (analogVal2 >= threshold and prevAnalogVal2 < threshold):
			endLineNum2 = lineNum2
			if ((endLineNum2 - startLineNum2) > 50):
				numReps2 += 1
		var[0] = numReps
		var[1] = numReps2
		var[1] = bpm
		lineNum += 1
		myoware_data.append(analogVal)

threading.Thread(target=repsCount, args=(outputVar,)).start()