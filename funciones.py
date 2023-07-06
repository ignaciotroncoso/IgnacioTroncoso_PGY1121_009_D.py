import os
import time
import msvcrt as tecla
from numpy import *
lista_asistentes = []
lista_filas = []
lista_columnas = []
lista_contador_platinum = [0]
lista_contador_gold = [0]
lista_contador_silver = [0]
escenario = zeros((10,10), int)
contador_platinums = 0
contador_golds = 0
contador_silvers = 0
def listado_asistentes():
    print("\nLISTADO DE ASISTENTES: ")
    print("RUN: ",sort(lista_asistentes))
    print("\n Presione una tecla para continuar...")
    tecla.getch()
    os.system("cls")
def ganancias_totales(precio_platinum:int,precio_gold:int,precio_silver:int,total_ganancias:int):
    total_platinum = lista_contador_platinum[0]*precio_platinum
    total_gold = lista_contador_gold[0]*precio_gold
    total_silver = lista_contador_silver[0]*precio_silver
    cantidad_total = lista_contador_platinum[0] + lista_contador_gold[0] + lista_contador_silver[0]
    print("GANANCIAS TOTALES:")
    print("-----------------------------------------")
    print("TIPO DE ENTRADA | CANTIDAD | TOTAL")
    print("-----------------------------------------")
    print(f"\nPLATINUM | {lista_contador_platinum[0]} | ${total_platinum}")
    print("-----------------------------------------")
    print(f"\nGOLD | {lista_contador_gold[0]} | ${total_gold}")
    print("-----------------------------------------")
    print(f"\nSILVER | {lista_contador_silver[0]} | ${total_silver}")
    print("-----------------------------------------")
    print(f"TOTAL | {cantidad_total} | ${total_ganancias}")
    print("\nPresione cualquier tecla para continuar...")
    tecla.getch()
    os.system("cls")
def validar_entradas():
    while True:
        try:
            entrada = int(input("Ingrese cantidad de entradas a comprar (1-3): "))
            if entrada in(1,2,3):
                return entrada
            else:
                print("ERROR! La cantidad de entradas debe ser entre 1 a 3")
        except:
            print("ERROR! Debe ingresar números enteros!")
def validar_columna():
    while True:
        try:
            columna = int(input("Ingrese número de columna (1-10): "))
            if columna >= 1 and columna <=10:
                return columna
            else:
                print("ERROR! Columna no existe!")
        except:
            print("ERROR! Debe ingresar solo números enteros!")
def validar_fila():
    while True:
        try:
            fila = int(input("Ingrese número de fila (1-10): "))
            if fila in(1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("ERROR! Fila no existe!")
        except:
            print("ERROR! Debe ingresar solo números enteros!")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese su rut sin puntos ni digito verificador: "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut
            else:
                print("ERROR! RUT NO VALIDO!")
        except:
            print("ERROR! Debe ingresar solo números enteros!")
def comprar_entradas(precio_platinum:int,precio_gold:int,precio_silver:int,total:int):
    total_ganancias = 0
    entrada = validar_entradas()
    for x in range(entrada):
        rut = validar_rut()
        while True:
            ver_escenario()
            fila = validar_fila()
            columna = validar_columna()
            if fila in(1,2):
                total = precio_platinum
                total_ganancias += total
                lista_contador_platinum[0] += 1
            elif fila in(3,4,5):
                total = precio_gold
                total_ganancias += total
                lista_contador_gold[0] += 1
            else:
                total = precio_silver
                total_ganancias += total
                lista_contador_silver[0] += 1
            print(f"Su total a pagar es de: {total}")
            if escenario[fila-1][columna-1] == 0:
                lista_asistentes.append(rut)
                escenario[fila-1][columna-1] = 1
                lista_filas.append(fila)
                lista_columnas.append(columna)
                print("\nLa operación se ha realizado correctamente!")
                print("Gracias por su compra!")
                time.sleep(2)
                os.system("cls")
                break
            else:
                print("Ubicación ocupada por favor elija otra!")
    return total_ganancias
def validar_opcion(min:int,max:int):
    while True:
        try:
            opcion = int(input(f"Ingrese opción ({min}-{max}): "))
            if opcion >= min and opcion <= max:
                return opcion
            else:
                print("ERROR! La opción ingresada no es valida!")
        except:
            print("ERROR! Debe ingresar un número entero!")
def menu_creativoscl():
    print("""MENU CONCIERTO:
    1. Comprar Entradas
    2. Mostrar ubicaciones
    3. Ver listado de asistencia
    4. Mostrar ganancias totales
    5. Salir""")
def ver_escenario():
    print("\nESCENARIO:")
    print("\t         COLUMNAS:")
    print("          1 2 3 4 5 6 7 8 9 10")
    print("---------------------------------------------")
    for x in range(10):
        print("FILA", str(x+1).ljust(2), end=": ")
        for y in range(10):
            print("",escenario[x][y], end="")
        print()
    print("---------------------------------------------")
    print("\n Presione una tecla para continuar...")
    tecla.getch()