alphanum = input('Digite algo: ')

if alphanum.isnumeric():
    print('É um numerico Inteiro')
elif alphanum.isalpha():
    print('Faz parte do alfabeto')
elif alphanum.isalnum():
    print('É um alphanumerico')

