import pandas as pd
from .models import *

df_city=pd.read_excel('world/data/city.xlsx')  #city
df_pref=pd.read_excel('world/data/Prefecture.xlsx') #prefecture

for i,row in df_pref.iterrows():
    pref=Pref()
    pref.id=row['id']
    pref.name=row['name']
    pref.save()
