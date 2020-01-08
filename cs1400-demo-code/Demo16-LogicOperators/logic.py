print("not Operator")
print(format("X", "^8s") + format("Output", "^8s"))
X = True
print(format(str(X), "^8s") + format(str(not X), "^8s"))
X = False
print(format(str(X), "^8s") + format(str(not X), "^8s"))

print("\n\n")
print("and Operator")
print(format("X", "^8s") + format("Y", "^8s") + format("Output", "^8s"))
X = True
Y = True
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X and Y), "^8s"))
X = True
Y = False
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X and Y), "^8s"))
X = False
Y = True
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X and Y), "^8s"))
X = False
Y = False
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X and Y), "^8s"))

print("\n\n")
print("or Operator")
print(format("X", "^8s") + format("Y", "^8s") + format("Output", "^8s"))
X = True
Y = True
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X or Y), "^8s"))
X = True
Y = False
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X or Y), "^8s"))
X = False
Y = True
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X or Y), "^8s"))
X = False
Y = False
print(format(str(X), "^8s") + format(str(Y), "^8s") + format(str(X or Y), "^8s"))

