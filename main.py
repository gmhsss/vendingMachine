maquina = [[3.75, 2], [3.67, 5], [9.96, 1], [1.25, 100], [13.99, 2]] #definição de
valores e quantidades disponíveis
notas = [[200, 1], [100,1], [50, 3], [20, 5], [10, 10], [5, 5], [2, 10]] # matriz
com notas disponíveis
moedas = [[1, 15], [0.5, 10], [0.25, 10] ,[0.1, 50], [0.05, 25], [0.01, 5]] #lista
com moedas disponíveis
def calcular_notas_e_moedas(troco, notas, moedas): # Função para calcular o troco
troco_em_dinheiro = [] #lista para armazenar as notas e moedas de troco
total_notas = sum(nota[0] * nota[1] for nota in notas) # calcula o total de
valor em notas /
total_moedas = sum(moeda[0] * moeda[1] for moeda in moedas) # calcula o total
valor em moedas
#compra cancelada
if troco > total_notas + total_moedas:
print("Desculpe, não há troco disponível. Compra cancelada.")
maquina[escolha][1] += escolha_qtd
return []
# Calcular as notas do troco
for nota in notas:
qtd_dinheiro = min(int(troco // nota[0]), nota[1]) # Calcula a quantidade
de notas que serão utilizadas no troco, o MIN compara a quantidade de notas
necessárias, com a qtd disponível, utilizando sempre o mínimo possível (quando há)
if qtd_dinheiro > 0: #condicional caso possa ser utilizada uma nota do
sistema
troco_em_dinheiro.append((qtd_dinheiro, nota[0])) #adiciona na lista
troco em dinheiro, a qtd de notas e o valor da nota
troco -= qtd_dinheiro * nota[0] #subtrai do troco, o valor que se
atinge com a nota no loop
nota[1] -= qtd_dinheiro #remove da matriz, a quantidade de notas
necessárias para o troco
# Calcular as moedas do troco
for moeda in moedas:
qtd_dinheiro = min(int(troco // moeda[0]), moeda[1]) # Calcula a quantidade
de moedas que serão utilizadas no troco
if qtd_dinheiro > 0: #condicional caso possa ser utilizada uma moeda do
sistema
troco_em_dinheiro.append((qtd_dinheiro, moeda[0])) #adiciona na lista
troco em dinheiro, a qtd de moedas e o valor da moeda
troco -= qtd_dinheiro * moeda[0] #subtrai do troco, o valor que se
atinge com a nota no loop
moeda[1] -= qtd_dinheiro #remove da matriz, a quantidade de moedas
necessárias para o troco
return troco_em_dinheiro # quantidade de notas e moedas
contador = 1 #contador para loop de repetir solicitação
while contador >= 1: #condicional para repetir solicitação
# Solicitar a escolha do produto ao usuário
escolha = int(input(f'Lista de produtos:\n [0] --> Coca-Cola -->R$ 3.75 -->
DISPONÍVEIS: {maquina[0][1]}\n [1] --> Pepsi-->R$ 3.67 --> DISPONÍVEIS: {maquina[1]
[1]}\n [2] --> Monster-->R$ 9.96 --> DISPONÍVEIS: {maquina[2][1]}\n [3] --> Café --
>R$ 1.25 --> DISPONÍVEIS: {maquina[3][1]}\n [4] --> Red Bull-->R$ 13.99 -->
DISPONÍVEIS: {maquina[4][1]}\n Escolha o produto desejado: '))
if escolha > 4 or escolha < 0: # Verificar se a escolha do produto é válida
print('Este produto não existe. Produtos disponíveis são:\n')
print(f' [0] --> Coca-Cola -->R$ 3.75 --> DISPONÍVEIS: {maquina[0][1]}\n
[1] --> Pepsi-->R$ 3.67 --> DISPONÍVEIS: {maquina[1][1]}\n [2] --> Monster-->R$
9.96 --> DISPONÍVEIS: {maquina[2][1]}\n [3] --> Café -->R$ 1.25 --> DISPONÍVEIS:
{maquina[3][1]}\n [4] --> Red Bull-->R$ 13.99 --> DISPONÍVEIS: {maquina[4][1]}\n')
print('[ 1 ] SIM \n[ 2 ] NAO')
pedir = int(input('Gostaria de comprar novamente?\n '))
else: #caso a escolha seja válida
escolha_qtd = int(input('Informe a quantidade desejada: ')) # Solicitar a
quantidade desejada do produto
if escolha_qtd > maquina[escolha][1]: # Verificar se a quantidade desejada
está disponível na máquina
print('O produto não está disponível nesta quantidade.Tente com outra
quantidade!\n')
print('[ 1 ] SIM \n[ 2 ] NAO')
pedir = int(input('Gostaria de comprar novamente?\n '))
else: #caso a quantidade solcitada esteja disponível na máquina
valor_total = escolha_qtd * maquina[escolha][0] # Calcular o valor
total da compra
print(f'Valor total: R$ {valor_total}\n') #exibe o valor total da
comprado usuário
valor_pago = float(input("Realize o pagamento, insira o valor que
deseja pagar: R$ ")) # Solicitar o valor pago pelo usuário
if valor_pago >= valor_total: # Verificar se o valor pago é suficiente
troco = valor_pago - valor_total #definição de troco
print(f'Troco: R$ {troco:.2f}\n') #exibir valor de troco
# Calcular e exibir as notas e moedas do troco
troco_em_dinheiro = calcular_notas_e_moedas(troco, notas, moedas)
for qtd_dinheiro, dinheiro in troco_em_dinheiro: #Quantidade de
dinheiro, valor --> dentro da matriz troco
if dinheiro > 1: # caso o dinheiro seja nota
tipo = "nota(s)"
else: #caso o dinheiro seja moeda
tipo = "moeda(s)"
print(f'{qtd_dinheiro} {tipo} de R${dinheiro:.2f}') # Resposta
de quantidade de notas e valor
maquina[escolha][1] -= escolha_qtd #remove a quantidade do estoque
print('[ 1 ] SIM \n[ 2 ] NAO')
pedir = int(input('Gostaria de comprar novamente?\n '))
if pedir == 1:
contador +=1
elif pedir == 2:
contador = 0
else:
print('RESPOSTA INVÁLIDA')
contador = 0
else:
print("Valor de Pagamento abaixo do valor do produto. Compra
cancelada.\n")
print('[ 1 ] SIM \n[ 2 ] NAO')
pedir = int(input('Gostaria de efetuar outra compra?\n '))
