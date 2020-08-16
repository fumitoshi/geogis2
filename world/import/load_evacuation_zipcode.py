import pandas as pd
from .models import *

df_city=pd.read_excel('world/data/city.xlsx')
df_zipcode=pd.read_excel('world/data/zipcode.xlsx')

# for i,row in df_zipcode.iterrows():
#     evacuation=Evacuation()
for evacuation in Evacuation.objects.all():
    if '徳島市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7700835')
        evacuation.save()
    elif '鳴門市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7720000')
        evacuation.save()
    elif '小松島市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7730000')
        evacuation.save()
    elif '阿南市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7740000')
        evacuation.save()
    elif '吉野川市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7760000')
        evacuation.save()
    elif '阿波市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7711700')
        evacuation.save()
    elif '美馬市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7793600')
        evacuation.save()
    elif '三好市' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7780000')
        evacuation.save()
    elif '勝浦郡勝浦町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7714300')
        evacuation.save()
    elif '勝浦郡上勝町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7714500')
        evacuation.save()
    elif '名東郡佐那河内村' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7714100')
        evacuation.save()
    elif '名西郡石井町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7793200')
        evacuation.save()
    elif '名西郡神山町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7713200')
        evacuation.save()
    elif '那賀郡那賀町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7715200')
        evacuation.save()
    elif '海部郡牟岐町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7750000')
        evacuation.save()
    elif '海部郡美波町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7792300')
        evacuation.save()
    elif '海部郡海陽町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7750200')
        evacuation.save()
    elif '板野郡松茂町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7710219')
        evacuation.save()
    elif '板野郡北島町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7710204')
        evacuation.save()
    elif '板野郡藍住町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7711200')
        evacuation.save()
    elif '板野郡板野町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7790100')
        evacuation.save()
    elif '板野郡上板町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7711300')
        evacuation.save()
    elif '美馬郡つるぎ町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7794100')
        evacuation.save()
    elif '三好郡東みよし町' in evacuation.location:
        evacuation.zipcode=Zipcode.objects.get(code='7794700')
        evacuation.save()
        


