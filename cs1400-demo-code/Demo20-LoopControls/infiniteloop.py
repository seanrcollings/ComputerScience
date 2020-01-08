import random

while True:
    val = random.randint(0, 20)
    print("The value is", val)
    if val == 10:
        break

print("You escaped the infinite loop")