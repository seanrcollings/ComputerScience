# Need to import a module to use non-built-in functions
import math
from math import floor # A new import statement

print("Ceiling/Round Up", math.ceil(4.2))
print("Floor/Round Down", floor(7.8)) # No need to use "math."
print("Natural Log", math.log(13.3221))
print("Square Root", math.sqrt(16))
print("Cosine", math.cos(45))