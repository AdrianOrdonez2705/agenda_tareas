tareas = [] 

def agregar_tarea(): 
    nombre = input("Ingrese el nombre de la tarea: ") 
    tarea = { "Nombre:" : nombre, "Estado": "Pendiente" } 
    tareas.append(tarea) 
    print("Tarea agregada correctamente") 

def eliminar_tarea(numero): 
    if numero < 1 or numero > len(tareas): 
        print ("esta tarea no existe, revisa de nuevo su numero") 
        return 
    
    copiaTareas = tareas[numero - 1] 

    if copiaTareas ["estado"] == "Completada": 
        tareas.pop(numero - 1) 
        print ("Tarea eliminada con éxito") 
    else: 
        print ("Error al eliminar la tarea, solo se pueden borrar tareas en estado Completado") 

def completar_tarea(): 
    print("Tareas\nNro\tNombre\tEstado\n-------------") 

    for i, tarea in enumerate(tareas): 
        print(i+1, "\t", tarea["Nombre"], "\t", tarea["Estado"], "\n") 
        print("-----------------------------------") 
        try: 
            num = int(input("Ingrese el número de tarea: ")) 
        except ValueError: 
            print("Entrada inválida. Ingrese un número.") 
            return 
        
    if num < 1 or num > len(tareas): 
        print("Número de tareas inválido") 
        return 
    
    tarea = tareas[num - 1] 
    estado_actual = tarea["Estado"] 
    transiciones = { 
        "Pendiente" : "En progreso", 
        "En progreso" : "Completada" 
    } 

    nuevo_estado = transiciones.get(estado_actual) 
    
    if nuevo_estado: 
        tarea["Estado"] = nuevo_estado 
        print(f"Cambiado el estado de {estado_actual} a {nuevo_estado}") 
    else: 
        print("No se puede cambiar un estado ya completado") 
        
def ver_tareas(): 
    print("1. Ver todas las tareas") 
    print("2. Ver tareas pendientes") 
    print("3. Ver tareas en progreso") 
    print("4. Ver tareas completadas") 
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
        print("No hay tareas para mostrar.") 
        return 
    
    for tarea in tareas_filtradas: 
        print("Nombre:", tarea["Nombre"], "\tEstado:", tarea["Estado"])
