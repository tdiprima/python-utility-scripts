# Displays the Python module search path and prints the contents of the pizzapy menu.
import sys
from pprint import pprint

pprint(sys.path)

import pizzapy.menu

print(pizzapy.menu.MENU)
