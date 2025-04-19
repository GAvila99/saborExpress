import os

# Lista global para armazenar os nomes dos restaurantes cadastrados
restaurantes = [
    {'id': 1, 'nome': 'LaChapa', 'categoria': 'Hamburgueria', 'status': False},
    {'id': 2, 'nome': 'LaFornalha', 'categoria': 'Pizzaria', 'status': True},
    {'id': 3, 'nome': 'LaMasia', 'categoria': 'Italiana', 'status': True}
]

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

def voltar_ao_menu():
    """
    Exibe uma mensagem para o usuário pressionar uma tecla e retorna ao menu principal.
    """
    input('\nPressione uma tecla para voltar ao menu principal')

def opcao_invalida():
    """
    Exibe uma mensagem de erro para opções inválidas e retorna ao menu principal.
    """
    print('Opcao Invalida!\n')
    input('Pressione ENTER para voltar ao menu principal')

#implementar auto incremetno no id
#terminar tratamento de excessao 
def cadastrar_restaurante():
    """
    Permite ao usuário cadastrar um novo restaurante.
    O nome do restaurante é adicionado à lista global 'restaurantes'.
    """
    exibir_subtitulo('Cadastro de Restaurante.')
    nome_restaurante = input('Digite o nome do restaurante: ').strip()  # Solicita o nome do restaurante
    categoria_restaurante = str(input('Digite a categoria do restaurante: '))
    
    if not nome_restaurante or not categoria_restaurante:
        print('Nome e Categoria nao podem ser vazio!')
        voltar_ao_menu()
        
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            print('Restaurante ja cadastrado')
            voltar_ao_menu()
    
    restaurantes.append({'nome': nome_restaurante, 'categoria': categoria_restaurante, 'status': False})
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu()

def alternar_status_restaurante():
    """
    Altera status do restaurante (ativado/desativado)
    """
    exibir_subtitulo('Alternar Status Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')
    print()
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            voltar_ao_menu()
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} nao foi encontrado')
        voltar_ao_menu()

def listar_restaurante():
    """
    Exibe a lista de restaurantes cadastrados.
    """
    exibir_subtitulo(f'{"Lista de restaurantes":^58}')
    print('{:^8} {:^22} {:^22} {:^8}'.format('ID', 'NOME', 'CATEGORIA', 'STATUS'))
    print()
    for restaurante in restaurantes:  # Itera sobre a lista de restaurantes
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = restaurante['status']
        id_restaurante = restaurante['id']
        print(f' {id_restaurante:>5}- | {nome_restaurante:<20} | {categoria_restaurante:<20} | {status_restaurante:^} ')  # Exibe cada restaurante
    voltar_ao_menu()

def escolher_opcao():
    """
    Solicita ao usuário que escolha uma opção do menu.
    Executa a função correspondente à opção escolhida.
    """
    opcao_escolhida = int(input('Escolha uma opção: ').strip())  # Solicita a entrada do usuário
    try:
        if opcao_escolhida == 1:  # Estrutura de correspondência para as opções            
            cadastrar_restaurante()  # Opção para cadastrar restaurante
        elif opcao_escolhida == 2:
            listar_restaurante()  # Opção para listar restaurantes
        elif opcao_escolhida == 3:
            alternar_status_restaurante()  # Opção para ativar restaurante
        elif opcao_escolhida == 4:
            finalizar_programa()  # Opção para finalizar o programa
        else:
            opcao_invalida()  # Opção inválida
    except ValueError:
        opcao_invalida()  # Trata entradas inválidas (não numéricas)

def finalizar_programa():
    """
    Finaliza o programa exibindo uma mensagem de encerramento.
    """
    exibir_subtitulo('Programa Finalizado!')
    exit()   

def exibir_subtitulo(mensagem):
    """
    Exibe um subtítulo formatado e limpa a tela.
    """
    os.system('cls')  # Limpa a tela
    print(f'{mensagem:^48}')
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
    while True:
        os.system('cls')  # Limpa a tela
        exibir_nome_programa()  # Exibe o banner do programa
        exibir_menu()  # Exibe o menu principal
        escolher_opcao()  # Solicita a escolha do usuário

if __name__ == '__main__':
    main()  # Inicia o programa