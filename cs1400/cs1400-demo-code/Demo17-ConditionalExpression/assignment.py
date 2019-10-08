input = eval(input("Enter an integer: "))

# Long Way
if input > 100:
    message = "big"
else:
    message = "small"
print("That number is " + message)

# Conditional Expression
print("\nConditional Expression")
message = "big" if input > 100 else "small"
print("That number is still " + message)