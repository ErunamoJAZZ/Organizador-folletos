# Organizador de páginas para hacer folletos

Si algúna vez haz intentado imprimir un documento muy largo, te habrás planteado la posibilidad de imprimirlo a media página. Es decir, de a dos páginas por una cara de una hoja.

Según [la documentación del visor de documentos Evince](http://library.gnome.org/users/evince/stable/print-booklet.html.es "Cómo imprimir folletos en Evince" ), la creación de folletos debe hacerse de forma manual, es decir, colocando los números de las páginas manualmente, e imprimiendo de a 2 páginas por hoja. 
Es decir, que por hoja van 4 páginas (2 por un lado, y 2 por el otro).



## El problema de los folletos muy grandes

La particularidad de los folletos, es que una vez quedan impresos, solo es necesario doblarlos por la mitad y graparlos para que queden en el orden correcto. Pero, ¿qué pasa si voy a imprimir un libro de **400 páginas**?

Para no morir en el intento, creé este programa, que automáticamente genera el orden correcto para imprimir un folleto sin importar el número de páginas que se tengan.

El programa solo tiene una restricción: _el número de páginas debe ser múltiplo de **4**,_ es decir, que en caso de no cumplir esto debe modificarse el PDF. Para ello recomiendo la aplicación **PDF shuffler** (está en los repositorios de cualquier distribución).



## Modo de uso

### Update
Se sigue ejecutando con python. Ahora pregunta el número de páginas y el número de una página en blanco.
Lo que que hace es poner 4 páginas en blanco al inicio y al final, y divide el total de páginas cuadernillos de a 20 páginas (realmente se adaptará segun sea necesario).

Es un poco más complejo, pero permite hacer libros que pueden coserse de forma común.

### Modo obsoleto
Se ejecutaba usando python, seguido del nombre del script, y se le pasa como parámetro el número de páginas del documento.


```
$ python numero-folleto.py 400

 > INICIANDO...


400,1,2,399,398,3,4,397,396,5,6,395,394,7,8,393,392,9,10,391,390,11,12,389,388,13,14,387,386,15,16,385,384,17,18,383,382,19,20,381,380,21,22,379,378,23,24,377,376,25,26,375,374,27,28,373,372,29,30,371,370,31,32,369,368,33,34,367,366,35,36,365,364,37,38,363,362,39,40,361,360,41,42,359,358,43,44,357,356,45,46,355,354,47,48,353,352,49,50,351,350,51,52,349,348,53,54,347,346,55,56,345,344,57,58,343,342,59,60,341,340,61,62,339,338,63,64,337,336,65,66,335,334,67,68,333,332,69,70,331,330,71,72,329,328,73,74,327,326,75,76,325,324,77,78,323,322,79,80,321,320,81,82,319,318,83,84,317,316,85,86,315,314,87,88,313,312,89,90,311,310,91,92,309,308,93,94,307,306,95,96,305,304,97,98,303,302,99,100,301,300,101,102,299,298,103,104,297,296,105,106,295,294,107,108,293,292,109,110,291,290,111,112,289,288,113,114,287,286,115,116,285,284,117,118,283,282,119,120,281,280,121,122,279,278,123,124,277,276,125,126,275,274,127,128,273,272,129,130,271,270,131,132,269,268,133,134,267,266,135,136,265,264,137,138,263,262,139,140,261,260,141,142,259,258,143,144,257,256,145,146,255,254,147,148,253,252,149,150,251,250,151,152,249,248,153,154,247,246,155,156,245,244,157,158,243,242,159,160,241,240,161,162,239,238,163,164,237,236,165,166,235,234,167,168,233,232,169,170,231,230,171,172,229,228,173,174,227,226,175,176,225,224,177,178,223,222,179,180,221,220,181,182,219,218,183,184,217,216,185,186,215,214,187,188,213,212,189,190,211,210,191,192,209,208,193,194,207,206,195,196,205,204,197,198,203,202,199,200,201


 >> Copie y pegue el orden de las páginas
    anterior para imprimir estilo folleto. 

```



## Ejemplo:

Puede verse en el [siguiente Screencast en Youtube](https://www.youtube.com/watch?v=j-UtCMHwHNw "Link al video").
