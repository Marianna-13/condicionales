#SENTENCIA ELIF
# letras=input("Ingrese las vocales: ")
# palabras=""
# if letras.lower():
#      palabras +=letras.lower()
# elif letras.lower():
#      palabras+=letras
# else:
#      palabras+=letras

#Ejercicios con condicionales y operaciones matematicas
#1. verifica si un numero es positivo negativo o cero
# numero=int(input("Ingresa un numero: "))
# if numero >1:
#     print("El numero es positivo")
# elif numero <-1:
#     print("El numero es negativo")
# else:
#     print("El numero es cero")

#2. calcula el mayor de dos numeros ingresados
# num1=int(input("Ingresa el primer  numero: "))
# num2=int(input("Ingresa el segundo  numero: "))
# if num1 > num2:
#     print("El primer numero es mayor")
# elif num1 < num2:
#     print("El segundo numero es mayor")
# else:
#     print("Los numeros son iguales")

#3. Determina si un numero es par o impar
# numero=int(input("Ingresa un numero: "))
# if numero % 2==0:
#     print("El numero es par")
# else:
#     print("El numero es impar")

#4.Dado un numero, verifica si esta entre 10 y 20.
# numero=int(input("Ingresa un numero: "))
# if numero >=10 and numero <=20:
#     print("El numero SI esta entre 10 y 20")
# else:
#     print("El numero NO esta entre los dos numeros dados")


#5. Dados tres numeros, encuentra el mayor usando condicionales.
# num1=int(input("Ingresa un numero: "))
# num2=int(input("Ingresa un numero: "))
# num3=int(input("Ingresa un numero: "))
# if num1>= num2 and num1>=num3:
#     print("El numero mayor es ",num1)
# elif num2>=num1 and num2>=num3:
#     print("El numero menor es ",num2)
# else:
#     print("El mayor es ",num3)


#6. Calcula el precio final con un 10% de descuento si el total es mayor a $100.
# precio=float(input("Ingresa el precio de tu compra: "))
# if precio >=100:
#     descuento=precio*0.10
#     precio_F=precio-descuento
#     print("A su compra se le aplico un 10% de descuento, su precio final es ",precio_F)
# else:
#     print("A su compra no se le aplico el descuento, el precio final es: ",precio)


#7. Verifica si una persona puede votar (mayor o igual a 18).
# edad=int(input("Ingresa tu edad: "))
# if edad >=18:
#     print("Puede votar")
# else:
#     print("No puede votar")


#8. Dado el precio y tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.
# precio=float(input("Ingresa el precio de tu compra: "))
# tipo_de_cliente=input("Que tipo de cliente eres (VIP o normal): ")
# if tipo_de_cliente == "VIP":
#     descuento=precio*0.20
#     precio_final=precio-descuento
#     print("Por ser cliente VIP, se te aplicara el 20 de descuento, por lo tanto tu precio final sera ",precio_final)
# else:
#     print("No se te aplicara descuento, por lo tanto tu precio final es ",precio)


#9.Determina si un numero es multiplo de 5 y de 3 al mismo tiempo
# numero=int(input("Ingrese un numero "))
# if numero % 5 == 0 and numero % 3 == 0:
#     print("El numero es multiplo de 5 y de 3 al mismo tiempo")
# else:
#     print("El numero no es multiplo de ninguno de los dos numeros dados")


#10. Dado un numero, verifica si es divisible entre dos numeros dados.
# numero=int(input("Ingresa un numero "))
# if numero % 2 == 0:
#     print("El numero SI es divisible entre dos")
# else:
#     print("El numero NO es divisible entre dos")

#EJERCICIOS CON LISTAS (con condicionales)

#11. Crea una lista con 5 numeros . si el tercer numero es mayor que 10, muestra "Mayor a diez", si no, muestra "Menor o igual a 10"
# num1=int(input("Ingresa el primer  numero: "))
# num2=int(input("Ingresa el segundo numero: "))
# num3=int(input("Ingresa el tercer  numero: "))
# num4=int(input("Ingresa el cuarto  numero: "))
# num5=int(input("Ingresa el quinto  numero: "))
# numeros=[num1,num2,num3,num4,num5]
# if numeros[2] > 10:
#     print("El numero es mayor a cero ")
# else:
#     print("El numero es menor o igual a cero")

#12. Verifica si el numero 7 esta en la lista [3, 5, 7, 9]. Si esta, muestra "Esta en la lista", si no, muestra "No esta en la lista".
# lista_numeros=[3, 5, 7, 9]
# if 7 in lista_numeros:
#     print("Esta en la lista")
# else:
#     print("NO esta en la lista")

