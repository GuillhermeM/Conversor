import requests
import pandas as pd 
from datetime import datetime
import time
import matplotlib.pyplot as plt

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
        
    def most(self):
        self.doli = float(self.cotacao_dolar)
        print('O dolar atual é',self.doli)

        cotacoes = [self.cotacao_dolar, self.cotacao_euro, self.cotacao_bitc, self.cotacao_yene, self.cotacao_dolartur]

        moedas = ['Dólar', 'Euro', 'Bitcoin', 'Iene', 'Dólar Turismo']
        plt.bar(moedas, cotacoes)
        plt.title('Cotações')
        plt.xlabel('Moedas')
        plt.ylabel('Cotações')
        plt.show()

aa = conversor_moeda()
aa.most()
