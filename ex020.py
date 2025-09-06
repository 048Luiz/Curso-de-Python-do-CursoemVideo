import math
cateto = abs(float(input('Digite o valor do cateto oposto:')))
cateto2 = abs(float(input('Digite o valor do cateto adjacente:')))
hipotenusa = math.hypot(cateto, cateto2)
print(f'O valor da hipotenusa é: {hipotenusa:.2f}')