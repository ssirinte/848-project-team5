# main.py

import settings
from appJar import gui
from countReps import outputVar
app = gui("Personal Trainer", "600x400")

app.setBg("lightBlue")

#app=gui("Grid Demo", "300x300")
app.setSticky("news")
app.setExpand("both")
app.setFont(20)
app.addLabel("l1", "Heartrate", 0, 0)
app.addLabel("l2", "Reps 1", 0, 1)
app.addLabel("l3", "Reps 2", 0, 2)
app.addLabel("heartRate", "66 bpm", 1, 0)
app.addLabel("rep1", "2", 1, 1)
app.addLabel("rep2", "8", 1, 2)

def press():
	return
	
app.addButtons( ["Reset", "Pause"], press, colspan=3)

# def press(btn):
# 	resetVal = x[0]
# 	print resetVal

# app.addButton("Reset", press)

def getNewValue():
	myo = outputVar[0]
	myo2 = outputVar[1]
	heart = outputVar[2]
	#print("in getNewValue resetVal: %d" % resetVal)
	app.setLabel("rep1",str(myo))
	app.setLabel("rep2",str(myo2))
	app.setLabel("heartRate",("%d bpm" % heart))


#app.registerEvent(getNewValue)

app.go()