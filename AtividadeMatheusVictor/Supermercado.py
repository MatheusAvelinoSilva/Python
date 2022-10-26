
"""

Questão 1

Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado.
Uma das estratégias de vendas dessa empresa X é dar desconto maiores por unidade conforme a tabela abaixo:


Quantidades	   -   Desconto
Até 4	       -   0% na unidade
Entre 5 e 19   -   3% na unidade
Entre 20 e 99  -   6% na unidade
Mais que 100   -   10% na unidade


Elabore um programa em Python que:
1.	Entre com o valor unitário do produto (Lembrar que número decimal é feito com ponto e não vírgula);
2.	Entre com a quantidade desse produto;
3.	O programa deve retornar o valor total sem desconto;
4.	O programa deve retornar o valor total após o desconto;
5.	Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);

"""

print('Loja Matheus Victor Avelino Silva 4119107')

valorProduto = float(input('Digite O Valor do Produto: ').replace(',','.')) # Variavel responsável para receber o valor do produto
quantProduto4119107 = int(input('Digite A Quantidade De Produtos: ')) # Variavel responsável para receber a quantidade de produtos

valTotal = valorProduto * quantProduto4119107  # Variavel responsável para receber o valor total do produto

if (quantProduto4119107 <= 4):

    valDesconto = valTotal # Preço final sem desconto

elif (quantProduto4119107 >= 5 and quantProduto4119107 <= 19):

    valDesconto = valTotal * 0.97 # Preço final 3 % de desconto

elif (quantProduto4119107 >= 20 and quantProduto4119107 <= 99):

    valDesconto = valTotal * 0.94 # Preço final com 6 % de desconto

else:

    valDesconto = valTotal * 0.90 # Preço final com 10 % de desconto

print('O Valor Total Foi De: R${}'.format(valTotal)) # Exibe o valor total sem desconto
print('O Valor Total Com Desconto Foi De: R${}'.format(valDesconto)) # Exibe o valor total com desconto