import pandas as pd
import numpy as np
import openpyxl
import warnings 

warnings.simplefilter('ignore')

# upload csv
historico_casos_mundo = 'historic.csv'
casos_totais_br = 'brasil.csv'

df_hist_mundo = pd.read_csv(historico_casos_mundo,sep=';')
df_total_br = pd.read_csv(casos_totais_br,sep=';')
print(df_total_br)
