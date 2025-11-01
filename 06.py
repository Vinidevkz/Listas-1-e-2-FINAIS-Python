def buscaBinaria(lista, target):
    inicio = 0
    fim = len(lista) - 1

    for i in range(len(lista)): 
        meio = (inicio + fim) // 2

        if lista[meio] == target:
            return meio
        elif lista[meio] < target:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1  

nums = [2, 5, 7, 9, 12, 20, 25, 30, 31, 50]
print(buscaBinaria(nums, 20))
