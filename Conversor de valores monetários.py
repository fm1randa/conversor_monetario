import requests
from bs4 import BeautifulSoup
import json


r = requests.get('https://www.valor.com.br/valor-data') #requisição do site
soup = BeautifulSoup(r.text, 'html.parser')

checkok = False
while(checkok == False):
    checkquote = input("Você deseja atualizar o valor da cotação? [s/n] ")

    if(checkquote == "s"):
        '''Dólar'''
        cotacaodolar = soup.find_all(class_='data-cotacao__ticker_quote')[0]
        valorcotacaodolar = float((cotacaodolar.text).replace(',', '.'))

        '''Euro'''
        cotacaoeuro = soup.find_all(class_='data-cotacao__ticker_quote')[3]
        valorcotacaoeuro = float((cotacaoeuro.text).replace(',', '.'))

        quotation = {
            "dolar": valorcotacaodolar,
            "euro": valorcotacaoeuro
        }

        q = open("quote.json", "w")
        json.dump(quotation, q)

        checkok = True 
    elif(checkquote == "n"):
        checkok = True
    else:
        print("Opção inválida")

msg = 'Conversor de valores monetários'
msg2 = 'Script feito por Filipe Miranda, os valores utilizados são do site: https://www.valor.com.br/valor-data'
msg3 = 'Utilize "." para casas decimais.'
contmsg = 0
for caracter in msg2:
    if caracter in 'ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvxwyzã:/.-, ':
        contmsg = contmsg + 1

print('='*int(contmsg))
print(msg)
print(msg2)
print(msg3)
print('='*int(contmsg))
print('Cotação atual do dólar: {}'.format(valorcotacaodolar))
print('Cotação atual do euro: {}'.format(valorcotacaoeuro))
saldo = float(input('Insira o valor em reais (R$): '))
print('Com R${:.2f} você pode comprar US${:.2f} dólares'.format(saldo, (saldo/float(valorcotacaodolar))))
print('Com R${:.2f} você pode comprar EUR€{:.2f} euros'.format(saldo, (saldo/float(valorcotacaoeuro))))
input('Tecle enter para sair ')