import os

# Lista global para armazenar os nomes dos restaurantes cadastrados
restaurantes = []

#Exibe o nome do programa com um banner estilizado
def exibir_nome_programa():
    print(""""
      
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

#Gera mensagem de voltar ao menu
def voltar_ao_menu():
    input('\nPressione uma tecla para voltar ao menu principal')
    main()  # Retorna ao menu principal

# Exibe uma mensagem de erro para opções inválidas e retorna ao menu principal.
def opcao_invalida():
    print('Opcao Invalida!\n')
    input('Pressione ENTER para voltar ao menu principal')
    main()  # Retorna ao menu principal

#Permite ao usuário cadastrar um novo restaurante.
#O nome do restaurante é adicionado à lista global 'restaurantes'.
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de Restaurante.')
    nome_restaurante = str(input('Digite o nome do restaurante: '))  # Solicita o nome do restaurante
    restaurantes.append(nome_restaurante)  # Adiciona o restaurante à lista
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu()

#Exibe a lista de restaurantes cadastrados.
def listar_restaurante():
    exibir_subtitulo('Lista de restaurantes')
    for restaurante in restaurantes:  # Itera sobre a lista de restaurantes
        print(f'. {restaurante}')  # Exibe cada restaurante
    voltar_ao_menu()

#Executa a função correspondente à opção escolhida.
def escolher_opcao():
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
    exibir_subtitulo('Programa Finalizado!')

def exibir_subtitulo(mensagem):
    os.system('cls') # Limpa a tela
    print(mensagem)
    print()

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