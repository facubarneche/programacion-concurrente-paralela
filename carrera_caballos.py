# Implementar una "carrera de caballos" usando threads, donde cada "caballo" es un Thread o bien 
# un objeto de una clase que sea sub clase de Thread, y contendrá una posición dada por un número entero. 
# El ciclo de vida de este objeto es incrementar la posición en variados instantes de tiempo, mientras 
# no haya llegado a la meta, la cual es simplemente un entero prefijado. Una vez que un caballo llegue a 
# la meta, se debe informar en pantalla cuál fue el ganador, luego de lo cual los demás caballos no 
# deberán seguir corriendo. Imprimir durante todo el ciclo las posiciones de los caballos, o bien de alguna 
# manera el camino que va recorriendo cada uno (usando símbolos Ascii). El programa podría producir un 
# ganador disitnto cada vez que se corra. Opcionalmente, extender el funcionamiento a un array de n caballos, 
# donde n puede ser un parámetro.

import threading
import time
import random
import os

# Clase principal "Caballo"
class Caballo(threading.Thread):
    def __init__(self, nombre, meta):
        super().__init__()
        self.nombre = nombre
        self.posicion = 0
        self.meta = meta
        self._corriendo = True

    def run(self):
        while self.posicion < self.meta and self._corriendo:
            self.posicion += random.randint(1, 5)
            time.sleep(random.uniform(0.1, 0.5))  # Varía el tiempo de espera entre movimientos
        if self.posicion >= self.meta:
            self._corriendo = False
            global ganador
            if not ganador:
                ganador = self.nombre
            detener_carrera()

    def mostrar_progreso(self):
        recorrido = '.' * self.posicion
        recorrido += '/\~/\>' if self.posicion % 2 == 0 else '/\~()>'
        return f"{self.nombre}: {recorrido}"

    def detener(self):
        self._corriendo = False

# Sub Clase para gestionar la carrera
class Carrera:
    def __init__(self, num_caballos, meta):
        self.caballos = [Caballo(f"Caballo {i+1}", meta) for i in range(num_caballos)]
        self.meta = meta

    def iniciar(self):
        for caballo in self.caballos:
            caballo.start()

        while any(caballo.is_alive() for caballo in self.caballos):
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola Windows u otros
            for caballo in self.caballos:
                print(caballo.mostrar_progreso())
            time.sleep(0.1)  # Controla la frecuencia de actualización

        print(f"\n¡{ganador} ha ganado la carrera!")

def detener_carrera():
    for caballo in carrera.caballos:
        caballo.detener()

# Variables globales
ganador = None

# Inicia la carrera con cantidad de caballos y distancia meta como parametros
carrera = Carrera(20, 100)
carrera.iniciar()
