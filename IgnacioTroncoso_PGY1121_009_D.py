from funciones import *
os.system("cls")
precio_platinum = 120000
precio_gold = 80000
precio_silver = 50000
total_ganancias = 0
while True:
    menu_creativoscl()
    opcion = validar_opcion(1,5)
    if opcion ==1:
        total_ganancias += comprar_entradas(precio_platinum,precio_gold,precio_silver,total_ganancias)
    elif opcion ==2:
        ver_escenario()
        os.system("cls")
    elif opcion ==3:
        listado_asistentes()
    elif opcion ==4:
        ganancias_totales(precio_platinum,precio_gold,precio_silver,total_ganancias)
    else:
        os.system("cls")
        print("Nos vemos, en otra ocasión!")
        print("-----------------------")
        print("Ignacio Troncoso")
        print("06-07-2023")
        break