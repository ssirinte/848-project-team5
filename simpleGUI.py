from appJar import gui

app = gui("Personal Trainer", "600x400")


#app=gui("Grid Demo", "300x300")
app.setSticky("news")
app.setExpand("both")
app.setFont(20)

app.addLabel("l1", "Heartrate", 0, 0)
app.addLabel("l2", "Reps", 0, 1)
app.addLabel("l3", "Hydration", 0, 2)
app.addLabel("l4", "66 bpm", 1, 0)
app.addLabel("l5", "2", 1, 1)
app.addLabel("l6", "8/10", 1, 2)

app.go()
