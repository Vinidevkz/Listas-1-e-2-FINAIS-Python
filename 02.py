def progressaoAritmetica(a1, n , r):
    total = a1 + (n -1) * r
    return(total)
def progressaoGeometrica(a1, q, n):
    total = a1 * (q ** (n -1))
    return total

op = int(input("Digite uma opção (1 = PA, 2 = PG): "))

if op == 1:
    a1 = int(input("Digite o termo a1: "))
    n = int(input("Digite a posição do termo: "))
    r = int(input("Digite a razão: "))
    print(progressaoAritmetica(a1, n, r))
elif op == 2:
    a1 = int(input("Digite o termo a1: "))
    q = ((a1 + 1) / a1)
    n = int(input("Digite a posição do termo desejado: "))
    print(progressaoGeometrica(a1, q, n))
else:
    print("Número inválido.")

