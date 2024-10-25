####################################################################################################################################
################################################## TRABAJO PRÁCTICO: SEMÁFOROS #####################################################
######################################################### FACUNDO BARNECHE #########################################################
####################################################################################################################################

#1. Describir en pseudocódigo una solución al problema de productor-consumidor, para el caso de 2 productores y 1 consumidor, 
# todos sobre un mismo buffer. Escribir todas las aclaraciones que sean necesarias.

# El problema indicado funciona de la siguiente manera, los procesos arrancan en paralelo con la ayuda de los threads.
# Se asigna el semaforo nombrado W con un valor de -1.
# Tanto el proceso P como Q, llamadas productores, van a poder ejecutarse sin problemas, pero solo si estos dos envian la señal 
# (sumando en este ejemplo, 1 al contador de W) el proceso M, tambien llamado consumidor, va a poder seguir el flujo de su ejecución.

# W = -1

#   PROCESO P:                 PROCESO Q:              PROCESO M: 
#   do anything                do anything             do anything 
#   signal (W)                 signal(W)               wait(W)
#   keep doing anything        keep doing anything     wait(W)
#   keep doing anything        keep doing anything     keep doing anything

# -------------------------------------------------------------------------------------------------------------------------------------

#2. En pseudocódigo, usando semáforos, resolver el problema del "rendez-vous" (o encuentro). 
# Consiste en tener dos procesos, tales que uno de ellos mientras ejecuta deberá alcanzar un punto (o marca) dentro de su código, y lo mismo 
# con otro proceso. El primero de ambos que llegue a la marca correspondiente deberá quedarse esperando a que el otro proceso llegue a su marca, 
# y recién en el momento en que el otro haya llegado, ambos podrán continuar ejecutando su código a partir de allí. 
# Escribir o discutir luego una solución análoga del rendez-vous para para 3 o más procesos, cada uno con su código y su marca dada. 
# (Opcionalmente, implementarlo en Python u otro lenguaje, imprimiendo mensajes que informen cuando los procesos lleguen a las marcas dadas. 
# En este caso, dentro del código podrían utilizar algún paquete o clase existente que implemente semáforos...)

# Este caso de rendez-vous con 2 procesos se puede hacer con 2 semaforos, ambos productores - consumidores.
# Ambos procesos dependen de si, ya que uno proceso le da la señal de permiso de ejecución al otro. Por el otro lado, el otro proceso
# para tomar ese permiso y seguir su flujo debe habilitar el semaforo del otro proceso.
# Cuando hablamos del punto de encuentro o marca, hablamos cuando comienzan las acciones de signals y waits para los semaforos.

# P = -1
# Q = -1

#   PROCESO P:					PROCESO Q:
#   do anything			    	do anything
#   do anything				    signal(Q)
#   do anything				    wait(P)
#   do anything				    keep doing anything
#   signal(P) 					keep doing anything
#   wait(Q)     				keep doing anything	
#   keep doing anything			keep doing anything
#   keep doing anything			keep doing anything

# El caso rendez-vous con 3 procesos se necesitan 3 semaforos, por eso podemos decir que la cantidad de procesos necesarias a priori siempre
# va a ser de (N, esto quiere decir 2 procesos 2 semaforos, 3 procesos 3 semaforos, asi sucesivamente).
# Como en el caso anterior cada proceso va a poder ejecutar sin problemas hasta la marca (signals y waits) pero cada proceso va a necesitar
# que el resto de procesos lleguen a dar la señal para que este pueda seguir, que vale aclarar que el que sigue ya dió su señal anteriormente
# habilitando al resto de procesos.

# P = -1
# Q = -1
# M = -1

#   PROCESO P:			    PROCESO Q:				PROCESO M:
#   do anything		        do anything			    do anything
#   do anything		        signal(Q)				do anything
#   do anything		        signal(Q)				do anything
#   do anything             wait(M)                 do anything
#   do anything		        wait(P)			        signal(M) 
#   do anything		        do anything		        signal(M) 		
#   do anything             do anything             wait(Q)
#   do anything 		    do anything			    wait(P)
#   do anything		        keep doing anything		keep doing anything
#   signal(P)			    keep doing anything		keep doing anything
#   signal(P)			    keep doing anything		keep doing anything
#   wait(M)                 keep doing anything     keep doing anything
#   wait(Q)     		    keep doing anything		keep doing anything
#   keep doing anything	    keep doing anything		keep doing anything
#   keep doing anything	    keep doing anything		keep doing anything

# ------------------------------------------------------------------------------------------------------------------------------

import threading as t
import time
import random

# Semáforos para el rendez-vous
P_ready = t.Semaphore(0)
Q_ready = t.Semaphore(0)
M_ready = t.Semaphore(0)

# Semáforo adicional para coordinación después de la marca
rendezvous = t.Semaphore(0)

def process(word, process_ready):
    print(f"{word}: Ejecutando proceso")
    time.sleep(random.randint(1, 10)) # Duermo el proceso por un tiempo random para que se aprecie el flujo al ojo humano
    print(f"{word}: Llegué a la marca")
    process_ready.release()  # Indica que P llegó a la marca

    # Espera a que todos los procesos lleguen a la marca
    rendezvous.acquire()
    
    print(f"{word}: Sigo con el proceso después de la marca")

# Creamos hilos y los asignamos con los argumentos como segundo parametros ya que no queremos ejecutar la funcion en estas lineas
thread_P = t.Thread(target=process, args=('P', P_ready))
thread_Q = t.Thread(target=process, args=('Q', Q_ready))
thread_M = t.Thread(target=process, args=('M', M_ready))

# Iniciamos hilos
thread_P.start()
thread_Q.start()
thread_M.start()

# Esperamos a que todos los procesos lleguen a la marca
P_ready.acquire()
Q_ready.acquire()
M_ready.acquire()

# Liberamos el semáforo para que todos los procesos continúen
rendezvous.release()  # Activa a uno de los procesos para continuar
rendezvous.release()  # Activa al segundo proceso para continuar
rendezvous.release()  # Activa al tercer proceso para continuar

