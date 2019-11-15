from random import randint

counts = [0] * 10
for num in range(1000):
    counts[randint(0, 9)] += 1

for index, count in enumerate(counts):
    print("{} occured {} times".format(index, count))
