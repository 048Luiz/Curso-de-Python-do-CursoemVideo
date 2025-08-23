#(int) serve para converter para números inteiros.
#(float) serve para converter para números reais.

number1 = int(input('Digite um número:'))
number2 = int(input('Digite outro número:'))
addition = number1 + number2

#Formato de print antigo: 
#print('A soma entre',number1,'e',number2,'vale:',addition) 

#Formato de print moderno usando .format:
print('A soma entre {} e {}, vale: {}'.format(number1,number2,addition))