#13. Suma los dos primeros elementos de la lista [4, 6, 2, 8]. Si la suma es mayor que 10, muestra “Suma alta”, de lo contrario, muestra “Suma baja”. 
# numeros=[4, 6, 2, 8]
# suma=numeros[0]+numeros[1]
# if suma > 10:
#     print("Suma alta")
# else:
#     print("Suma baja")

#14. Dada la lista ["Ana", "Luis", "Pedro", "Marta"], muestra el último nombre. Si ese nombre es “Marta”, muestra “Nombre correcto”, si no, “Nombre diferente”.
# nombres=["Ana", "Luis", "Pedro", "Marta"]
# ultimo_nombre=nombres[-1]
# if ultimo_nombre == "Marta":
#     print("Nombre correcto")
# else:
#     print("Nombre diferente")

#15. Crea una lista con tres colores. Cambia el segundo color solo si es igual a "azul", y muestra la lista actualizada.
# color1=input("Ingresa el primer  color: ")
# color2=input("Ingresa el segundo  color: ")
# color3=input("Ingresa el tercer  color: ")
# colores=[color1,color2,color3]
# if color2 == "azul":
#     colores[1] = "celeste"
#     print("Lista actualizada",colores)
# else:
#     print("La lista sigue normal", colores)

#EJERCICIOS COn TUPLAS (con condicionales)

#16. Crea una tupla con los valores (5, 8, 12, 20). Si el primer valor es menor que el último, muestra “Orden ascendente”, si no, “Orden descendente”. 
# numeros=(5, 8, 12, 20)
# if numeros[0] < numeros[-1]:
#     print("Orden ascendente")
# else:
#     print("Orden descentente")

#17. Dada la tupla (25, 32, 28), verifica si el segundo valor es mayor a 30. Si lo es, muestra “Edad mayor a 30”, si no, “Edad menor o igual a 30”.
# edades=(25, 32, 28)
# if edades[1] > 30:
#     print("Edad mayor a 30")
# else:
#     print("Edad menor o igual a 30")

#18. Convierte la tupla (1, 2, 3) a lista, cambia el segundo valor a 10 solo si es igual a 2, luego vuelve a convertirla en tupla y muéstrala.
# numeros=(1, 2, 3)
# lista=list(numeros)
# print(lista)
# if lista [1] == 2:
#     lista[1]==10
#     numeros=tuple(lista)
#     print("Tupla actualizada",numeros)
# else:
#     print("Los numeros o son correctos")

#19. Dada la tupla (4, 9), accede al segundo valor. Si es mayor que 5, muestra “Coordenada alta”, si no, “Coordenada baja”.
# numeros=(4, 9)
# if numeros[1] > 5:
#     print("Coordenada alta")
# else:
#     print("Coordenada baja")

#20. Compara si las tuplas (3, 4) y (3, 5) son iguales. Si lo son, muestra “Tuplas iguales”, si no, “Tuplas diferentes”. 
# tupla1=(3, 4)
# tupla2=(3, 5)
# if tupla1 == tupla2:
#     print("Tuplas iguales")
# else:
#     print("Tuplas diferentes")

#EJERCICIOS CON DICCIONARIOS (CON CONDICIONALES)

#21. Crea un diccionario con {"nombre": "Juan", "edad": 17}. Si la edad es mayor o igual a 18, muestra “Adulto”, si no, muestra “Menor de edad”.
# datos={
#     "nomre":"Juan",
#     "edad":17
# }
# if datos["edad"] >= 18:
#     print("Adulto")
# else:
#     print("Menor de edad")

#22. Crea un diccionario {"nombre": "Lucía", "edad": 20}. Si la edad es mayor a 18, cambia el valor de “edad” a 21. Luego muestra el diccionario. 
# datos={
#     "nombre": "Lucía",
#       "edad": 14
# }
# if datos["edad"] > 18:
#     datos["edad"] = 21
# print(datos)

#23. Crea un diccionario con {"nombre": "Carlos"}. Si la clave “ciudad” no existe, agrégala con el valor “Bogotá” y muestra el diccionario.
# persona={"nombre": "Carlos"}
# if "ciudad" not in persona:
#     persona["ciudad"]="Bogota"
# print(persona)

#24. Dado el diccionario {"producto": "pan", "precio": 1200}, verifica si la clave “precio” existe. Si existe, muestra su valor, si no, muestra “No hay precio”.
# compra={
#     "producto": "pan",
#       "precio": 1200
#       }
# if "precio" in compra:
#     print("El precio del producto es ", compra ["precio"])
# else:
#     print("No hay precio")

#25. Crea un diccionario con {"pan": 1200, "leche": 2000}. Si “pan” está en el diccionario, muestra su precio; si no, muestra “Producto no disponible”.
# compra={
#     "pan": 1200,
#       "leche": 2000
#       }
# if "pan" in compra:
#     print("El precio del pan es ",compra ["pan"])
# else:
#     print("Producto no disponible")
