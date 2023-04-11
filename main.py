import requests
import matplotlib.pyplot as plt
from alpha_vantage.foreignexchange import ForeignExchange
from datetime import datetime, timedelta
import pandas as pd

class conversor_moeda:
    def __init__(self):
        self.conversao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,JPY-BRL,USD-BRLT")
        #Pega as moedas disponíveis no site (Atualizado a cada 30 segundos) e armazena
        
        self.requisicao = self.conversao.json()
        
        self.cotacao_dolar = self.requisicao["USDBRL"]["bid"]
        self.cotacao_euro = self.requisicao["EURBRL"]["bid"]
        self.cotacao_bitc = self.requisicao["BTCBRL"]["bid"]
        self.cotacao_yene = self.requisicao["JPYBRL"]["bid"]
        self.cotacao_dolartur = self.requisicao["USDBRLT"]["bid"]
        #Armazena cada moeda em sua devida variavel
        
    def graff(self):
        # Defina a chave da API da Alpha Vantage
        self.api_key = 'SUA_CHAVE_API'

        # Defina o símbolo da moeda que você deseja obter os dados
        self.symbol = 'USDBRL'

        # Defina a data de um mês atrás e a data atual
        self.end_date = datetime.now().strftime('%Y-%m-%d')
        self.start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        # Obtenha os dados históricos da moeda usando a API da Alpha Vantage
        self.fx = ForeignExchange(key=self.api_key)
        self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='USD', to_symbol='BRL', outputsize='full')
        self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
        self.data = self.data.loc[self.start_date:self.end_date]

        # Calcule a taxa de variação diária da moeda
        self.daily_returns = self.data['4. close'].astype(float).pct_change()

        # Plote o gráfico da taxa de variação diária
        plt.plot(self.daily_returns.index, self.daily_returns)
        plt.title(f'Taxa de variação diária de {self.symbol} em um mês')
        plt.xlabel('Data')
        plt.ylabel('Taxa de variação diária')
        plt.show()       
        
        

aa = conversor_moeda()
aa.graff()
