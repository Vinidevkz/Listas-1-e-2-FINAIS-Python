def ordenarLista(lista):
    n1 = len(lista)

    for i in range(n1):                     
        mudarNumero = False
        for j in range(0, n1 - 1 - i):      
            if lista[j] > lista[j + 1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                mudarNumero = True
        if not mudarNumero:           
            break
    return lista


listaNumeros = [9, 2, 5, 1, 7, 3]
print(ordenarLista(listaNumeros))
