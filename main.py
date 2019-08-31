"""
Coding-eric video 16
Archivos pt 3

Leer de un archivo alumnos.csv y crear una lista de diccionarios.
Luego crear un random de faltas entre 1 y 15 para luego guardar la nueva lista
en un nuevo archivo alumnos_nuevo.csv
"""
import random

with open("alumnos.csv") as fi:
	alumnos = []
	ln = fi.readline()
	while ln != "":
		alumnos.append(ln.replace("\n", "").split(","))
		ln = fi.readline()

"""
for alumno in alumnos:
	alumno.append(random.randint(1,15))
	alumnos_nuevo.append(alumno)
"""

[alumno.append(str(random.randint(1,15))) for alumno in alumnos]

alumnos_nuevo = [",".join(alumno) for alumno in alumnos]

alumnos_nuevo = "\n".join(alumnos_nuevo)

with open("alumnos_nuevo.csv", "w") as fo:
	fo.write(alumnos_nuevo)