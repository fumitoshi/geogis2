import pandas as pd
from .models import *

df_city=pd.read_excel('world/data/city.xlsx')  #city
df_pref=pd.read_excel('world/data/Prefecture.xlsx') #prefecture

for i,row in df_city.iterrows():
    city=City()
    city.code=row[0]
    city.prefecture=Pref.objects.get(name=row[1])
    city.name=row[2]
    city.save()

