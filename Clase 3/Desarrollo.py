'''Introduccion de listas'''
array = ["futbol", "Pc", 18.6,18,[6, 7,10.4], True, False]

print("Ejemplo de Array ")
print(array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])
#Cantidad de datos que cuenta el array
print(len(array))
#Agregar un valor dentro de la lista
array.append(66)
print(array)
#Insertar datos en una posicion especifica
array.insert(1,88)
print(array)
#Insertar mas de un dato al final 
array.extend([1,88, True,100])
print(array)
# Buscar valores dentro de un array
print("Pc" in array)
# Saber el índice donde está lo que busco
print(array.index("Pc"))
# Cantidad de veces que tengo el valor en mi array
print(array.count("Pc"))
# Borrar valores de un array
array.remove("Pc")
print(array)
# Limpiar (comentado)
array.clear()
print(array)
# Cambiar la posición (reversa)
array.reverse()
print(array)
# Ordenar de mayor a menor
array4 = [1, 2, 8, -11, 5]
array4.sort()
print(array4)
array4.sort(reverse=True)
print(array4)



'''WHILE -MIENTRAS QUE'''
#si o si inicializar 
i= 0
while i < 10:
    print("Unida", "INDEX: ", i)
    i+=1



'''BUCLE FOR '''
array1 = ["futbol", "Pc", 18.6,18,[6, 7,10.4], True, False]


for i in array1:
    print(f"Datos :{i}")


'''FUNCIONESSSS
palabra reservada def
'''
def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def multiplica(a,b):
    return a * b

def division(a,b):
    return a / b

def resto(a,b):
    return a % b


#Ejemplo de uso 1
n1=2
n2=6
resultado1=0

resultado1=sumar(n1,n2)
print(f"La suma es :{resultado1}")

resultado1=restar(n1,n2)
print(f"La resta es :{resultado1}")

resultado1=multiplica(n1,n2)
print(f"La multiplicacion es :{resultado1}")

resultado1=division(n1,n2)
print(f"La division es :{resultado1}")

resultado1=resto(n1,n2)
print(f"El resto es :{resultado1}")

#Ejemplo de uso 2
resultado=sumar(3,5)
print(f"La suma es :{resultado}")

