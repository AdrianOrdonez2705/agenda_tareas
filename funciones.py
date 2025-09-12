# Este es el archivo de funciones

# Funcion de eliminar la tarea
def eliminar_tarea(numero):
    if numero < 1 or < len(tareas):
        print ("esta tarea no existe, revisa de nuevo su numero")
        return
    copiaTareas = tareas[numero - 1]
    if copiaTareas ["estado"] == "Completada":
        tareas.pop(numero - 1)
        print ("Tarea eliminada con éxito")
    else:
        print ("Error al eliminar la tarea, solo se pueden borrar tareas en estado Completado")
    

tareas = []
def agregar_tarea ():
    nom_tarea = input("Nombre tarea")
    est_tarea = "pendiente"
    tarea = {"Nombre": nom_tarea, "Estado": est_tarea}
    tareas.append(tarea)
    print ("Tarea agregada")


