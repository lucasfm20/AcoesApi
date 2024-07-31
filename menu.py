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
            else:
                print("Não está na lista")
            
   # print (lista)
    return lista

def maisItem(lista_palavras):
    
    esc =input("Digite alguma coisa:")

    lista_palavras = esc.split(',')
    for palavra in lista_palavras:
        lista.append(palavra)
    #print(lista)
    return lista

def menu():

    while True:
        
        print()
        print("*"*15)
        print("MENU")
        print("1-Cadastrar 1 item por vez")
        print("2-Cadastrar mais itens por vez")
        print("3-Sair")
        print()
        print("*"*15)
    
        escolha = int(input("Digite um número: "))

        if escolha == 1:
            umItem(lista)
        
        elif escolha == 2:
            maisItem(lista)
        
        elif escolha == 3:
            print("Sair")
            break
        else:
            print("Informe um número válido!!!")

