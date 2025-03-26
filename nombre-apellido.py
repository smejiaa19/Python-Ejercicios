# Pedir el primer nombre y apellido del usuario y mostrar la inicial del nombre y el apellido

nombre=input("Ingrese su primer nombre: ")
print(dir(nombre))
nombre=nombre.capitalize() # Metodo para poner la primer letra en mayuscula
apellido=input("Ingrese su apellido: ")
apellido=apellido.capitalize() # Mismo metodo
inicial_nombre=nombre[0] # Aqui decimos que la variable inicial nombre va a ser igual al indice 0 de la variable nombre en este caso pues la primer letra del nombre 

print(f'Bienvenido {inicial_nombre}. {apellido}')