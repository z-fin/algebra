from fractions import Fraction

# variables globales
divA0 = []
divAn = []
raices_posibles = []

# funcion para encontrar divisores de a0(coef independiente) (parte 1)
def para_divisores(a,lista):
    # lista arbitraria de num a chequear
    a_chequear = list(range(-100,100))
    # el loop chequea cada elemeno de la lista a_chequear para ver si el primer parametro es divisible por este num
    # despues le hace append a los num que si son divisores del parametro
    for i in a_chequear:
        if i == 0:
            continue
        elif a % int(i) == 0:
            lista.append(i)

# funcion para encontrar los divisores de a0 y an (coef principal) parte 2
def posiblesRaices(an,x0):
    # aca uso la funcion que defini anteriormente dandole valores a los parametros y printeo los resultados que son los divisores de x0 e xn
    para_divisores(an ,divAn)
    para_divisores(x0,divA0)
    print('los numeros divisibles por', an, 'son:', divAn)
    print('los numeros divisibles por', x0, 'son:', divA0)

# funcion para fabricar las fracciones con los divisores de a0 y an
def fracciones(lista1, lista2):
    lista_fracciones = []

    # for loop que adentro tiene otro for loop jjsjsj 
    # divide o convierte en fraccion dependiendo de para que lo quiero usar
    # porque no me dejaba usar el append con la funcion Fraction. entonces lo dividi en:
    # fracciones (para que se lea facil) 
    # y divisiones (para poder hacer las cuentas)
    for i in lista1:
        for j in lista2:
            # fracciones legibles
            frac1 = Fraction(i,j)
            lista_fracciones.append(frac1) #este append se hace a la lista que defini al principio de esta funcion
            # y divisones
            frac = i / j
            raices_posibles.append(frac) #este append se hace a una lista global que defini en la primera parte
    print('hay', len(lista_fracciones), 'posibles raices')
    lista_fracciones = list(dict.fromkeys(lista_fracciones))
    print(lista_fracciones)

#funcion para reemplazar las posibles raices en el polinomio y chequear cual es la raiz
def polinomio_grado_3(an,bn,cn,x0,lista):
    posiblesRaices(an,x0)
    fracciones(divA0,divAn)
    print(raices_posibles)

    lista_raices = []
    habra_solucion_racional = len(lista)
    # chequea el tamaño de la lista, si no tiene elementos entonces significa que el polinomio no tiene raices racionales
    if habra_solucion_racional != 0:
         # ooootro for loop :')
         # este reemplaza los resultados de la funcion fracciones y hace las cuentas
         # si la cuenta da 0, entonces esa fraccion es raiz
        for i in raices_posibles:
            q = (an) * (i**3) + (bn) * (i**2) + (cn) * i +  (x0) 
            if q == 0:
                lista_raices.append(i)
                print(i,' es una raiz real del polinomio')

    else:
        print('el polinomio',an,'x^3 + ',bn,'x^2 + ',cn,' x + ',x0,' no tiene raices racionales')


#pruebas

polinomio_grado_3(1,0,0,8,raices_posibles)
