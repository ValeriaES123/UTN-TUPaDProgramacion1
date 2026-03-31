#Ejericio 1
nombre=input("Ingrese el nombre del cliente").strip()
while not nombre.isalpha():
      nombre = input("Error. Solo letras. Intente de nuevo: ")

cantidad_productos=input("Ingrese cantidad de productos a comprar")
while not cantidad_productos.isdigit() or cantidad_productos==0:
     cantidad_productos=input("Ingrese una cantidad válida")
cantidad_productos=int(cantidad_productos)

total_a_pagar_sindesc=0
total_a_pagar=0

for cont in range(cantidad_productos):
    print("ingrese el precio del producto",(cont+1))
    precio_s=int(input())
    total_a_pagar_sindesc+=precio_s
    print("¿Tiene descuento?, S o N")
    descuento=input().lower()
    while not descuento.isalpha() or (descuento!="s" and descuento!="n"):
         print("Ingrese s o n")
         descuento=input()
    if descuento=="s":
        precio=0.9*precio_s
    else:
         precio=precio_s
        
    total_a_pagar+=precio


promedio=float(total_a_pagar/cantidad_productos)

print(f"El total sin descuentos es, {total_a_pagar_sindesc}")
print(f"El total con descuentos es, {total_a_pagar}")
print(f"El ahorro fue de, {total_a_pagar_sindesc-total_a_pagar}") 
print(f"El promedio es: {promedio:.2f}") 

#Ejercicio 2
usuario_correcto="alumno"
contraseña_correcta="phyton123"
cont=1
while cont<=3:
    print("Intento", cont, "/3")
    usuario=input("Ingrese nombre de usuario")
    contraseña=input("Ingrese contraseña")
    if usuario!=usuario_correcto or contraseña!=contraseña_correcta:
        print("Credenciales inválidas. Intente nuevamente")
        cont+=1
    else:
        print("Elija \n 1 para ver su estado de inscripción \n 2 para cambiar su clave \n 3 Mensaje motivador \n 4 Salir")
        entrada=input()
        while not entrada.isdigit() or entrada not in ["1","2","3","4"]:
             print("Opcion invalida. Ingrese nuevamente.")
             entrada=input()
        if entrada=="1":
             print("Inscripto")
        elif entrada=="2":
            cambio=input("Ingrese nueva contraseña")
            confirmacion=input("Confirme su clave")
            while cambio!=confirmacion or len(cambio)<6:
                print("Intente nuevamente, las claves no coinciden o tienen menos de 6 caracteres")
                cambio=input("Ingrese nueva contraseña")
                confirmacion=input("Confirme su clave")
            print("Cambio exitoso")
        elif entrada=="3":
             print("Sigue así")
        else:
             print("Salir")   
        break
if cont > 3:
    print("Intentos agotados")

#Ejercicio 3
L1=L2=L3=L4=M1=M2=M3=""
operador=input("Ingrese nombre operador")
menu=input("Ingrese 1 para reservar turno \n 2 para cancelar turno \n 3 agenda del dia \n 4 Resumen").strip()
while not menu.isdigit() or (menu!=1 and menu!=2 and menu!=3 and menu!=4):
    print("incorrecto, ingrese 1,2,3 o 4")
    menu=input("Ingrese 1 para reservar turno \n 2 para cancelar turno \n 3 agenda del dia \n 4 Resumen").strip()
paciente=input("ingrese nombre del paciente").strip()
while not paciente.isalpha():
    print("Error, ingrese un nombre válido")
    paciente=input("ingrese nombre del paciente").strip()
if menu=="1":
    dia=input("Elija dia Lunes L o martes M")
    if dia=="L":
        if L1=="":
            turno=paciente
            print("turno asignado")
        elif L2=="":
            turno=paciente
            print("turno asignado")
        elif L3=="":
            turno=paciente
            print("turno asignado")
        elif L4=="":
            turno=paciente
            print("turno asignado")
        else:
            print("turno ocupado")
        
    else:
        turno=input("Elija M1, M2")
        turno=paciente
        if M1=="":
            turno=paciente
            print("turno asignado")
        elif M2=="":
            turno=paciente
            print("turno asignado")
        elif M3=="":
            turno=paciente
            print("turno asignado")
        else:
            print("turno ocupado")
#Ejercicio 4
cerraduras_porabrir=3
energia=100
tiempo=12
cerraduras_abiertas=0
alarma=False
codigo_parcial=""
print(cerraduras_porabrir)
print(energia)
print(tiempo)
print(cerraduras_abiertas)
print(alarma)
print(codigo_parcial)
eleccionesmenu_1=0

