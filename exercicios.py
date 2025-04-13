def impar_ou_par():
    numero = int(input('Insira um numero: '))

    if numero % 2 != 1:
        print(f'O numero {numero} e par!')
    else:
        print(f'O numero {numero} e impar!')

def verificao_deIdade():
    idade = int(input('Digite sua idade: '))
    if idade >= 0 and idade <= 12:
        print('Criança')
    elif idade >= 13 and idade <= 18:
        print('Adolescente')
    elif idade > 1:
        print('Adulto')
    else:
        print('Insira um numero valido')

def autenticacao_senha():
    usuario = str(input('Login: '))
    senha = str(input('Senha: '))
    if usuario == 'shaolinmatadorDePorco' and senha == '123':
        print(f"""Acesso autorizado
Bem vindo {usuario}!""")
    else:
        print("""Acesso negado!
Verifique Login e Senha.""")

def localizacao_plano_cartesiano():
    x = float(input('Insira o valor de X: '))
    y = float(input('Insira o valor de Y: '))
    if x > 0 and y > 0:
        print('Primeiro Quandrante')
    elif x < 0 and y < 0:
        print('Terceiro Quadrante')
    elif x  < 0 and y > 0:
        print('Segundo Quadrante')
    elif x > 0 and y < 0:
        print('Quarto Quadrante')
    else:
        print('Está localizado no eixo')

def listas():
    numeros = 1,2,3,4,5,6,7,8,9,10
    nomes = 'gabriel', 'avila', 'ribeiro'
    data_nascimento = 1999
    print(numeros)
    print(nomes)
    print(data_nascimento)

    for numero % 2  1 in numeros:
        numero = numero + numero
        print(numero)

listas()

