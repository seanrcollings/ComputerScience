# var1 is a global variable because it is not defined in a function
var1 = 5

def func():
    # var2 is a local variable because it is defined in a function
    var2 = 10
    # Can print both global and local variables in a function
    print(var1)
    print(var2)

print(var1)
# local variables cannot be accessed outside of the function
print(var2)
