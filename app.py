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

def cadastrar_restaurante():
    """
    Permite ao usuário cadastrar um novo restaurante.
    O nome e a categoria do restaurante são solicitados e adicionados à lista global 'restaurantes'.
    """
    exibir_subtitulo('Cadastro de Restaurante.')
    nome_restaurante = input('Digite o nome do restaurante: ').strip()  # Solicita o nome do restaurante
    if not nome_restaurante:  # Verifica se o nome está vazio
        print('Nome nao podem ser vazio!')
        return voltar_ao_menu()
    
    categoria_restaurante = str(input('Digite a categoria do restaurante: '))  # Solicita a categoria do restaurante
    if not categoria_restaurante:  # Verifica se a categoria está vazia
        print('Categoria nao podem ser vazio!')
        return voltar_ao_menu()
        
    for restaurante in restaurantes:  # Verifica se o restaurante já está cadastrado
        if restaurante['nome'].lower() == nome_restaurante.lower():
            print('Restaurante ja cadastrado')
            return voltar_ao_menu()
    
    # Gera um novo ID para o restaurante e adiciona à lista
    novo_id = restaurantes[-1]['id'] + 1 if restaurantes else 1
    restaurantes.append({'id': novo_id,  'nome': nome_restaurante, 'categoria': categoria_restaurante, 'status': False})
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!\n')
    voltar_ao_menu()

def alternar_status_restaurante():
    """
    Altera o status de um restaurante (ativado/desativado).
    Solicita o nome do restaurante e alterna o valor do campo 'status'.
    """
    exibir_subtitulo('Alternar Status Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar: ')  # Solicita o nome do restaurante
    print()
    restaurante_encontrado = False  # Flag para verificar se o restaurante foi encontrado
    
    for restaurante in restaurantes:  # Itera sobre a lista de restaurantes
        if nome_restaurante == restaurante['nome']:  # Verifica se o nome corresponde
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']  # Alterna o status
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            voltar_ao_menu()
    if not restaurante_encontrado:  # Caso o restaurante não seja encontrado
        print(f'O restaurante {nome_restaurante} nao foi encontrado')
        voltar_ao_menu()

def listar_restaurante():
    """
    Exibe a lista de restaurantes cadastrados.
    Mostra o ID, nome, categoria e status (Ativo/Desativado) de cada restaurante.
    """
    exibir_subtitulo(f'{"Lista de restaurantes":^58}')
    print('{:^8} {:^22} {:^22} {:^8}'.format('ID', 'NOME', 'CATEGORIA', 'STATUS'))
    print()
    for restaurante in restaurantes:  # Itera sobre a lista de restaurantes
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        id_restaurante = restaurante['id']
        status_restaurante =  'ATIVO' if restaurante['status'] == True else 'DESATIVADO'
        
        # Exibe os dados formatados
        print(f' {id_restaurante:>5}- | {nome_restaurante:<20} | {categoria_restaurante:<20} | {status_restaurante:^} ')
    voltar_ao_menu()

def escolher_opcao():
    """
    Solicita ao usuário que escolha uma opção do menu.
    Executa a função correspondente à opção escolhida.
    """
    opcao_escolhida = input('Escolha uma opção: ').strip()  # Solicita a entrada do usuário
    if not opcao_escolhida:  # Verifica se a entrada está vazia
        print('Por favor escolha uma das opcoes!')
        return escolher_opcao()
    
    opcao_escolhida = int(opcao_escolhida)  # Converte a entrada para inteiro
    try:
        if opcao_escolhida == 1:  # Opção para cadastrar restaurante
            cadastrar_restaurante()
        elif opcao_escolhida == 2:  # Opção para listar restaurantes
            listar_restaurante()
        elif opcao_escolhida == 3:  # Opção para ativar/desativar restaurante
            alternar_status_restaurante()
        elif opcao_escolhida == 4:  # Opção para finalizar o programa
            finalizar_programa()
        else:
            opcao_invalida()  # Opção inválida
            return
    except ValueError:  # Trata entradas inválidas (não numéricas)
        opcao_invalida()
        return escolher_opcao()

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