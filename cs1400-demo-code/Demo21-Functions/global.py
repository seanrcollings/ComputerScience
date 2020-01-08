# var1 is a global variable because it is not defined in a function
var1 = 5
var2 = 50

def func1():
    # change the value of var1. What does it do?
    var1 = 10
    print("Inside func1(): " + str(var1))

def func2():
    global var2
    # change the value of var2. What does it do?
    var2 = 100
    print("Inside func2(): " + str(var2))

print("var1 start: " + str(var1))
func1()
print("var1 after func1(): " + str(var1))

print()

print("var2 start: " + str(var2))
func1()
print("var2 after func2(): " + str(var2))



