
#Crear un programa que pida ddos numeros y obtenga como resultado 
#cual de ellos es par o si ambos lo son
input("Buenas tardes, Buen Sabado")
input("Averigua que numero es Par y cual no")

numero1=int(input("Favor ingresar un numero: "))
numero2=int(input("Favor ingresar otro numero : "))

if((numero1%2 == 0) and (numero2%2==0)):
    print("Ambos numeros son Pares")
elif((numero1%2 == 0 )and (numero2%2!=0)):
    print(f"{numero1} es Par")
    print(f"{numero2} es Impar")
elif((numero1%2 != 0 )and (numero2%2==0)):
    print(f"{numero1} es Impar")
    print(f"{numero2} es Par")
else:
    print("Los dos Numeros ingresados Son Impares")

input("Hasta luegoooo....")

