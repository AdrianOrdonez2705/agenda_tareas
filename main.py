import funciones as f


def menu():
    while True:
        print("------Agenda Tareas------- \n1. Agregar Tarea\n2. Ver Tareas\n3.Marcar tarea como completada\n4.Eliminar tarea\n5. Salir")
        opcion=int(input("Ingrese su opcion: "))
        print("-------------------------------")
        if opcion not in [1,2,3,4,5]:
            print("Opcion invalida")
            continue
        if opcion==1:
            f.agregar_tarea()
        elif opcion ==2:
            f.ver_tareas()
        elif opcion==3:
            f.completar_tarea()
        elif opcion==4:
            print("Tareas\nNro\tNombre\tEstado\n----------------------------")
            for i, tarea in enumerate(f.tareas):
                print(i+1,"\t",tarea["Nombre"],"\t",tarea["Estado"],"\n")
            print("-------------------------------")
            eliminar=int(input("Ingrese el numero de la tarea a eliminar: "))
            f.eliminar_tarea(eliminar)
        elif opcion ==5:
            print("Saliendo...\n¡Gracias por usar la agenda!")
            break
if __name__ == "__main__":
    menu()
