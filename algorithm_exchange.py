import threading as t
import time


common = 1
def run_thread():
    global common
    local1 = 0
    for _ in range(20):
        # Emulamos procesos
        time.sleep(0.1)

        # Hacemos el intercambio de variables para activar el semaforo para el otro thread
        common, local1 = local1, common
        if(local1 == 1):
            print('Seccion Critica 1')

            # Normalizamos semaforo con cambio de variable
            common, local1 = local1, common

def run_thread2():
    global common
    local2 = 0
    for _ in range (20):
        # Emulamos procesos
        time.sleep(0.1)

        # Hacemos el intercambio de variables para activar el semaforo para el otro thread
        common, local2 = local2, common
        if(local2 == 1):
            print('Seccion Critica 2')

            # Normalizamos semaforo con cambio de variable
            common, local2 = local2, common

thread1 = t.Thread(target=run_thread)
thread2 = t.Thread(target=run_thread2)
thread1.start()
thread2.start()