days = int(input('Qauntos dias o veículo foi alugado:'))
km = float(input('Quantos km ele rodou:'))
# R$: 60.00 o dia, e R$: 0.15 por km
calc1 = days * 60
calc2 = km * 0.15
calc3 = calc1 + calc2

print(f'Valor dos dias R$:{calc1:.2f}\nValor dos km rodados R$:{calc2:.2f}\nTotal dê R$: {calc3:.2f}')