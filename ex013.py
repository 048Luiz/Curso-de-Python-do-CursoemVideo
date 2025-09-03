import requests

response = requests.get('https://economia.awesomeapi.com.br/json/last/USD-BRL')
data = response.json()
exchange_rate = float(data['USDBRL']['bid'])

numberMoney = input('Digite o quanto você deseja converter para dólar: ')
numberMoney = numberMoney.replace('.', '').replace(',', '.')
numberMoney = float(numberMoney)
calculation = numberMoney / exchange_rate
print(f'O valor em dólares é: {calculation:,.2f}')