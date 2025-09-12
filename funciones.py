tareas = [] 

def agregar_tarea(): 
    nombre = input("Ingrese el nombre de la tarea: ") 
    tarea = { 
        "Nombre" : nombre, 
        "Estado": "Pendiente" 
    } 
    tareas.append(tarea) 
    print("Tarea agregada correctamente\n") 

def eliminar_tarea(numero): 
    if numero < 1 or numero > len(tareas): 
        print ("esta tarea no existe, revisa de nuevo su numero\n") 
        return 
    
    tareas.pop(numero - 1)
    print("Tarea eliminada con éxito\n")

def completar_tarea(): 
    print("Tareas")
    print("Nombre\tEstado\n")

    transiciones = { 
        "Pendiente" : "En progreso", 
        "En progreso" : "Completada" 
    }


    for i, tarea in enumerate(tareas):
        print(i+1, tarea["Nombre"], "\t", tarea["Estado"])

    try:
        num = int(input("\nIngrese el nro de tarea: "))
    except ValueError:
        print("Debe ser un número\n")
    
    tarea = tareas[num - 1] 
    estado_actual = tarea["Estado"]  

    nuevo_estado = transiciones.get(estado_actual) 

    if nuevo_estado: 
        tarea["Estado"] = nuevo_estado 
        print(f"Cambiado el estado de {estado_actual} a {nuevo_estado}\n") 

    else: 
        print("No se puede cambiar un estado ya completado\n") 
        
def ver_tareas(): 
    print("\n")
    print("1. Ver todas las tareas") 
    print("2. Ver tareas pendientes") 
    print("3. Ver tareas en progreso") 
    print("4. Ver tareas completadas\n") 

    try: 
        opcion = int(input("Ingrese una opción: ")) 

    except ValueError: 
        print("Entrada inválida. Debe ingresar un número.") 
        return 
    
    if opcion not in [1, 2, 3, 4]: 
        print("Opción no válida.") 
        return 
    
    if opcion == 1: 
        tareas_filtradas = tareas 

    elif opcion == 2: 
        tareas_filtradas = [t for t in tareas if t["Estado"] == "Pendiente"] 

    elif opcion == 3: 
        tareas_filtradas = [t for t in tareas if t["Estado"] == "En progreso"] 

    elif opcion == 4: 
        tareas_filtradas = [t for t in tareas if t["Estado"] == "Completada"] 
    
    if not tareas_filtradas: 
        print("No hay tareas para mostrar.\n") 
        return 
    
    for tarea in tareas_filtradas: 
        print("Nombre:", tarea["Nombre"], "\tEstado:", tarea["Estado"])
