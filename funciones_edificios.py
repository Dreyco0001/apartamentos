import os
import time
import numpy


lista_ruts = []
lista_nombres = []
lista_filas = []
lista_columnas = []
lista_totales = []
apartamentos = numpy.zeros((10,4),int)

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
    contador=1
    for x in range(10):
        print(f"pisos {(x+1)}:", end="   ")
        for y in range(4):
            print(f"nro{y+1} {apartamentos[x][y]}", end=" ")
            contador+=1
        print("\n")
    time.sleep(3)

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