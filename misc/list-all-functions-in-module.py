# Prints out the name of each function and variable in the 'shutil' module, one per line.
import shutil as module

# This will do the trick:
# dir(module)

# However, if you find it annoying to read the returned list, just use the
# following loop to get one name per line.
for i in dir(module):
    print(i)
