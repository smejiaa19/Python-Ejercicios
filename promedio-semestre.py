# Crear un programa donde se ingresen 3 semestres de clase, darle la opcion al usuario de ingresar el numero de evaluaciones por cada semestre y que ingrese la nota de estas
# Despues calcular el promedio de cada semestre. Para finalmente calcular el promedio general 

nombre= input('Ingrese el nombre del usuario: ') # Aqui se le pide al usuario que ingrese el nombre del estudiante 
semestre1 = []
semestre2 = []
semestre3 = [] #Creamos listas vacias para almacenar las notas de cada semestre
semestres = 3 # Numero de semestres
#print(dir(semestre1))

for i in range(1, 2): # Ciclo for para el primer semestre 
    evaluaciones = int(input(f'Ingrese el numero de evaluaciones del semestre {i}: ')) # Se le pide al usuario que ingrese el numero de evaluaciones
    for j in range(evaluaciones): # Ciclo for para ingresar las notas de cada evaluacion
        nota = int(input(f'Ingrese la nota de la evaluacion {j+1} del semestre {i}: ')) # Se le pide al usuario que ingrese la nota de cada evaluacion 
        semestre1.append(nota) # Se agregan las notas a la lista semestre1
prom1 = sum(semestre1)/len(semestre1) # Se calcula el promedio de las notas del semestre 1 utilizando los metodos sum y len de python, esto lo hacemos mediante los metodos sum y len de python
        
        
for i in range(2, 3): # Ciclo for para el segundo semestre
    evaluaciones = int(input(f'Ingrese el numero de evaluaciones del semestre {i}: ')) # A partir de aqui se repite el mismo proceso que en el semestre 1
    for j in range(evaluaciones):
        nota = int(input(f'Ingrese la nota de la evaluacion {j+1} del semestre {i}: '))
        semestre2.append(nota)
prom2 = sum(semestre2)/len(semestre2)

for i in range(3, 4): # Se repite el mismo proceso que el ciclo for 1 y 2. 
    evaluaciones = int(input(f'Ingrese el numero de evaluaciones del semestre {i}: '))
    for j in range(evaluaciones):
        nota = int(input(f'Ingrese la nota de la evaluacion {j+1} del semestre {i}: '))
        semestre3.append(nota)
prom3 = sum(semestre3)/len(semestre3)

promedio_final = (prom1 + prom2 + prom3)/semestres
print(f'El promedio general de estudiante {nombre.capitalize()} es de: {promedio_final} puntos') 
    