#Kiara Torales 2903
# Variables
nombre = "Juan"
edad = 25
altura = 1.75

# Comentarios
# Esto es un comentario en Python
print("Hola, esto es un ejemplo de comentario")

# Asignaciones
x = 10
y = 20
z = x + y
print("La suma es:", z)

# Comparaciones
print(5 > 3)  # True
print(10 == 10)  # True
print(4 != 5)  # True

# Operadores Aritméticos
suma = 5 + 3
resta = 10 - 4
multiplicacion = 6 * 7
division = 20 / 4
print("Suma:", suma, "Resta:", resta, "Multiplicación:", multiplicacion, "División:", division)

# Operadores Lógicos
es_mayor = (10 > 5) and (8 > 6)
es_menor = (4 < 3) or (7 > 5)
negar = not (5 == 5)
print("AND:", es_mayor, "OR:", es_menor, "NOT:", negar)

# Entrada de Datos
nombre_usuario = input("Ingrese su nombre: ")
print("Hola, " + nombre_usuario + "!")

# Condicionales
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")