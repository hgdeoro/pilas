import pilas
# Permite que este ejemplo funcion incluso si no has instalado pilas.
import sys
sys.path.insert(0, "..")

pilas.iniciar()
mono = pilas.actores.Mono()
mono.escala = 1
mono.rotacion = 0

def girar():
    mono.rotacion = mono.rotacion + 1
    return True

pilas.mundo.agregar_tarea(0, girar)

pilas.avisar("Creando una tarea interminable de girar...")
pilas.ejecutar()
