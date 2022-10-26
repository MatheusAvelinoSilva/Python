"""

Enunciado: Imagina-se que você e sua equipe foram contratados por um restaurante que serve feijoada para desenvolver a solução de software.
Você ficou encarregado da parte de retirar pedido por parte do cliente.O valor que a empresa cobra por feijoada é dado pela seguinte equação:
total=(volume*opção)+adional(is)
Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:

volume (ml)	            -   valor (R$)
volume < 300	        -   Não é aceito
300  <= volume <= 5000  -   volume * 0.08
volume > 5000	        -   Não é aceito

peso(kg)	                                                                                  -      multiplicador
b - Básica (Feijão + paiol + costelinha) 	                                                  -      1.00
p - Premium (Feijão + paiol + costelinha + partes de porco)	                                  -      1.25
s - Suprema (Feijão + paiol + costelinha + partes do porco + charque + calabresa + bacon)     -	     1.50

Elabore um programa em Python que:
1.	Pergunte o volume (em ml).Se digitar um valor não numérico e/ou volume for menor/maior que o limite aceito repetir a pergunta;
2.	Pergunte a opção da feijoada. Se digitar uma opção não válida deve repetir a pergunta
3.	Pergunte o acompanhamento. Deve-se perguntar se o usuário quer mais um acompanhamento até digitar a opção 0
4.	Encerre o total a ser pago com base na equação desse enunciado;
5.	Deve-se codificar uma função volumeFeijoada (EXIGÊNCIA 1 de 3);
o	Deve-se perguntar dentro da função o volume da porção (em ml);
o	Deve-se ter um if/else ou if/elif ou if/else/elif para verificar se o usuário não digitou um volume fora da faixa com que o restaurante trabalha;
o	Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
o	Deve-se retornar o valor em (RS) conforme a Quadro 1
6.	Deve-se codificar uma função opcaoFeijoada (EXIGÊNCIA 2 de 3);
o	Deve-se perguntar dentro da função a opção desejada;
o	Deve-se ter um if/elif/else para verificar as opções possíveis ou não;
o	Deve-se retornar o multiplicador conforme o Quadro 2
7.	Deve-se codificar uma função acompanhamentoFeijoada (EXIGÊNCIA 3 de 3);
o	Deve-se perguntar dentro se deseja ou não mais algum acompanhamento
o	Deve-se ter um if/elif/else para verificar as opções possíveis ou não;
o	Deve-se retornar o multiplicador conforme o Quadro 3

"""

print('Venda Feijoada Matheus Victor Avelino 4119107')
print()


def menuAcompanhamentoFeijuada():

    # Menu para exibir o acompanhamento da feijoada.

    print()
    print('Acompanhamentos')
    print('0 - Encerrar Pedido         -> R$0.00')
    print('1 - 200g De Arroz           -> R$5.00')
    print('2 - 150g De Farofa Especial -> R$6.00')
    print('3 - 100g De Couve Cozida    -> R$7.00')
    print('4 - 1 Laranja Descascada    -> R$3.00')
    print()


def menuTipoFeijoada():
    # Menu para exibir o tipo da feijoada.

    print()
    print(
        '________________________________________________________________________________________________________________')
    print(
        '|'                            '                                   Tipo                                                       | Multiplicador |')
    print(
        '|                                                                                              |               |')
    print(
        '| B - Basica   (Feijão + Paiol + Costelinha)                                                   |    1.00       |')
    print(
        '| P - Primiium (Feijão + Paiol + Costelinha Partes Do Porco)                                   |    1.25       |')
    print(
        '| S - Suprema  (Feijão + Paiol + Costelinha + Partes Do Porco + Charque + Calabresa + Bacon)   |    1.50       |')
    print(
        '________________________________________________________________________________________________________________')
    print()


def volumeFeijoada():
    # Função para pegar o volume da feijoada e verificar se o usuario digitou um volume invalido, se caso verdadeiro repete a pergunta até receber um valor valido.

    while True:

        try:
            volFeijoada = int(input('Digite O Volume Da Feijoada Em Ml: '))

            if (volFeijoada < 300 or volFeijoada > 5000): # vefica se o volume é invalido.

                print('Digite Um Valor Entre 300 ml e 5000 ml')

            else:

                return volFeijoada * 0.08  # retorna o volume escolhido * 0.08


        except ValueError: # Tratamento de exceção.

            print('Digite Uma Valor Numerico') # Retorna uma mensagem se caso o usuario digitar um valor texto ao em vez de um valor inteiro.

#---------------------------------------------------------------------------------------------------------------

def opcaoFeijoada():

    # Função que recebe a opção da feijoada e retorna o multiplicador com base no opção escolhida.

    while True:

        menuTipoFeijoada() # chama o menu da feijoada.
        opcFeijoada = input('Digite A Opção da Feijoada: ').upper() # Recebe a opção da feijoada e transforma o caractere digitado em maiúsculo.

        if (opcFeijoada == 'B'): # Feijoada basica.

            return 1.00
            break # Interrompe o while.

        elif (opcFeijoada == 'P'): # Feijoada premium.

            return 1.25
            break # Interrompe o while.

        elif (opcFeijoada == 'S'): # Feijoada suprema.

            return 1.50

            break  # Interrompe o while.

        else:

            print('Digite Uma Opção Valida!')  # Retorna uma mensagem caso o usuario tenha digitado um valor inválido.
            continue  # Continua o while

    # ---------------------------------------------------------------------------------------------------------------

def acompanhamentoFeijoada():

    # Função para somar os valores dos acompanhamentos.

    soma = 0.00

    while True:

        menuAcompanhamentoFeijuada()  # Chama o menu do acompanhamento.
        acoFeijoada = int(input('Deseja Algum Acompanhamento? '))

        if (acoFeijoada == 0):

            break  # Interrompe o while.

        elif (acoFeijoada == 1):

            soma += 5.00  # adiciona + 5 a variável soma.
            continue  # Continua o while.

        elif (acoFeijoada == 2):

            soma += 6.00  # adiciona + 6 a variável soma.
            continue  # Continua o while.

        elif (acoFeijoada == 3):

            soma += 7.00  # adiciona + 7 a variável soma.
            continue  # Continua o while.

        elif (acoFeijoada == 4):

            soma += 3.00  # adiciona + 3 a variável soma.
            continue  # Continua o while.

        else:

            print('Digite Uma Opção Valida!!!')  # Retorna uma mensagem caso o usuario tenha digitado um valor inválido.
            continue  # Continua o while.

    return soma  # Retorna o valor da variável soma.



#---------------------------------------------------------------------------------

print()
volume = volumeFeijoada() # adiciona o valor recebido da função volume feijoada a variável volume.
opcao = opcaoFeijoada() # adiciona o valor recebido da função opção feijoada a variável opção.
acompanhamento = acompanhamentoFeijoada() # adiciona o valor recebido da função acompanhamento feijoada a variável acompanhamento.

totalPagar4119107 = volume * opcao + acompanhamento # Variável para calcular o total a pagar.

print('O Valor Do Volume da Feijuada É De: R${} \nO Multiplicador É {}\nE O Valor Do Acompanhamento É De: R${}\nO Valor Total A Pagar É De R${}'.format(volume,opcao,acompanhamento,totalPagar4119107)) # Mensagem para mostrar o total a pagar.

