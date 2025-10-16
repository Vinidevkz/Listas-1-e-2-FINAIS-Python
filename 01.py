listaNumeros = []

finalLista = int(input("Digite o tamanho da lista: "))
intervalo = int(input("Digite o intervalo da lista: "))

for i in range(0,finalLista, intervalo):
    n = int(input("Insira um numero para a lista: "))
    listaNumeros.append(n)

op = int(input("Digite um opção de formatação (1 = N° de  Pares, 2 = N° de Ímpares, 3° = % dos números maiores que 100.): "))

def valuesFormat(list, option):
    if option == 1:
        nPar = 0
        for i in list :
            if i % 2 == 0:
                nPar = nPar + 1
        return "N° de números par: ", nPar
    elif option == 2:
        nImpar = 0
        for i in list :
            if i % 2 != 0:
                nImpar = nImpar + 1
        return "N° de números ímpares: ", nImpar
    elif option == 3:
        pcntCem = 0
        for i in list:
            if i > 100:
                pcntCem = pcntCem + 1
        nLista = len(list)
        total = (pcntCem / nLista) * 100
        return total
    
print(valuesFormat(listaNumeros, op))






