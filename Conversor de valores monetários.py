import requests
from bs4 import BeautifulSoup
import json

try:
    q = open("quote.json", "r")
    quotation = json.load(q)
    valorcotacaodolar = quotation["dolar"]
    valorcotacaoeuro = quotation["euro"]
    jsonExists = True
except IOError:
    jsonExists = False


msg = 'Conversor de valores monetários'
msg2 = 'Script feito por Filipe Miranda, os valores utilizados são do site: https://www.valor.com.br/valor-data'
msg3 = 'Utilize "." para casas decimais.'
if(jsonExists == True):
    msg4 = 'Cotação atual do dólar: {}'.format(valorcotacaodolar)
    msg5 = 'Cotação atual do euro: {}'.format(valorcotacaoeuro)
else:
    msg4 = 'Não há cotação do dólar armazenada localmente.'
    msg5 = 'Não há cotação do euro armazenada localmente.'
contmsg = 0
for caracter in msg2:
    if caracter in 'ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvxwyzã:/.-, ':
        contmsg = contmsg + 1

print('='*int(contmsg))
print(msg)
print(msg2)
print(msg3)
print(msg4)
print(msg5)
print('='*int(contmsg))

checkquote = "s"
checkok = False
while(checkok == False):
    if(jsonExists == True):
        checkquote = input("Você deseja atualizar o valor da cotação? [s/n] ")

    if(checkquote == "s"):
        try:
            r = requests.get('https://www.valor.com.br/valor-data') #requisição do site
            soup = BeautifulSoup(r.text, 'html.parser')

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
            msg4 = 'Cotação atual do dólar: {}'.format(valorcotacaodolar)
            msg5 = 'Cotação atual do euro: {}'.format(valorcotacaoeuro)
            print("Valores atualizados:")
            print(msg4)
            print(msg5)
            
        except:
            print("Não foi possível obter valores de cotação do site.")

        finally:
            checkok = True
            
    elif(checkquote == "n"):
        checkok = True
    else:
        print("Opção inválida")


saldo = float(input('Insira o valor em reais (R$): '))
print('Com R${:.2f} você pode comprar US${:.2f} dólares'.format(saldo, (saldo/float(valorcotacaodolar))))
print('Com R${:.2f} você pode comprar EUR€{:.2f} euros'.format(saldo, (saldo/float(valorcotacaoeuro))))
input('Tecle enter para sair ')