#!/usr/bin/python3

import sys
print(sys.argv)
print(sys.argv[1:])



if sys.argv[1] == "sumar":
    result = float(sys.argv[2]) + float(sys.argv[3])
elif sys.argv[1] == "restar":
    result = float(sys.argv[2]) - float(sys.argv[3])
elif sys.argv[1] == "dividir":
    result = float(sys.argv[2]) / float(sys.argv[3])
elif sys.argv[1] == "multiplicar":
    result = float(sys.argv[2]) * float(sys.argv[3])


try:
    print("El resultado es " + str(result))
except NameError:
    print("Operacion no aceptada")
