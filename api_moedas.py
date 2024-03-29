import requests
# import pandas as pd
# from datetime import datetime

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic["USDBRL"]["bid"]
cotacao_euro = requisicao_dic["EURBRL"]["bid"]
cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

print(f"Cotação Dólar: {cotacao_dolar}\n\
Cotação Euro: {cotacao_euro}\n\
Cotação BTC: {float(cotacao_btc) * 1000}")
