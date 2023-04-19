import threading

# Se crean dos recursos compartidos
resource_a = threading.Lock()
resource_b = threading.Lock()

# Función que representa al primer proceso
def process_one():
    print("Proceso 1 adquiriendo recurso A")
    resource_a.acquire()
    print("Proceso 1 adquiriendo recurso B")
    resource_b.acquire()
    print("Proceso 1 liberando recurso B")
    resource_b.release()
    print("Proceso 1 liberando recurso A")
    resource_a.release()

# Función que representa al segundo proceso
def process_two():
    print("Proceso 2 adquiriendo recurso A")
    resource_a.acquire()
    print("Proceso 2 adquiriendo recurso B")
    resource_b.acquire()
    print("Proceso 2 liberando recurso B")
    resource_b.release()
    print("Proceso 2 liberando recurso A")
    resource_a.release()

# Se crean los hilos para ejecutar los procesos
thread_one = threading.Thread(target=process_one)
thread_two = threading.Thread(target=process_two)

# Se inician los hilos
thread_one.start()
thread_two.start()

# Se espera a que los hilos terminen
thread_one.join()
thread_two.join()