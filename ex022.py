import random
student1 = input('Nome do primeiro aluno:')
student2 = input('Nome do segundo aluno:')
student3 = input('Nome do terceiro aluno:')
student4 = input('Nome do quarto aluno:')
list = [student1, student2, student3, student4]
sort = random.choice(list)
print(f'O aluno sorteado foi: {sort}!')
