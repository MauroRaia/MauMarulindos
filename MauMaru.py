palabra1 = "Hola mundo"
 
palabra = "Hola Mundo"
palabra = palabra[::-1]

a = {palabra1: palabra}
for a in a.interitems(): 
    print palabra, palabra1  

numero = 0 
while numero < 10:
    print a 
    numero += 1