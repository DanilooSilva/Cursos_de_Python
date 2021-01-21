#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo

vlr = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))

meses = anos * 12
prestacao  = vlr / meses

print('Para pegar uma casa de RS {:.2f} em {} anos a prestção será de R$ {:.2f}'.format(vlr, anos, prestacao))
if prestacao > salario * 30 / 100:
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')
