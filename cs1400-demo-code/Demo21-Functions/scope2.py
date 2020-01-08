'''
    Steps:
    1) define func1()
    2) call func1()
    3) call func2() from inside func1()
    4) define func2()
'''

def func1():
    print("Calling func1()")
    func2()


func1()


def func2():
    print("Calling func2()")
    print("This doesn't work because func2() isn't defined before it's used")