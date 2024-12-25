# Opens 'myfile.txt', reads the first line, and tries to convert it to an integer, while handling any I/O, value conversion, or unexpected errors.
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as io:
    print("I/O error: {0}".format(io))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
