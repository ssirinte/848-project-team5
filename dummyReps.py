# dummyReps.py

# import settings
# import time

# val = 0

# while True:
# 	time.sleep(1)
# 	val +=1
# 	settings.reps = val
# 	print("Updated: %d" %val)

import time
import threading

x = [0,1]

def update_var(var):
    while True:
        var[0] += 1
        var[1] += 2
        time.sleep(2.0)

threading.Thread(target=update_var, args=(x,)).start()
