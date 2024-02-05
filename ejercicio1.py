listaProductos = []

def agregar_producto():
    ID_producto = input("Ingrese el ID del producto: ")
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad_producto = int(input("Ingrese la cantidad del producto: "))
    precio_producto = float(input("Ingrese el precio del producto: "))
    listaProductos.append([ID_producto, nombre_producto,cantidad_producto,precio_producto])

def ver_producto():
    for producto in listaProductos:
        print(f"ID Producto : {producto[0]} ---> nombre: {producto[1]} ---> Cantidad: {producto[2]} ---> precio: {producto[3]}")

def eliminar_producto():
    ID_producto = input("Ingrese el ID del producto que desee eliminar: ")

    global listaProductos
    listaProductos = [producto for producto in listaProductos if producto[0] != ID_producto]

    print("Empleado eliminado")

def buscar_producto():
    print()

def calcular_producto():
    print()
    
def mostrar_menu():
    print("1. añadir producto")
    print("2. Mostrar producto")
    print("3. Eliminar producto")
    print("4. Buscar producto por ID")
    print("5. Calcular  valor total del inventario")
    print("6. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))

        if opcion == 6:
            break
        elif opcion == 1:
            agregar_producto()
        elif opcion == 2:
            ver_producto()
        elif opcion == 3:
            eliminar_producto()
        elif opcion == 4:
            buscar_producto()
        elif opcion == 5:
            calcular_producto()
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