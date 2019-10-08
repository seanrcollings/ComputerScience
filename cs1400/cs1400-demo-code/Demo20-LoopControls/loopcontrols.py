for i in range(0, 10):
    if i % 2 == 0:
        continue
    for j in range(0, 10):
        print(str(i) + ": " + str(j))
        if j == 5:
            continue
        print("got here")