import pandas as pd
from .models import *

df_city=pd.read_excel('world/data/city.xlsx')
df_zipcode=pd.read_excel('world/data/zipcode.xlsx')

for i,row in df_zipcode.iterrows():
    zipcode=Zipcode()
    zipcode.code=row[0]
    zipcode.city=City.objects.get(name=row[1])
    zipcode.save()












