score = input("What is your score? ")

if score.isdigit():
    score = eval(score)

    if score >= 90:
        print("A")
    else:
        if score >= 80:
            print("B")
        else:
            if score >= 70:
                print("C")
            else:
                if score >= 60:
                    print("D")
                else:
                    print("F")
else:
    print("Your input is not valid")