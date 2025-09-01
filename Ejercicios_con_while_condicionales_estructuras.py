#EJRCICIOS CON WHILE, CONDICIONALES Y ESTRUCTURAS

#1. Suma hasta cero.
"""total = 0  # acumulador

while True:
     numero = int(input("Ingresa un número entero (0 para terminar): "))
     if numero == 0:
         break   # sale del bucle si el número es 0
     total += numero

print("La suma total es:", total)"""



#2. Contraseña secreta

"""while True:
    contrasena=input("Ingresa la contraseña: ")

    if contrasena == "jirafa":
        print("Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta, sigue intentando")"""
    
    


#3. Lista de compras
"""
productos = []  #lista vacía para guardar los productos

while True:
    producto = input("Ingresa un producto (escribe 'fin' para terminar): ")
    if producto.lower() == "fin":  #si escribe fin, se detiene
        break
    productos.append(producto)  #agrega el producto a la lista

print("La lista de productos es:")
print(productos)
"""



#4. Contador de pares e impares
"""pares = 0
impares = 0
contador = 0

while contador < 10:   #se repite hasta que el usuario ingrese 10 números
    numero = int(input("Ingresa un número: "))
    
    if numero % 2 == 0:   #Si el residuo es 0, es par
        pares += 1
    else:
        impares += 1
    
    contador += 1   #aumenta el conteo de números ingresados
    

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)"""
 


#5. Promedio de calificaciones
"""notas=[]
while True:
       numero=(input("Ingresa tus notas entre 0 y 5 (SALIR para terminar): "))
       
       if numero == "SALIR":
           break
       numero=float(numero)

       if numero >=0 and numero <=5:
          notas.append(numero)       
       else:
           print("La nota debe estar entre 0 y 5")

if len(notas)>0:       
    promedio=sum(notas)/len(notas)
    print(notas) 
    print("El promedio de las notas es: ",promedio) 
else:
    print("No se ingresaron las notas correctamente") """
    


#6. Tabla de multiplicar interactiva
"""numero=int(input("Ingresar numero de la tabla de multiplicar "))
i=1

while i <=10:
     print(f"{numero} * {i} = {numero * i}")
     i += 1 """



#7. Adivina el numero
"""secreto=17
print("Adivina el numero secreto entre 1 y 100")
intento=None
while intento != secreto:
     intento=int(input("Ingresa un numero: "))

     if intento < secreto:
         print("El numero secreto es mayor")
     elif intento > secreto:
         print("El numero secreto es menor")
     else:
         print("Adivinaste el numero")"""


#8.Tupla de frutas
"""frutas=("Mango","Fresa","Uva","Mayacuya")
print("Adivina una de las frutas ")

while True:
    intento=input("Ingresa una fruta hasta adivinar: ")

    if intento in frutas:
        print("Lo conseguiste")
        break
    else:
        print("Sigue intentando")"""


#9. Diccionario de traduccion
"""diccionario={
   "gato":"cat",
   "perro":"dog",
   "pajaro":"bird",
   "oveja":"sheep",
   "pez":"fish"
}
print("Diccionario ingles español")

while True:
    palabra=input("Ingresa un amimal en español: ").lower()

    if palabra == "salir":
        print("Hasta luego")
        break

    if palabra in diccionario:
        print(f"La traduccion de {palabra} es {diccionario[palabra]}\n")
    else:
        print(f"La {palabra} no esta en el diccionario. \n")"""


#10. Calculadora basica
"""while True:
    print("Operaciones")
    print("1. sumar")
    print("2. restar")
    print("3. multiplicar")
    print("4. dividir")
    print("5. salir")

    opcion=input("Eligue una opcion (1-5): ")

    if opcion == "5":
        print("Hasta luego")
        break

    if opcion in ["1","2","3","4","5"]:
        num1=int(input("Ingresa el primer numero: "))
        num2=int(input("Ingresa el segundo numero: "))

    if opcion == "1":
        resultado=num1+num2
        print(f"Resultado: {num1} + {num2} = {resultado}")
    elif opcion == "2":
        resultado=num1-num2
        print(f"Resultado: {num1} - {num2} = {resultado}")
    elif opcion == "3":
        resultado=num1*num2
        print(f"Resultado: {num1} * {num2} = {resultado}")
    elif opcion == "4":
        resultado=num1/num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Opcion invalida, intenta de nuevo")
        break"""
             



#11. Registro de edades
"""personas={}
while True:
    nombre=input("Ingresa un nombre (Para terminar SALIR): ")

    if nombre == "salir":
        break

    edad=int(input(f"Ingrese la edad de {nombre}: "))

    if edad >=0:
        personas[nombre] = (edad)
    else:
        print("Por favor ingresa un numero valido para la edad ")

print(f"El registro de personas y sus edades es {personas}")"""
   

#12. Bucar en lista
"""print("Adivina el color")
colores=["Azul","Verde","Amarillo","Rojo","Morado"]

while True:
    intento=input("Ingresa un color: ")
    if intento in colores:
        print("Lo conseguiste")
        break
    else:
        print("Sigue intentando")"""
    
        
#13. Potencias de un numero
""""numero=int(input("Ingresa un numero: "))
potencia=1
while potencia <= 5:
    resultado=numero**potencia
    print(f"{numero} elevado a la {potencia} = {resultado}")
    potencia += 1"""


#14. Lista de cuadrados
"""numero_cuadrados=[]
contador=1
while contador <= 5:
    numero=int(input(f"Ingrese el numero {contador}: "))
    numero_cuadrados.append(numero**2)
    contador +=1
print(numero_cuadrados)"""


#15. Diccionario estudiantes
"""estudiantes={}
while True:
    nombre=input("Ingresa el nombre del estudiante (FIN para terminar): ")

    if nombre.lower() == "fin":
        break

    nota = float(input(f"Ingrese la nota final de {nombre}: "))

    if nota >=0 and nota <=5:   
        estudiantes[nombre] = nota
    else:
        print("La nota debe estar entre 0 y 5")

print(f"El registro de estudiantes y notas es {estudiantes}")"""


