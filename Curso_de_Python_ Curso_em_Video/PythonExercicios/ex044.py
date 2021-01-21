#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

valor = float(input('Valor do produto: R$ '))
print(''' Qual forma de pagamento?
[1] À vista dinheiro ou cheque:
[2] À vista no cartão:
[3] Em até 2x no cartão:
[4] 3x ou mais no cartão''')
opcao = int(input('Qual á a opção: '))

if opcao == 1:
    novo = valor - (valor * 10 / 100)
elif opcao == 2:
    novo = valor - (valor * 5 / 100)
elif opcao == 3:
    novo = valor
    parcela = valor / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} sem juros'.format(parcela))
elif opcao == 4:
    quantidadeParcela = int(input('Digite a quantidade de parcelas '))
    novo = valor + (valor * 20 / 100)
    parcela = novo / quantidadeParcela
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(quantidadeParcela, parcela))
else:
    print('Opção inválida!')

print('Sua compra de R$ {:.2f} vai custar {:.2f} no final'.format(valor, novo))