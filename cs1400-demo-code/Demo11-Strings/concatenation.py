string1 = "Utah State"
string2 = "Aggies"

full_string = string1 + " " + string2

print(full_string)

value = 1

# full_string += value # this doesn't work
full_string += str(value) # convert the number to a string
print(full_string)