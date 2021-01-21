nome = input('Digite o seu nome completo: ')
print('Seu nome é: {}'.format(nome))
listnome = nome.split()

print('O seu primeiro nome é: {}'.format(listnome[0]))
#print('O seu ultimo nome é: {}'.format(nome[nome.rfind(' '):]))
listnome.reverse()
print('O seu ultimo nome é: {}'.format(listnome[0]))
