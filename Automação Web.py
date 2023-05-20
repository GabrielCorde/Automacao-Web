#!/usr/bin/env python
# coding: utf-8

# In[75]:


#!pip install selenium


# In[76]:


# baixar selenuim (!pip install selenium) para automatizar o navegador
# baixar o chromedrive no google e colocar na pasta onde o python esta.

# Passo a passo 

# Passo 1: Entrar na internet (abrir o navegador)

from selenium import webdriver

navegador = webdriver.Chrome()
navegador.get('https://www.google.com.br/')



# In[77]:


# Passo 2: Importar a base de dados
import pandas as pd

tabela = pd.read_excel('commodities.xlsx')
display(tabela)


# In[78]:


# navegador.send_kays('meu nome é lira') > escrever nele
    # ''       .click() > clicar nele
    # ''       .get_attribute() > pegar uma informação dele

for linha in tabela.index: 
    
    produto = tabela.loc[linha,'Produto'] 
    
    # entrar no site do melhor cambio:
    link = f"https://www.melhorcambio.com/{produto}-hoje"
    link = link.replace('ó', 'o'). replace('ã', "a").replace('é', 'e').replace('ú', 'u'). replace('í', 'i').replace('á', 'a').replace('ç','c')

    navegador.get(link)

    # pegar a cotação do milho

    cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    cotacao = cotacao.replace('.', '').replace(',', '.')
    cotacao = float(cotacao)
    print(link)
    print(cotacao)


    # na coluna preço atual, preencher a cotação de milho

    tabela.loc[linha,'Preço Atual'] = cotacao
    

# Passo 3: Para cada produto da nossa base



# In[79]:


# Passo 4:  Pegar o preço atual do produto
# Passo 5: Atualizar o preço na base de dados
# Passo 6: Decidir quais produtos a gente vai comprar
display(tabela)

tabela['Comprar'] = tabela['Preço Atual'] < tabela['Preço Ideal']
display(tabela)


# In[80]:


# Passo 7: Exportar a base de dados atualizada

navegador = quit() # fechar navegador

tabela.to_excel('commodities_atualizado.xlsx', index=False)

