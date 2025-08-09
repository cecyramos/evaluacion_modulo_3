tareas = [] # Estoy creando una lista vacía
def menu():
    print("--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("Elige una opción: ")

while True:
    menu()
    opcion = input()
    if opcion == "1":
        def agregar_tarea():
            nombre = input("Ingrese el nombre de la tarea: ")
            estado = False # Por defecto estoy creando una tarea pendiente (False)
            tareas.append({"nombre": nombre, "estado": estado}) # Estoy agregando tareas que consisten en un diccionario con el nombre y el estado
            print("Tarea agregada exitosamente.")
            return tareas
        agregar_tarea()
    elif opcion == "2":
        def mostrar_tareas():
            print("Este es el listado de tareas:")
            for tarea in tareas:
                print(tarea)
            return tareas
        mostrar_tareas()
    elif opcion == "3":
        def marcar_completada():
            nombre = input("Ingrese el nombre de la tarea a marcar como completada: ")
            for tarea in tareas:
                if tarea["nombre"] == nombre:
                    tarea["estado"] = True # Cambiando el estado a True la estoy marcando como completada
                    print("Tarea marcada como completada.")
                    return tareas
            print("Tarea no encontrada.")
            return tareas
        marcar_completada()
    elif opcion == "4":
        def eliminar_tarea():
            nombre = input("Ingrese el nombre de la tarea a eliminar: ")
            for tarea in tareas:
                if tarea["nombre"] == nombre:
                    tareas.remove(tarea)
                    print("Tarea eliminada.")
                    return tareas
            print("Tarea no encontrada.")
            return tareas
        eliminar_tarea()
    elif opcion == "5":
        print("Gracias por usar el Gestor de Tareas.")
        break
    else:
        print("Opción no válida. Ingrese un número del 1 al 5.")