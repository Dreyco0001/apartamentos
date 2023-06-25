import funciones_edificios as fe

while True:
    fe.mostrar_menu()
    opc=fe.validacion_opcion()
    if opc==1:#ver edificio
        fe.ver_edifico()
    elif opc==2:#comprar edificio
        fe.opc_2()
    elif opc==3:#buscar dueño
        pass
    elif opc==4:#Total de ganancias
        pass
    else:#cierre de sistema (terminado)
        cerrar=fe.cerrar_todo()
        if cerrar==1:
            break
        elif cerrar==2:
            continue