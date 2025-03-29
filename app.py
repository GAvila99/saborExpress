import os

def exibir_nome_programa():
    print(""""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
        case 1:
            print('Cadastrar Restaurante')
        case 2:
            print('Listar Restaurante')
        case 3:
            print('Ativar Restaurante')
        case _:
            finalizar_programa()

def finalizar_programa():
    os.system('cls')
    print('Programa Finalizado!\n')

def exibir_menu():
    print('1- Cadastrar Restaurante')
    print('2- Listar Restaurantes')
    print('3- Ativar Restaurante')
    print('4- Sair\n')



def main():
    exibir_nome_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()
