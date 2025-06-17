# LISTAS: Dato complejo. Corresponde a una colección arbitraria de objetos.
# list[obj1,obj2,obj3...objn]

lista = [1,2,3,4,5]

# En las listas no se puede modificar el orden. Si el contenido

lista2 = ["t1","t2","t3"]
print(lista2)

lista2[0] = "a"
print(lista2) # [a,t2,t3]

lista3 = [1,'a',0.92,'texto']
print(lista3[0:3:2]) #[1, 0.92]

lista4 = lista3[::-1] # De esta manera se puede invertir el orden de lista3 guardado en la variable lista4
print(lista4) # ['texto', 0.92, 'a', 1]
 
texto = "Hola Mundo"
print(texto[:])
print(texto[:] is texto) # True


lista = [1,2,3]
lista2 = [7,2,6]
print(lista + lista2) # [1, 2, 3, 7, 2, 6]
print(lista * 2) # [1, 2, 3, 1, 2, 3]
print(min(lista)) # 1
print(max(lista)) # 3
print(len(lista)) # 3 (longitud)

lista3 = ["texto2", "~~~~~","texto3"]
print(min(lista3)) # texto2
print(max(lista3)) # ~~~~~

lista4 = [4,5,6]
print(lista4 + [9]) # [4, 5, 6, 9] -> Se puede añadir un elemento a una lista

lista5 = [1, [2, [3,4],5],6]
print(lista5[1]) # [2, [3, 4], 5]
print(lista5[1][1]) # [3, 4]

