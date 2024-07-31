import listaAcoes
lista = []
def umItem(lista):
    
    listaDeAcoes=listaAcoes.listaDasAcoes()
    while True:

        esc =input("Digite alguma coisa:")

        if esc=='parar':
            break
        else:
            if esc in listaDeAcoes:
                lista.append(esc)
                print (esc)
            else:
                print("Não está na lista")
            
    print (lista)
    return lista

def maisItem():
    lista =[]
    esc =input("Digite alguma coisa:")

    lista_palavras = esc.split(',')
    lista_palavras = [palavra.strip() for palavra in lista_palavras]
    print(lista_palavras)


def menu():

    while True:
        
        print()
        print("*"*15)
        print("MENU")
        print("1-Cadastrar")
        print("2-Selecionar")
        print("3-Sair")
        print()
        print("*"*15)
    
        escolha = int(input("Digite um número: "))

        if escolha == 1:
            umItem(lista)
        
        elif escolha == 2:
            print("Escolha selecionar")
        
        elif escolha == 3:
            print("Sair")
            break
        else:
            print("Informe um número válido!!!")

   