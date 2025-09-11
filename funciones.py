tareas = []

def cambiar_estado_tarea():
    try:
        num = int(input("Ingrese el número de tarea: "))
    except ValueError:
        print("Entrada inválida. Ingrese un número.")
        return

    if num < 1 or num > len(tareas):
        print("Número de tarea inválido.")
        return

    tarea = tareas[num - 1]
    estado_actual = tarea["Estado"]

    transiciones = {
        "pendiente": "en_progreso",
        "en_progreso": "completado"
    }

    nuevo_estado = transiciones.get(estado_actual)

    if nuevo_estado:
        tarea["Estado"] = nuevo_estado
        print(f"Cambiado el estado de '{estado_actual}' a '{nuevo_estado}'")
    else:
        print("No se puede cambiar un estado ya completado")
