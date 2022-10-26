"""

Enunciado: Imagina-se que você está desenvolvendo um software de controle de estoque para uma mercearia. Este software deve ter o seguinte menu e opções:
1.	Cadastrar Produto
2.	Consultar Produto(s)
1)	Consultar Todas as Produto
2)	Consultar Produto por Código
3)	Consultar Produto(s) por Fabricante
4)	Retornar
3.	Remover Produto
4.	Sair
Elabore um programa em Python que:
1.	Deve-se codificar uma função cadastrarProduto (código) (EXIGÊNCIA 1);
o	Essa função recebe como parâmetro um código exclusivo para cada produto cadastrado (DICA: utilize um contador como parâmetro)
o	Dentro da função perguntar o nome do produto;
o	Dentro da função perguntar o fabricante do produto;
o	Dentro da função perguntar o valor do produto
o	Cada produto cadastrado deve ter os seus dados armazenados num DICIONÁRIO (DICA: Conferir material escrito da p. 22 até p24  da AULA 06)
2.	Deve-se codificar uma função consultarProduto(EXIGÊNCIA 2);
o	Dentro da função ter um menu com as seguintes opções:
	Consultar Todos os Produtos
	Consultar Produtos por Código
	Consultar Produtos por Fabricante
	Retornar
3.	Deve-se codificar uma função chamada removerProduto (EXIGÊNCIA 3);
o	Dentro da função perguntar qual o código do produto que se deseja remover do cadastro (da lista de dicionário)

"""

print('Mercearia Matheus Victor Avelino 4119107')
cadastro4119107 = {}
cadastroLista = []
codProduto = 0

def validaInt(pergunta,min,max):

    """

    :param pergunta: Pergunta que ira aparecer para o usuário.
    :param min: menor valor que a função ira receber.
    :param max: maior valor que a função ira receber.
    :return:

    """

    x = int(input(pergunta))

    while ((x < min) or (x > max)): # Se o menor valor for menor que valor minimo ou se o maior valor for maior que valor maximo.

        x = int(input(pergunta)) # Repete a pergunta até o usuário digitar um valor valido.

    return x # Retorna a pergunta.

def cadastrarProduto(codigo):

    # Função para cadastrar um produto.

    print('Codigo Produto: {}{}'.format('00',codigo)) # Mostar o codigo do produto.
    cadastro4119107['codigo'] = codigo # Inseri o codigo do produto na lista.
    cadastro4119107['produto'] = input('Digite O Nome Do Produto: ').upper() # Inseri o produto na lista e converte os caracteres para maiusculos.
    cadastro4119107['fabricante'] = input('Digite O Fabricante Do Produto: ').upper() # Inseri o fabricante na lista e converte os caracteres para maiusculos.
    cadastro4119107['preco'] = float(input('Digite O Preço Do Produto: ').replace(',','.')) # Inseri o preco na lista e substitui a virgula por ponto.

    cadastroLista.append(cadastro4119107.copy()) # copia a lista de produtos para tupla cadastro4119107.

def consultarProduto():

    # Função para consultar todos produtos, consultar por codigo e por fabricante.

    while True:

        print('', 12 * '_ ', 'Consultar Produto', 12 * ' _')
        print('|                                                                    |')
        print('|        1 - Consultar Todos Os Produtos                             |')
        print('|        2 - Consultar Produto Por Código                            |')
        print('|        3 - Consultar Por Fabricante                                |')
        print('|        4 - Retornar                                                |')
        print(12 * '_ ', 'Consultar Produto', 12 * ' _')

        print() # Quebra de linha.
        opConsulta = validaInt('Escolha A Opção Desejada: ',1,4)
        print() # Quebra de linha.

        if (opConsulta == 1):

            print('Você Escolheu Consultar Todos Os Produtos')

            for cadastro4119107 in cadastroLista:

                print() # Quebra de linha.

                for key,value in cadastro4119107.items():

                    print('{}:{} '.format(key,value)) # Exibe o produto.

            continue

        elif (opConsulta == 2):

            print('Você Escolheu Consultar Os Produtos Por Codigo')

            entradaCodigo = int(input('Digite O Código Do Produto: '))

            for cadastro4119107 in cadastroLista:

                if (cadastro4119107['codigo'] == entradaCodigo):

                    for key, value in cadastro4119107.items():

                        print('{}:{} '.format(key,value)) # Exibe o produto.

        elif (opConsulta == 3):

            print('Você Escolheu Consultar Os Produtos Por Fabricante')

            entradaFabricante = input('Digite O Fabricante Do Produto: ').upper()

            for cadastro4119107 in cadastroLista:

                print() # Quebra de linha.

                if(cadastro4119107['fabricante'] == entradaFabricante): # Se o fabricante do procuto é igual ao fabricante digitado pelo usuário.

                    for key,value in cadastro4119107.items():

                        print('{}:{}'.format(key,value)) # Exibe o produto.

        elif (opConsulta == 4) : # Encerra o programa.

            break # Interrompe o while.

def removerProduto():

    # Função para remover o produto por codigo.

    print('Você Escolheu Remover Produtos')
    entradaRemover = int(input('Digite O Código Do Produto Desejado: ')) # Recebe o valor do codigo a ser removido.

    for cadastro4119107 in cadastroLista:

        if (cadastro4119107['codigo'] == entradaRemover): # Se o codigo do procuto é igual ao codigo digitado pelo usuário.

            cadastroLista.remove(cadastro4119107) # Remove o produto.


# Programa principal.


while True:

    print(' _________________________________________________________________') # Exibe um menu com as opções.
    print('|                                                                |')
    print('|        1 - Cadastrar Produto                                   |')
    print('|        2 - Consultar Produto(s)                                |')
    print('|        3 - Remover Produto                                     |')
    print('|        4 - Sair                                                |')
    print('|________________________________________________________________|')
    print() # Quebra de linha.
    opCadastro = validaInt('Digite A Opção Desejada: ', 1, 4) # Recebe o valor digitado e verifica se o valor esta entre 1 e 4.
    print() # Quebra de linha.

    if (opCadastro == 1): # Se caso o usuário escolheu cadastrar um produto.

        codProduto += 1 # Adiciona + 1 ao codigo para cada produto cadastrado.
        cadastrarProduto(codProduto) # Chama a função cadastrar produto.
        continue # Continua o while.

    elif (opCadastro == 2): # Se caso o usuário escolheu consultar um produto.

        consultarProduto() # Chama a função consultar produto.

    elif (opCadastro == 3): # Se caso o usuário escolheu deletar um produto.

        removerProduto() # Chama a função remover produto.

    else: # Se caso o usuário escolheu sair.

        print('Encerrando O Programa.....')
        break # Interrompe o while.
