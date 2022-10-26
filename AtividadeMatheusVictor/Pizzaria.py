"""

Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma pizzaria.
Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
A Pizzaria possui seguinte tabela de sabores de pizzas listados com sua descrição, códigos e valores:

Código  -	Descrição     -	 Pizza Média - M  -	   Pizza Grande – G (30% mais cara)
21	    -    Napolitana	  -  R$ 20,00	      -    R$ 26,00
22	    -    Margherita	  -  R$ 20,00	      -    R$ 26,00
23	    -    Calabresa	  -  R$ 25,00	      -    R$ 32,50
24	    -    Toscana	  -  R$ 30,00	      -    R$ 39,00
25	    -    Portuguesa	  -  R$ 30,00	      -    R$ 39,00

Elabore um programa em Python que:
1.	Entre com o tamanho da pizza
2.	Entre com o código do produto desejado;
3.	Pergunte se o cliente quer pedir mais alguma coisa (se sim repetir a partir do item 1.  Caso contrário ir para próximo passo);
4.	Encerre a conta do cliente com o valor total;
5.	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 3);
6.	Se a pessoa digitar um TAMANHO de pizza e/ou   NÚMERO diferente dos da tabela printar na tela: ‘opção inválida’ e voltar para o menu (EXIGÊNCIA 2 de 3);
7.	Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);
o	(DICA: utilizar o continue dentro else que verifica a opção inválida)
o	(DICA: utilizar o break dentro if que verifica a opção sair)

O código da linha 26 pega o valor do teclado e caso o usuario tenha digitado um caractere minusculo converte o para maiusculo.
O código da linha 30 até 33 verifica se o caractere recebido é diferente de M e G, se caso verdadeiro imprimi na tela a mensagem e volta ao inicio para o usuario digitar um caractere valido.
O código da linha 37 pega o código da pizza pelo teclado.
O código da linha 39 até 42 verifica se código recebido é menor que 20 e maior 26, se caso verdadeiro imprimi na tela a mensagem e volta ao inicio para o usuario digitar um caractere valido.
O código da linha 44 se caso o código for valido  passa para proxima parte.
O código da linha 46 até 84 verifica o valor do codigo, depois verifica o tamanho,exibe na tela a pizza selecionada e calcula o valor total da compra.
O código da linha 88 até 92  recebe se o usuario deseja sair ou não, casa sim encerra o programa.
O código da linha 94 e 95 exibe a mensagem de encerramento e mostra o total a pagar.


"""

totalPagar4119107 = 0  # Variavel responsavel em receber o valor total da compra.

print('Pizzaria Matheus Victor Avelino Silva 4119107')
print('_______________________Cardápio________________________')
print('| Código |   Descrição   | Pizza Média | Pizza Grande |')
print('|   21   |   Napolitana  |    20.00    |    26.00     |')
print('|   22   |   Margherita  |    20.00    |    26.00     |')
print('|   23   |   Calabresa   |    25.00    |    32.00     |')
print('|   24   |   Toscana     |    30.00    |    39.00     |')
print('|   25   |   Portuguêsa  |    30.00    |    39.00     |')
print('_______________________________________________________')
print()  # Salto de linha.

while True:

    tamPizza = input('Digite O Tamanho Da Pizza Que Deseja: M -> Para Media e G -> Para Grande: ').replace('g','G').replace('m', 'M')

    if (tamPizza != 'M' and tamPizza != 'G'):
        print('Digite Uma Opção Valida!!!!')
        continue  # Repete o laço.

    # ---------------------------------------------------------------------------------------------------------------------------------------------

    codProduto = int(input('Digite O Código Do Produto: '))

    if (codProduto <= 20 or codProduto >= 26):

        print('Digite Uma Opção Valida!!!!')
        continue  # Repete o laço.

    else:

        if (codProduto == 21 or codProduto == 22):

            if (tamPizza == 'M'):

                totalPagar4119107 += 20
                if (codProduto == 21):
                    print(
                        'Você Comprou Uma Pizza Média Sabor Napolitana')  # Verifica o código e exibe a pizza comprada.
                elif (codProduto == 22):
                    print(
                        'Você Comprou Uma Pizza Média Sabor Margherita')  # Verifica o código e exibe a pizza comprada.

            else:

                totalPagar4119107 += 26
                if (codProduto == 21):
                    print('Você Comprou Uma Pizza Grande Sabor Napolitana')
                elif (codProduto == 22):
                    print('Você Comprou Uma Pizza Grande Sabor Margherita')

        elif (codProduto == 23):

            if (tamPizza == 'M'):
                totalPagar4119107 += 25
                if (codProduto == 23): print('Você Comprou Uma Pizza Média Sabor Calabresa')

            else:

                totalPagar4119107 += 32
                if (codProduto == 23): print('Você Comprou Uma Pizza Grande Sabor Calabresa')

                elif (codProduto == 24 or codProduto == 25):

                    if (tamPizza == 'M'):

                        totalPagar4119107 += 30
                        if (codProduto == 24):
                            print('Você Comprou Uma Pizza Média Sabor Toscana')
                        elif (codProduto == 25):
                            print('Você Comprou Uma Pizza Média Sabor Portuguêsa')

                else:

                        totalPagar4119107 += 39

                        if (codProduto == 24):
                            print('Você Comprou Uma Pizza Grande Sabor Toscana')
                        elif (codProduto == 25):
                            print('Você Comprou Uma Pizza Grande Sabor Portuguêsa')

                # ---------------------------------------------------------------------------------------------------------------------------------------------

        op = input('Deseja Comprar Mais Uma Pizza? S -> Para Sim e N -> Não: ').replace('s', 'S').replace('n', 'N')

        if (op == 'N'):

            break  # interrompe o laço.

        elif (op == 'S'):

            continue  # continua o laço

        print('Encerrando A Conta....')
        print('Total A Pagar É: R${}'.format(totalPagar4119107))