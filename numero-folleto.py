# -*- encoding: utf-8 -*-

'''
@param : Recibe el número n de páginas (multiplo de 4).
@Sumary: Este programa crea el orden en que las páginas
         deben ser impresas, según el número de páginas
         n del documento pdf.
'''

import sys


def ordenar_cuad(lista_cuad):
    '''ordena cada una de las sublistas en el orden correcto
    para que los cuadernillos queden como folletos.'''
    for index in range(len(lista_cuad)):
        old = lista_cuad.pop(index)
        new = []
        while len(old) > 0:
            new.append(old.pop())
            new.append(old.pop(0))
            new.append(old.pop(0))
            new.append(old.pop())

        lista_cuad.insert(index, new)

    return lista_cuad


def gestor_cuadernillos(n, blanco, pags_por_cuad=20):
    '''Gestiona la realización de los cuadernillos
    para el cosido del libro.'''

    def grupo(pag_cuad, lista, index):
    '''Va creando grupos de cuadernillos y 
    devualve la lista ya armada.'''
        if len(lista) == pag_cuad:
            print lista, pag_cuad
            return list(lista)
        else:
            return grupo(pag_cuad, lista + [(numero_pag(index))], index + 1)

    def numero_pag(index):
    '''Va generando de forma iterativa la numeración
    exacta para el libro, dejando 4 páginas al inicio
    y al final para no dañar el libro con las futuras
    "guardas" (cartulina entre la pasta y el libro).'''
        # [----|--.....---|----]
        if (index <= 4) or (index > n + 4):
            return blanco
        else:
            return index - 4

    def generador(num_cuad, pags_por_cuad, residuo):
    '''Genera una lista de listas de cuadernillos, 
    todos en el orden correcto para su impresión.'''
        new = list()
        index = 1
        while num_cuad > 0:
            aux = list()
            if residuo == 0:
                aux = grupo(pags_por_cuad, list(), index)
                new.append(aux)
                index += pags_por_cuad
            else:
                aux = grupo(pags_por_cuad + 4, list(), index)
                new.append(aux)
                index += (pags_por_cuad + 4)
                residuo -= 1
            num_cuad -= 1
        return new

    #Calcula bien cuantas hojas debe tener cada cuadernillo.
    while True:
        if ((n + 8) % pags_por_cuad) > ((n + 8) / pags_por_cuad):
            pags_por_cuad += 4
            #multiplos de 4
        else:
            break

    #El residuo siempre será una hoja (4 paginas)
    residuo = ((n + 8) % pags_por_cuad) / 4
    num_cuad = (n + 8) / pags_por_cuad

    cuadernillos = generador(num_cuad, pags_por_cuad, residuo)
    return ordenar_cuad(cuadernillos)


def print_list(lista):
   '''imprimer la lista ta y como debe copiarse en Evince.'''
    txt = ""
    for i in lista:
        for j in i:
            txt = txt + str(j) + ","
    print txt[:-1]


def main():
    '''Main del programa.'''

    #Si no hay argumentos, Pregunta las páginas.
    try:
        n = int(sys.argv[1])
    except:
        n = input("→ Escriba el número de páginas: ")
        blanco = input("\n→ Escriba el número de alguna página en blanco: ")

    #El n debe ser multiplo de 4.
    if n % 4 == 0:
        print("\n > INICIANDO...\n\n")

        tmp = gestor_cuadernillos(n, blanco)
        print_list(tmp)
        sys.exit(0)

    else:
        print("\n\n  >> ERROR!: el número de páginas debe ser múltiplo de 4.\n\n")
        sys.exit(1)


main()
