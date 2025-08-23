#O valor retornado de um input será sempre do tipo STRING
number = input('Digite algo:')

#Para ver se o valor do input pode ser convertido para número com (int ou float).
print(number.isnumeric())

#Para ver se o valor é alfabético.
print(number.isalpha())

#Para ver se o valor é alfanúmerico (nnúmeros e alfabeto).
print(number.isalnum())
