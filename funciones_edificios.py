import os
import time
import numpy
#por regla de negocio los apartamentos del piso 1 hasta el 7 cuestan 150 millones
# y los apartamentos del 10 al 8 cuestan 200 millones
apartamentos_precio_1=150000000
apartamentos_precio_2=200000000

lista_ruts = []
lista_nombres = []
lista_piso = []
lista_departamento = []
lista_totales = {}
apartamentos = numpy.empty((10,4),object)
apartamentos.fill("🟨")

'''
for x in range(10):#filas
        print(f"piso {contador}\t|", end=" ")
        for y in range(4):#columnas
            print(arreglo_hotel[x][y], end=" ")
        print()
        contador += -1
    
'''

#primera opc del sistema
def mostrar_menu():
    print("""
\t Menú 
1)_ Ver edificio
2)_ Comprar edificio
3)_ Buscar dueño
4)_ Total de ganancias
5)_ Salir
          """)
def validacion_opcion():
    while True:
        try:
            opc = int(input("Ingrese opción: "))
            if opc in(1,2,3,4,5):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")
def ver_edifico():
    os.system('cls')
    print("\t Ver apartamentos")
    contador=10
    print("           1 2 3 4")
    for x in range(10):#filas
        print(f"piso {contador}\t|", end=" ")
        for y in range(4):#columnas
            print(apartamentos[x][y], end=" ")
        print()
        contador += -1
    time.sleep(3)

#------------------------------------------------------
# 2 opcion def
#------------------------------------------------------
def confirmar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if rut >= 1000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")
            
def opc_2():
    while True:
        if 0 not in(apartamentos):
            print("departamentos no disponibles")
            continue
        rut= confirmar_rut()
        if rut in(lista_ruts):
            while True:
                try:
                    otro=int(input("Desea otra compra? (si=1/no=2)"))
                    if otro in(1,2):
                        break
                    else:
                        print("ingrese nro disponible")
                except:
                    print("solo nro enteros")
            if otro==1:
                nombre=validar_nombre()
                piso=int(input("ingrese piso que desea"))
                apartamento=int(input("ingese nro de apartamento"))
                if piso<=5:
                    piso+= -piso*2
                elif piso>=6:
                    piso+= -piso*2
                
                
                if apartamentos[piso-1][apartamento-1]=="🟨":
                    apartamentos[piso-1][apartamento-1]="✅"
                    lista_piso.append(piso-1)
                    lista_departamento.append(apartamento-1)
                
                while True:
                    try:
                        pagar_opc=int(input("Desea pagar? (si?1/no=2)"))
                        if pagar_opc in(1,2):
                            break
                        else:
                            print("ingrese un nro valido")
                    except:
                        print("solo nro enteros")
                if pagar_opc==1:
                    lista_ruts.append(rut)
                    lista_nombres.append(nombre)
                    if (piso-1)>=9 and (piso)<=7:
                        print("cargo de pago automatico a su nombre")
                        lista_totales+=apartamentos_precio_2
                    elif (piso-1)<=0 and (piso-1)>=6:
                        print("cargo de pago automatico a su nombre")
                        lista_totales+=apartamentos_precio_1
                elif pagar_opc==2:
                    print("regresando")
                    continue
            elif otro==2:
                print("regresando")
                continue
        else:
            while True:
                try:
                    otro=int(input("Desea otra compra? (si=1/no=2)"))
                    if otro in(1,2):
                        break
                    else:
                        print("ingrese nro disponible")
                except:
                    print("solo nro enteros")
            if otro==1:
                nombre=validar_nombre()
                piso=int(input("ingrese piso que desea"))
                apartamento=int(input("ingese nro de apartamento"))
                if apartamentos[piso-1][apartamento-1]=="🟨":
                    apartamentos[piso-1][apartamento-1]="✅"
                    lista_piso.append(piso-1)
                    lista_departamento.append(apartamento-1)
                
                while True:
                    try:
                        pagar_opc=int(input("Desea pagar? (si?1/no=2)"))
                        if pagar_opc in(1,2):
                            break
                        else:
                            print("ingrese un nro valido")
                    except:
                        print("solo nro enteros")
                if pagar_opc==1:
                    lista_ruts.append(rut)
                    lista_nombres.append(nombre)
                    if (piso-1)>=9 and (piso)<=7:
                        print("cargo de pago automatico a su nombre")
                        lista_totales+=apartamentos_precio_2
                    elif (piso-1)<=0 and (piso-1)>=6:
                        print("cargo de pago automatico a su nombre")
                        lista_totales+=apartamentos_precio_1
                elif pagar_opc==2:
                    print("regresando")
                    continue
            elif otro==2:
                print("regresando")
                continue
#------------------------------------------------------
    
#------------------------------------------------------
# 3 opcion
#------------------------------------------------------
def buscar_usuario():
    rut=confirmar_rut()
    if rut in lista_ruts:
        posicion= lista_ruts.index(rut)
        print("cargando datos")
        soli_piso=int(input("Ingrese nro de piso_ "))
        nro_apartemento=int(input("ingrese nro de aprtamento_ "))
        Contador=1
        apartamentos=[]
        for x in range(10):
            for y in range(4):
                if apartamentos[x][y]=="🟨":
                    apartamentos.appen(Contador)
        
                
        
    else:
        print("no se encuentra usuario")
#------------------------------------------------------
#4 opcin
#------------------------------------------------------
def cantidad_ganancias():
    print("cargando ganancias")
    print(sum(lista_totales))
    

#------------------------------------------------------
#sistema cierre
#------------------------------------------------------
def cerrar_todo():
    while True:
        try:
            print("Desea cerrar ejercicio? (si=1/no=2)")
            cerrar=int(input(":_"))
            if cerrar in(1,2):
                return cerrar
            else:
                print("numero no valido")
        except:
            print("ERROR solo numeros enteros")    