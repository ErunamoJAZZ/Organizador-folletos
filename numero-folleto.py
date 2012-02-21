# -*- encoding: utf-8 -*-

'''
@param : Recibe el número n de páginas (multiplo de 4).
@Sumary: Este programa crea el orden en que las páginas 
         deben ser impresas, según el número de páginas
         n del documento pdf.  
'''

import sys





def ordenar_paginas(n):
	'''Recibe el número de páginas a ordenar''' 
	
	string_ordenado=''

	# m:número de holas. 
	for m in range(n/4):
		#Cada hoja tiene 2 caras
		m=m*2 
		
		# a..d: son páginas.
		# reglas de ordenamiento (Es mágia, no tocar :P ) 
		a, b, c, d = n-m, m+1, m+2, n-m-1
		
		#Se junta todas las páginas separadas por comas.
		string_ordenado = string_ordenado + str(a) +','+ str(b)+ ','+ str(c) +','+ str(d) +',';
	
	return string_ordenado[:-1]



def main():
	'''Main del programa.'''

	#Si no hay argumentos, Termina.
	try:
		n = int(sys.argv[1])
	except:
		print("\n\n  >> ERROR!: Debe colocar el número de páginas.\n\n")
		sys.exit(1)
	
	
	#El n debe ser multiplo de 4.
	if n%4==0 :
		print("\n > INICIANDO...\n\n")
		print( ordenar_paginas(n) )
		print("\n\n >> Copie y pegue el orden de las páginas\n    anterior para imprimir estilo folleto. \n\n")
		sys.exit(0)
    
	else:
		print("\n\n  >> ERROR!: el número de páginas debe ser múltiplo de 4.\n\n")
		sys.exit(1)



main()
