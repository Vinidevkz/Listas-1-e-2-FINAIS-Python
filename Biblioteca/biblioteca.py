meusLivros = []

livros = [
    {"Nome": "Harry Potter", "Disponibilidade": True, "Usuario": ""}, {"Nome": "O Senhor dos Anéis", "Disponibilidade": True, "Usuario": ""}, {"Nome": "O Pequeno Príncipe", "Disponibilidade": True, "Usuario": ""}, {"Nome": "Percy Jackson", "Disponibilidade": True, "Usuario": ""}
]

def listarLivros():
    print("=== LIVROS NA BIBLIOTECA ===")
    for i in range(len(livros)):   # range(3)
        livro = livros[i]
        print(f"{i} - {livro['Nome']} | Disp: {livro['Disponibilidade']} | Usuario: {livro['Usuario']}")

    print()

def pegarLivro(usuario, bookIndice):
    try:
        if livros[bookIndice]["Disponibilidade"] == False:
            print("Esse livro já está emprestado!\n")
            return
        
        livroPego = livros[bookIndice]["Nome"]
        livros[bookIndice]["Disponibilidade"] = False
        livros[bookIndice]["Usuario"] = usuario

        meusLivros.append(livroPego)

        print(f"{usuario} pegou o livro: {livroPego}\n")
    except:
        print("Houve um erro ao pegar o livro, tente novamente mais tarde.")

def devolverLivro(usuario, nomeLivro):
    try:
        for livro in livros:
            if livro["Nome"] == nomeLivro and livro["Usuario"] == usuario:
                livro["Disponibilidade"] = True
                livro["Usuario"] = ""
                meusLivros.remove(nomeLivro)
                print(f"{usuario} devolveu o livro: {nomeLivro}\n")
                return
    except:
        print("Não encontrei esse livro como emprestado por esse usuário!\n")

opcao = 1        

while opcao != 0:
    print("###BEM-VINDO(A) A BIBLIOTECA###")
    print("Digite os seguintes numeros para realizar uma ação: \n 1: Listar todos os livros disponíveis \n 2: Pegar um livro para você \n 3: Devolver um livro \n 4: Ver meus livros \n 0: Sair do programa")

    opcao = int(input("Digite um número: "))

    if opcao == 1:
        print(listarLivros())
    elif opcao == 2:
        nome = str(input("Digite seu nome de usuario: "))
        indiceDoLivro = int(input("Digite o indice do livro que deseja pegar na lista(de 0 a 3): "))

        pegarLivro(nome, indiceDoLivro)
        print("-------")
    elif opcao == 3:
        nome = str(input("Digite seu nome de usuario: "))
        indiceDoLivro = str(input("Digite o nome do livro que deseja DEVOLVER: "))

        devolverLivro(nome, indiceDoLivro)
        print("-------")
    elif opcao == 4:
        print("Seus livros: ")

        print("\n", meusLivros, "\n")
    elif opcao == 0:
        opcao = 0
        print("---FIM DO PROGRAMA---")
    else:
        print("Numero inválido. Digite novamente. \n")