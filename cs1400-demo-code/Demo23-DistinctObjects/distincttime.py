import time
import random

time1 = time.time()
time.sleep(random.random() * 10)
time2 = time.time()

# Two objects, same type
print(time1, id(time1), type(time1))
print(time2, id(time2), type(time2))