import sys

from funciones_matematicas import *

variable1 = int(sys.argv[1])

variable2 = int(sys.argv[2])

print(sumar(variable1,variable2))

if variable1 > variable2:
    print("Variable 1 es mayor que variable 2")
else:
    print("Variable 2 es mayor que variable 1")