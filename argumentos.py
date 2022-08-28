import sys

if len(sys.argv) != 3:
    print("Error necesito 2 argumentos.")
else:
    palabra = sys.argv[1]

    cantidad = int(sys.argv[2])

    for i in range(cantidad):
        print(palabra)