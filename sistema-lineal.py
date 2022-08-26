#defino funcion de la ecuacion
def ecuacion(x1,x2,x3,x4):
 #defino las ecuaciones a resolver
    ec_1 = -x1 + 2*x2 + x3
    ec_2 = x1 + 3*x2 - x4
    ec_3 = 2*x1 + 3*x3 + x4

 #chequeo si los resultados coinciden para el sistema s
    print('\033[1m PARA EL SISTEMA S:  \033[0m')
 #si cuenta_1 = 2 y cuenta_2 = 0 y cuenta_3 = -1
    if ec_1 == 2 and ec_2 == 0 and ec_3 == -1:
 #entonces es solucion de S
                print('- Es solucion del sistema S porque verifica:')
                print(ec_1, '=', 2)
                print(ec_2, '=', 0)
                print(ec_3, '=', -1)

 #este es para incluir el v que esta ahi en el borde porque no da 2 clavado
    elif 1.9 < ec_1 <= 2 and ec_2 == 0 and ec_3 ==-1:
        print('- Es solucion del sistema S porque verifica:')
        print(ec_1, '≈', 2)
        print(ec_2, '=', 0)
        print(ec_3, '=', -1)

 #estos 3 chequean por que es que no es solucion del sistema S
    elif ec_1 != 2:
        print('-No es solucion porque', ec_1, '=/=', 2)
    elif ec_2 != 0:
        print('-No es solucion porque', ec_2, '=/=', 0)
    elif ec_3 != -1:
        print('-No es solucion porque', ec_3, '=/=', -1)
    else:
      print('No se encontro solucion')

 #chequeo si los resultados coinciden para el sistema homogeneo asociado
    print('\033[1m PARA EL SISTEMA HOMOGENEO ASOCIADO:  \033[0m')

 #si cuenta_1 = 0 y cuenta_2 = 0 y cuenta_3 = 0
    if ec_1 == 0 and ec_2 == 0 and ec_3 == 0:
 #entonces es solucion del sistema homogeneo asociado
                print ('- Es solucion del sistema homogeneo asociado porque verifica:')
                print(ec_1, '=', 0)
                print(ec_2, '=', 0)
                print(ec_3, '=', 0)

 #estos 3 chequean por que no es solucion del sistema homogeneo asociado
    elif ec_1 != 0:
        print('-No es solucion porque', ec_1, '=/=', 0)
    elif ec_2 != 0:
        print('-No es solucion porque', ec_2, '=/=', 0)
    elif ec_2 != 0:
        print('-No es solucion porque', ec_3, '=/=', 0)

print('\033[1m QUEREMOS RESOLVER EL SISTEMA DE ECUACIONES LINEALES S:  \033[0m')
print('{ -x1 + 2*x2 + x3 = 2')
print('{ x1 + 3*x2 - x4 = 0')
print('{ 2*x1 + 3*x3 + x4 = -1')
#llamo a la funcion asignandole valores           
print('\033[4m x=(2,2,1,0) \033[0m')
ecuacion(2,2,1,0)

print('\033[4m y=(1,1,1,4) \033[0m')
ecuacion(1,1,1,4)

print('\033[4m z=(0,0,0,0) \033[0m')
ecuacion(0,0,0,0)

print('\033[4m u=(-2,-5/3,10/3,-7) \033[0m')
ecuacion(-2,-5/3,10/3,-7)

print('\033[4m v=(-1,1/3,1/3,0) \033[0m')
ecuacion(-1,1/3,1/3,0)

print('\033[4m w=(-1,-2,3,-7) \033[0m')
ecuacion(-1,-2,3,-7)
