listaGrande = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(len(listaGrande))


def dividirListaEmDois(lista):

    lista1 = []
    lista2 = []

    tamanhoLista = len(lista) - 1
    tamanhoMetade = tamanhoLista / 2

    for i in range(tamanhoLista):
        if i <= tamanhoMetade:
            lista1.append(lista[i])
        else:
            lista2.append(lista[i])

    return lista1 , lista2

print(dividirListaEmDois(listaGrande))    
