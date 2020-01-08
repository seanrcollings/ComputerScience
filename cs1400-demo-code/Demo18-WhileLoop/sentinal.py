import random

KEY_VALUE = 35
done = False

while not done:
    rand_val = random.randint(0, 50)
    print("New Value is " + str(rand_val))
    if rand_val == KEY_VALUE:
        done = True