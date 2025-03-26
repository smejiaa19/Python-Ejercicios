# Programa que calcula el promedio de un estudiante de una clase en el semestre

estudiantes = []
nEst = int(input("Ingrese el número de estudiantes: "))

for i in range(nEst):
    print(f"\n\n--- Estudiante {i + 1} ---")
    cortes = []  # Inicializar la lista de cortes para cada estudiante

    for j in range(3):  # Tres cortes
        notas = []
        print(f"\n--- Corte {j + 1} ---")

        while True:
            try:
                n = int(input("Ingrese el número de evaluaciones: "))
                if n > 0:
                    break
                else:
                    print("Debe ingresar un número entero positivo")
            except ValueError:
                print("Debe ingresar un número entero")

        print("\n--- Evaluaciones ---")
        for k in range(n):
            while True:
                try:
                    nota = int(input(f"Ingrese la nota de la evaluación {k + 1}: "))
                    if 0 <= nota <= 100:
                        break
                    else:
                        print("La nota debe estar entre 0 y 100")
                except ValueError:
                    print("Debe ingresar un número entero")

            notas.append(nota)

        cortes.append(notas)  # Guardar las notas de este corte

    estudiantes.append(cortes)  # Guardar los cortes del estudiante

# Cálculo de promedios
promedios = []
for estudiante in estudiantes:
    promedio_estudiante = []
    for corte in estudiante:
        promedio_corte = sum(corte) // len(corte)
        promedio_estudiante.append(promedio_corte)
    promedios.append(sum(promedio_estudiante) // len(promedio_estudiante))

# Mostrar resultados
print("\n\n----Promedios de Estudiantes----")
for i in range(len(promedios)):
    print(f"Estudiante {i + 1}: {promedios[i]}")