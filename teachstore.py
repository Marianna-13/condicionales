#INICIO DE SESION 
clientes= [("Ana Torre", "C001", "ana@gmail.com"),  ("Juan Perez", "C002", "luis@gmail.com")]

intentos= 1 

while intentos <= 3:
    codigo = input("Ingrese su codigo por favor: ")
    if codigo == "C001":
        print("Bienvenido a TeochStore ")
        break
    if codigo == "C002":
        print("Bienvenido a TeochStore ")
        break
    intentos += 1
else:
    print("Codigo incorrecto, sigue intentando")

print("\n HISTORIAL DE COMPRA \n audifonos, 45000")




