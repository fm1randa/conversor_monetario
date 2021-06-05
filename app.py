from flask import Flask, request
import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


app = Flask("MoneyConvert")

@app.route('/')
def home():
  return {
    'title': 'Conversor de valores monetários',
    'disclaimer': 'Script feito por Filipe Miranda, os valores utilizados são do site: https://www.valor.com.br/valor-data',
    'github': 'fm1randa',
    'twitter': 'k1ra_exe',
    'usage': 'Utilize \'.\' para casas decimais. JSON: { currency: \'r\', value: 100 }'
  }

@app.route('/convert', methods=['POST'])
def convert():
    body = request.get_json()
    # try:
    #     q = open("quote.json", "r")
    #     quotation = json.load(q)
    #     valorcotacaodolar = quotation["dolar"]
    #     valorcotacaoeuro = quotation["euro"]
    #     dthratualtxt = quotation["hora"]
    # except:
    #     return {'error': "Erro ao encontrar dados locais."}, 502
    try:
        # requisição do site
        r = requests.get('https://www.valor.com.br/valor-data')
        soup = BeautifulSoup(r.text, 'html.parser')

        '''Dólar'''
        cotacaodolar = soup.find_all(
            class_='data-cotacao__ticker_quote')[0]
        valorcotacaodolar = float(
            (cotacaodolar.text).replace(',', '.'))

        '''Euro'''
        cotacaoeuro = soup.find_all(
            class_='data-cotacao__ticker_quote')[3]
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

    except:
        return {'error': "Não foi possível obter valores de cotação do site."}, 502
    saldo = 0
    moeda = ""
    try:
      moeda = body['currency']
    except:
      return {'error': 'Insira um moeda (currency null)'}, 400
    try:
      if (body['value']):
        saldo = float(body['value'])
      else:
        return {'error': 'Insira um valor (value null)'}, 400
    except:
      return {'error': 'Valor inválido, insira um número inteiro ou decimal.'}, 500
    if (type(saldo) == int or type(saldo) == float):
      if(moeda == 'r'):
          return {
            'eur': valorcotacaoeuro, 
            'usd': valorcotacaodolar, 
            'msg': 'Com R${:.2f} você pode comprar: US$ {:.2f} dólares e EUR€ {:.2f} euros'.format(saldo, saldo/float(valorcotacaodolar), saldo/float(valorcotacaoeuro))
            }
      elif(moeda == 'd'):
          return {
            'usd': valorcotacaodolar, 
            'msg': 'Com US${:.2f} você pode comprar: R$ {:.2f} reais'.format(saldo, saldo*float(valorcotacaodolar))
            }
      elif(moeda == 'e'):
          return {
            'eur': valorcotacaoeuro, 
            'msg': 'Com EUR€{:.2f} você pode comprar: R$ {:.2f} reais'.format(saldo, saldo*float(valorcotacaoeuro))
            }
      else: 
          return {
            'error': 'Moeda inválida. Uso: [Dólar: d, Euro: e, Real: r]'
            }, 400
    return {
      'error': 'Valor inválido, insira um inteiro ou decimal'
      }, 400

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
