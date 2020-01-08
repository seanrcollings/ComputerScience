# Import the entire path to the module
# Note there is no '-' in the file name like all
# other demos. - doesn't work in directory name for imports
import Demo22Modules.prime

# Use the entire modules path name to use the functions
print(Demo22Modules.prime.isPrime(5))