import listaAcoes
import time

lista = []
listaDeAcoes=listaAcoes.listaDasAcoes()
def umItem(lista):
    
    
    while True:

        esc =input("Digite uma ação:")

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
    
    esc =input("Digite as ações separadas por vírgula:")

    lista_palavras = esc.split(',')
    for palavra in lista_palavras:
        if palavra in listaDeAcoes:
            lista.append(palavra)
        else:
            print()
            print(f"{palavra} não está na lista!!")
            print()
            time.sleep(1.0)
    return lista

def listaPersonalizada(lista):
    listaPer=['KNHY11','MXRF11','VRTA11','TGAR11','XPML11','CPTS11','BRSR6','AERI3','MGLU3','VALE3F','IRBR3','BHIA3','PCAR3','TSLA34']
    for acao in listaPer:
        lista.append(acao)

    return lista

def menu():

    while True:
        
        print()
        print("*"*15)
        print("MENU")
        print("1-Cadastrar 1 ação por vez")
        print("2-Cadastrar mais ações por vez")
        print("3-Lista personalizada")
        print("4-Sair")
        print()
        print("*"*15)
    
        escolha = int(input("Digite um número: "))

        if escolha == 1:
            umItem(lista)
            break
        elif escolha == 2:
            maisItem(lista)
            break
        elif escolha == 3:
            listaPersonalizada(lista)
            break
        elif escolha == 4:
            print("Saindo")
            time.sleep(1.0)
            break
        else:
            print("Informe um número válido!!!")

# executável pyinstaller --onefile  main.py