listaTareas = []

def agregar_tarea():
    descripcion_tarea = input("Ingrese la descripcion tarea: ")
    estado_tarea = input("Ingrese el estado de la tarea: ")
    listaTareas.append([descripcion_tarea, estado_tarea])

def ver_tarea():
    for tarea in listaTareas:
        print(f"descripcion : {tarea[0]} ---> Estado: {tarea[1]}")

def eliminar_tarea():
    descripcion_tarea = input("Ingrese el nombre del empleado que desee eliminar: ")

    global listaTareas
    listaTareas = [tarea for tarea in listaTareas if tarea[0] != descripcion_tarea]

    print("Tarea eliminada")
    
def marcar_tarea():
    print()

def mostrar_menu():
    print("1. Agregar Tarea")
    print("2. Ver Tarea")
    print("3. Eliminar Tarea")
    print("4. Marcar Tarea")
    print("5 Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 5:
            break
        elif opcion == 1:
            agregar_tarea()
        elif opcion == 2:
            ver_tarea()
        elif opcion == 3:
            eliminar_tarea()
        elif opcion == 4:
            marcar_tarea()
        else:
            print("Ingrese una opcion valida: ")
            print("1. Agregar Tarea")
            print("2. Ver Tarea")
            print("3. Eliminar Tarea")
            print("4. Marcar Tarea")
            print("5 Salir")
            opcion = int(input("Seleccione una opcion valida: "))

main()