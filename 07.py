tempoEmMinutos = int(input("Digite o tempo do cronometro em minutos:"))

segundos = tempoEmMinutos * 60

for i in range(segundos, -1, -1):
    print(i)