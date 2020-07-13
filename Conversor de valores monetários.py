import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

try:
    q = open("quote.json", "r")
    quotation = json.load(q)
    valorcotacaodolar = quotation["dolar"]
    valorcotacaoeuro = quotation["euro"]
    dthratualtxt = quotation["hora"]
    jsonExists = True
except:
    print("Erro ao encontrar dados locais.")
    jsonExists = False


msg = 'Conversor de valores monetários'
msg2 = 'Script feito por Filipe Miranda, os valores utilizados são do site: https://www.valor.com.br/valor-data'
msg1 = 'GitHub: @fm1randa | Twitter: @k1ra_exe'
msg3 = 'Utilize "." para casas decimais.'
if(jsonExists == True):
    msg4 = 'Cotação atual do dólar: {}'.format(valorcotacaodolar)
    msg5 = 'Cotação atual do euro: {}'.format(valorcotacaoeuro)
    msg6 = 'Última atualização: {}'.format(dthratualtxt)
else:
    msg4 = 'Não há cotação do dólar armazenada localmente.'
    msg5 = 'Não há cotação do euro armazenada localmente.'
    msg6 = 'Nenhuma atualização encontrada.'
contmsg = 0

for caracter in msg2:
    if caracter in 'ABCDEFGHIJKLMNOPQRSTUVXWYZabcdefghijklmnopqrstuvxwyzã:/.-, ':
        contmsg = contmsg + 1

print('='*int(contmsg))
print(msg)
print(msg2)
print(msg1 + "\n")
print(msg3)
print(msg4)
print(msg5)
print(msg6)
print('='*int(contmsg))

checkquote = "s"
checkok = False
while(checkok == False):
    if(jsonExists == True):
        checkquote = input("\nVocê deseja atualizar o valor da cotação? [s/n]: ")

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

            dthratual = datetime.now()
            dthratualtxt = dthratual.strftime('%d/%m/%Y às %H:%M')

            quotation = {
                "dolar": valorcotacaodolar,
                "euro": valorcotacaoeuro,
                "hora": dthratualtxt
            }

            q = open("quote.json", "w")
            json.dump(quotation, q)
            msg4 = 'Cotação atual do dólar: {}'.format(valorcotacaodolar)
            msg5 = 'Cotação atual do euro: {}'.format(valorcotacaoeuro)
            print("\nValores atualizados:")
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


saldo = float(input('\nInsira o valor em reais (R$): '))
print('\nCom R${:.2f} você pode comprar:'.format(saldo)) 
print('US${:.2f} dólares'.format(saldo/float(valorcotacaodolar)))
print('EUR€{:.2f} euros'.format(saldo/float(valorcotacaoeuro)))
input('Tecle enter para sair ')