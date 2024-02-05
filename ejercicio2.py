empleados = []

def agregar_empleado():
    ID_empleado = input("Ingrese el ID del empleado: ")
    nombre_empleado = input("Ingrese el nombre del empleado: ")
    departamento_empleado = input("Ingrese el departamento del empleado: ")
    salario_empleado = input("Ingrese el salario del empleado: ")
    empleados.append([ID_empleado, nombre_empleado,departamento_empleado,salario_empleado])

def ver_empleados():
    for empleado in empleados:
        print(f"ID Empleado : {empleado[0]} ---> nombre: {empleado[1]} ---> departamento: {empleado[2]} ---> salario: {empleado[3]}")

def eliminar_empleado():
    ID_empleado = input("Ingrese el ID del empleado que desee eliminar: ")

    global empleados
    empleados = [empleado for empleado in empleados if empleado[0] != ID_empleado]

    print("Empleado eliminado")

def buscar_empleado():
    print()
    
    
def mostrar_menu():
    print("1. añadir empleado")
    print("2. Mostrar empleados")
    print("3. Eliminar empleado")
    print("4. Buscar empleado por ID")
    print("5. Calcular salario promedio por departamento")
    print("6. Calcular salario promedio general")
    print("7. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 4:
            break
        elif opcion == 1:
            agregar_empleado()
        elif opcion == 2:
            ver_empleados()
        elif opcion == 3:
            eliminar_empleado()
        elif opcion == 4:
            eliminar_empleado()
        elif opcion == 5:
            eliminar_empleado()
        elif opcion == 6:
            eliminar_empleado()
        else:
            print("Ingrese una opcion valida: ")
            print("1. añadir empleado")
            print("2. Ver empleados")
            print("3. Eliminar empleado")
            print("4. Buscar empleado por ID")
            print("5. Calcular salario promedio por departamento")
            print("6. Calcular salario promedio general")
            print("7. Salir")
            opcion = int(input("Seleccione una opcion valida: "))

main()