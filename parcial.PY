
  
#    __
#                      .'  '.
#                  _.-'/  |  \
#     ,        _.-"  ,|  /  0 `-.
#     |\    .-"       `--""-.__.'=====================-,
#     \ '-'`        .___.--._)=========================|
#      \            .'      |                          |
#       |     /,_.-'        |              By:         |
#     _/   _.'(             |          JOSE DONDIS     |
#    /  ,-' \  \            |                          |
#    \  \    `-'            |                          |
#     `-'                   '--------------------------'


from os import remove
from os import append

inventario = []

def menu():
    print()
    print("********************")
    print("*****INVENTARIO*****")
    print("********************")
    print()

while True:
    print()
    print("1. VER NOMBRE DEL CREADOR")
    print("2. Agregar item")
    print("3. Eliminar un item")
    print("4. Mostrar los items")
    print("5. Salir del programa")
    print()

    opcion = input("ELIGE UNA OPCION: ")

    if opcion == '1':
        print()
        print("EL CREADOR DEL PROGRAMA ES:")
        print()
        print("JOSE DONDIS")
        print("4-812-1989")
        print()
        continue

    elif opcion == '2':
        print()
        item = input("Ingresa el item que deseas agregar: ").capitalize()
        if item in inventario:
            print()
            print("Este item ya se encuentra en el inventario:  ")
            print()
            print()

        else:
            inventario.append(item)

    elif opcion == "3":
        print()
        item = input("Ingresa el item que deseas eliminar del inventario: ").capitalize()
        if item not in inventario:
            print()
            print("Este item no se encuentra en el inventario. ")
            print()
        else:
             inventario.remove(item)
    elif opcion == '4':
        print()
        print ("Los items en el inventario son: ")
        print()

        for e in inventario:
            print()
            print(" -",e)
    elif opcion == '5':
        break
    else: 
        print()
        print("Elige una opcion correcta.")

