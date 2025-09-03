number1 = int(input('Digite um número:'))
number2 = int(input('Digite outro número:'))
calc1 = number1 + number2
calc2 = number1 * number2
calc4 = number1 - number2

print(f'A soma dos números {number1} e {number2}, é: {calc1}')
print(f'A subtração dos números {number1} e {number2}, é: {calc4}')
print(f'A multiplicação dos números {number1} e {number2}, é: {calc2}')

if number2 != 0: 
    calc3 = number1 / number2
    print(f'A divisão dos números {number1} e {number2}, é: {calc3:.2f}')
else:
    print('Não é possível dividir por zero!')