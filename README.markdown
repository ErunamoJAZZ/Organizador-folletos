# Organizador de páginas para hacer folletos

Si algúna vez haz intentado imprimir un documento muy largo, te habrás planteado la posibilidad de imprimirlo a media página. Es decir, de a dos páginas por una cara de una hoja.

Según [la documentación del visor de documentos Evince](http://library.gnome.org/users/evince/stable/print-booklet.html.es "Cómo imprimir folletos en Evince" ), la greación de folletos debe hacerse de forma manual, es decir, colocando los números de las páginas manualmente, e imprimiendo de a 2 páginas por hoja. 
Es decir, que por hoja van 4 páginas (2 por un lado, y 2 por el otro).



## El problema de los folletos muy grandes

La particularidad de los folletos, es que una vez quedan impresos, solo es necesario doblarlos por la mitad y graparlos para que queden en el orden correcto. Pero, ¿qué pasa si voy a imprimir un libro de **400 páginas**?

Para no morir en el intento, creé este programa, que automáticamente genera el orden correcto para imprimir un folleto sin importar el número de páginas que se tengan.

El programa solo tiene una restricción: _el número de páginas debe ser múltiplo de **4**,_ es decir, que en caso de no cumplir esto debe modificarse el PDF. Para ello recomiendo la aplicación **PDF shuffler** (está en los repositorios de cualquier distribución).



## Modo de uso

Se ejecuta usando python, seguido del nombre del script, y se le pasa como parámetro el número de páginas del documento.

`$ python numero-folleto.py 400`



## Ejemplo:

Puede verse en el siguiente Screencast en Youtube.
