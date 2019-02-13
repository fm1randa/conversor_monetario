import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.valor.com.br/valor-data') #requisição do site

'''Dólar'''
soupdolar = BeautifulSoup(r.text, 'html.parser')
cotacaodolar = soupdolar.find(class_='number')
valorcotacaodolar = float((cotacaodolar.text).replace(',', '.'))


'''Euro'''
soupeuro = BeautifulSoup(r.text, 'html.parser')
cotacaoeuro = soupeuro.find(class_='item')
cotacaoeuro2 = soupeuro.find_all('span')[6]
valorcotacaoeuro = float((cotacaoeuro2.text).replace(',', '.'))

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