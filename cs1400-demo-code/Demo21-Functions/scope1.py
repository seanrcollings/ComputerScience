'''
    Steps:
    1) define func1()
    2) define func2()
    3) call func1()
    4) call func2() from inside func1()
'''

def func1():
    print("Calling func1()")
    func2()


def func2():
    print("Calling func2()")
    print("This works because everying is defined before it's used")


func1()