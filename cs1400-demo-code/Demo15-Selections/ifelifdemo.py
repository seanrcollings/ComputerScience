score = input("What is your score? ")

if score.isdigit():
    score = eval(score)

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")
else:
    print("Your input is not valid")