# **conver$or_monetario**
Script desenvolvido por **Filipe**

Requisitos:
[requests](https://pypi.org/project/requests/) ,
[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## **API**
https://kconvert.herokuapp.com/

## **Uso da API**
### **/**
Home, informações

### **/convert**
Converte de:

• Real pra dólar e euro

• Euro pra real

• Dólar pra real

### Exemplo de request com JSON:
```json
{
  "currency": "r",
  "value": 100
}
```
### Resposta:
```json
{
  "eur": 6.1258,
  "msg": "Com R$100.00 você pode comprar: US$ 19.86 dólares e EUR€ 16.32 euros",
  "usd": 5.0341
}
```
