import os

# Lista global para armazenar os nomes dos restaurantes cadastrados
restaurantes = []

def exibir_nome_programa():
    """
    Exibe o nome do programa com um banner estilizado.
    """
    print(""""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def opcao_invalida():
    """
    Exibe uma mensagem de erro para opções inválidas e retorna ao menu principal.
    """
    print('Opcao Invalida!\n')
    input('Pressione uma tecla para voltar ao menu principal')
    main()  # Retorna ao menu principal

#Permite ao usuário cadastrar um novo restaurante.
#O nome do restaurante é adicionado à lista global 'restaurantes'.
def cadastrar_restaurante():
    os.system('cls')  # Limpa a tela
    print('Cadastro de Restaurante.\n')
    
    
    nome_restaurante = str(input('Digite o nome do restaurante: '))  # Solicita o nome do restaurante
    if nome_restaurante == '':
        os.system('cls')
        print('Digite um nome valido!\n')
        input('Pressione uma tecla para voltar ao menu principal')
        cadastrar_restaurante()
    else:
        restaurantes.append(nome_restaurante)  # Adiciona o restaurante à lista
        print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
        input('\nPressione uma tecla para voltar ao menu principal')
        main()  # Retorna ao menu principal

#Exibe a lista de restaurantes cadastrados.
def listar_restaurante():
    os.system('cls')  # Limpa a tela
    print('Lista de restaurantes\n')
    for restaurante in restaurantes:  # Itera sobre a lista de restaurantes
        print(f'. {restaurante}')  # Exibe cada restaurante
    input('\nPressione uma tecla para voltar ao menu principal')
    main()  # Retorna ao menu principal

def escolher_opcao():
    """
    Solicita ao usuário que escolha uma opção do menu.
    Executa a função correspondente à opção escolhida.
    """
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))  # Solicita a entrada do usuário
        match opcao_escolhida:  # Estrutura de correspondência para as opções
            case 1:
                cadastrar_restaurante()  # Opção para cadastrar restaurante
            case 2:
                listar_restaurante()  # Opção para listar restaurantes
            case 3:
                print('Ativar Restaurante')  # Opção para ativar restaurante (não implementada)
            case 4:
                finalizar_programa()  # Opção para finalizar o programa
            case _:
                opcao_invalida()  # Opção inválida
    except:
        opcao_invalida()  # Trata entradas inválidas (não numéricas)

#Finaliza o programa exibindo uma mensagem de encerramento.
def finalizar_programa():
    os.system('cls')  # Limpa a tela
    print('Programa Finalizado!\n')

def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis.
    """
    print('1- Cadastrar Restaurante')
    print('2- Listar Restaurantes')
    print('3- Ativar Restaurante')
    print('4- Sair\n')

def main():
    """
    Função principal do programa.
    Exibe o banner, o menu e solicita a escolha do usuário.
    """
    os.system('cls')  # Limpa a tela
    exibir_nome_programa()  # Exibe o banner do programa
    exibir_menu()  # Exibe o menu principal
    escolher_opcao()  # Solicita a escolha do usuário

if __name__ == '__main__':
    main()  # Inicia o programa