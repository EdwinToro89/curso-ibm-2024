class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        tarea_nueva = Tarea(descripcion)
        self.tareas.append(tarea_nueva)

    def marcar_completada(self, posicion):
        try:
            tarea = self.tareas[posicion]
            tarea.completada = True
            print(f"Tarea '{tarea.descripcion}' marcada como completada.")
        except IndexError:
            print("La posición especificada no existe en la lista.")

    def mostrar_todas(self):
        for i, tarea in enumerate(self.tareas):
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{i}: {tarea.descripcion} ({estado})")

    def eliminar_tarea(self, posicion):
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        except IndexError:
            print("La posición especificada no existe en la lista.")

def main():
    lista = ListaTareas()

    while True:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            descripcion = input("Introduce la descripción de la tarea: ")
            lista.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                posicion = int(input("Introduce la posición de la tarea a marcar como completada: "))
                lista.marcar_completada(posicion)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "3":
            lista.mostrar_todas()
        elif opcion == "4":
            try:
                posicion = int(input("Introduce la posición de la tarea a eliminar: "))
                lista.eliminar_tarea(posicion)
            except ValueError:
                print("Por favor, introduce un número válido.")
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main() 
    