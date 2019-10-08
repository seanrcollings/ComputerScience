import random

while True:
    val = random.randint(0, 20)
    print("The value is", val)
    if val == 10:
        continue

print("You escaped the infinite loop (but you never really will)")