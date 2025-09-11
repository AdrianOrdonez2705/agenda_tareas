# Este es el archivo de funciones
tareas = []
def agregar_tarea ():
    nom_tarea = input("Nombre tarea")
    est_tarea = "pendiente"
    tarea = {"Nombre": nom_tarea, "Estado": est_tarea}
    tareas.append(tarea)
    print ("Tarea agregada")

