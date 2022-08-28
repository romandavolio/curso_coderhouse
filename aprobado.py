import sys

if len(sys.argv) != 3:
    print("Error, debes ingresar 2 notas.")
else:
    nota1 = int(sys.argv[1])
    nota2 = int(sys.argv[2])
    
    if (nota1 <= 1 and nota1 >= 10) or (nota2 <= 1 and nota2 >= 10):
        print("Notas fuera de rango.")
    elif(nota1 >= 7) and (nota2 >= 7):
        print("Promocionado")
    elif(nota1 >= 4) and (nota2 >= 4):
        print("Aprobado, debe rendir final")
    elif (nota1 < 4 or nota2 <4) and (not (nota1<4 and nota2<4)):
       if nota1<4:
           print("Recupera el primer parcial")
       else:
           print("Recupera el segundo parcial")
    else:
        print("Desaprobo ambos parciales, debe recursar")