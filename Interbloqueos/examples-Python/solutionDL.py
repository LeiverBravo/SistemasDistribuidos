import multiprocessing
import pickle

def worker1(conn1, conn2):
    print('worker1 iniciado')
    conn1.send('worker1: Esperando por un mensaje de worker2')
    conn1.recv()  # Espera a que worker2 esté listo
    conn2.send(pickle.dumps('worker1: Mensaje recibido de worker2'))
    conn1.close()
    conn2.close()
    print('worker1 terminado')

def worker2(conn1, conn2):
    print('worker2 iniciado')
    conn2.send('worker2: Esperando por un mensaje de worker1')
    conn2.recv()  # Espera a que worker1 esté listo
    conn1.send(pickle.dumps('worker2: Mensaje recibido de worker1'))
    conn1.close()
    conn2.close()
    print('worker2 terminado')

if __name__ == '__main__':
    # Crear las dos pipes
    conn1, conn2 = multiprocessing.Pipe()
    conn3, conn4 = multiprocessing.Pipe()

    # Crear los procesos y pasarles las pipes
    p1 = multiprocessing.Process(target=worker1, args=(conn1, conn4))
    p2 = multiprocessing.Process(target=worker2, args=(conn3, conn2))

    # Iniciar los procesos
    p1.start()
    p2.start()

    # Esperar a que los procesos terminen
    p1.join()
    p2.join()

    print('Terminado!')