while cerraduras_abiertas<3 and energia>0 and tiempo >0:
    menu=input("Ingrese 1 para forzar cerradura, 2 para hackear y 3 para descansar").strip()
    while not menu.isdigit() or (menu!="1" and menu!="2" and menu!="3"):
        print("menu incorrecto")
        menu=input("Ingrese 1 para forzar cerradura, 2 para hackear y 3 para descansar").strip()
    menu=int(menu)
    if menu==1:
        eleccionesmenu_1+=1
        if eleccionesmenu_1<3:
            energia-=20
            tiempo-=2
            if energia>=40:
                cerraduras_abiertas+=1
                cerraduras_porabrir-=1
                print("se abrió una cerradura")
            else:
                numero=input("Elija 1,2 o 3").strip()
                while not numero.isdigit() or (numero!="1" and numero!="2" and numero!="3"):
                    print("opcion incorrecta")
                    numero=input("Elija 1,2 o 3").strip()
                    numero=int(numero)
                    if numero==3:
                        alarma=True
                    else:
                        cerraduras_abiertas+=1
                        cerraduras_porabrir-=1
                        print("se abrió una cerradura")
        else:
            print("Bloqueado. perdiste")
            break

    elif menu==2:
        energia-=10
        tiempo-=3
        for i in range(4):
            codigo_parcial+="A"
        if len(codigo_parcial)>=8:
            cerraduras_abiertas+=1
            cerraduras_porabrir-=1
            codigo_parcial=""
            print("se abrió una cerradura")

    elif menu==3:
        energia+=15
        tiempo-=1
        if alarma==True:
            energia-=10
        if energia > 100:
            energia = 100
    if alarma==True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma. PERDISTE")
        print("cerraduras_porabrir",cerraduras_porabrir)
        print("energia",energia)
        print("tiempo",tiempo)
        print("cerraduras_abiertas",cerraduras_abiertas)
        print("alarma",alarma)
        print("codigo_parcial",codigo_parcial)
        break
    if energia<=0 or tiempo<=0:
        print("PERDISTE, te quedaste sin tiempo o sin energía")
        print("cerraduras_porabrir",cerraduras_porabrir)
        print("energia",energia)
        print("tiempo",tiempo)
        print("cerraduras_abiertas",cerraduras_abiertas)
        print("alarma",alarma)
        print("codigo_parcial",codigo_parcial)
        break
print("cerraduras_porabrir",cerraduras_porabrir)
print("energia",energia)
print("tiempo",tiempo)
print("cerraduras_abiertas",cerraduras_abiertas)
print("alarma",alarma)
print("codigo parcial", codigo_parcial)   
if cerraduras_abiertas==3:
    print("Ganaste")

#Ejercicio 5
Vida_del_Gladiador=100 
Vida_del_Enemigo=100 
Pociones_de_Vida=3 
Daño_base_Ataque_Pesado=15
Daño_base_enemigo=12 
Turno_Gladiador=True

nombregladiador=input("Ingrese el nombre del gladiador").strip()
while not nombregladiador.isalpha():
   nombregladiador=input("Ingrese un nombre válido (Sólo letras)") 
while Vida_del_Enemigo>0 and Vida_del_Gladiador>0:
    print(f"\n Vida del gladiador: {Vida_del_Gladiador}.\n Vida del enemigo: {Vida_del_Enemigo} \n Pociones: {Pociones_de_Vida}")
    opciones=input("Elija 1: Ataque Pesado. 2. Ráfaga Veloz 3. Curar").strip()
    while not opciones.isalpha() and opciones!="1" and opciones!="2" and opciones!="3":
        opciones= input("Ingrese una opción válida")
    opciones=int(opciones)
    if opciones==1:
        if Vida_del_Enemigo<20:
            ataque=Daño_base_Ataque_Pesado*1.5
            Vida_del_Enemigo-=Daño_base_Ataque_Pesado*1.5
        else:
            Vida_del_Enemigo-=Daño_base_Ataque_Pesado
            ataque=Daño_base_Ataque_Pesado
        print(f"¡Atacaste al enemigo por {ataque} puntos de daño!")
    
    elif opciones==2:
        for i in range(3):
            Vida_del_Enemigo-=5
            print("Golpe conectado por 5 de daño")
    
    elif opciones==3:
        if Pociones_de_Vida>0:
            Vida_del_Gladiador+=30
            Pociones_de_Vida-=1
        else:
            print("Te quedaste sin pociones")
    print("Ataque del enemigo")
    Vida_del_Gladiador-=12
    print("¡El enemigo te atacó por 12 puntos de daño!")
if Vida_del_Gladiador>0:
    print("Ganaste")
else:
    print("Perdiste")