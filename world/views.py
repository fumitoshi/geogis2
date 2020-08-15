from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import traceback
import json
from django.core.serializers import serialize
from .models import *
from .serializers import *
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from .forms import PostForm

# Create your views here.

#ホームページ表示
def index(request):
    return render(request,'world/index.html')

# 都道府県のjsonを返す
def serialize_pref(request):
    pref=Pref.objects.all()
    serialized=PrefSerializer(pref,many=True)
    content=JSONRenderer().render(serialized.data)
    return HttpResponse(content)

# 市区町村のjsonを返す
def serialize_city(request,pref_id):
    city=City.objects.filter(prefecture=pref_id)
    serialized=CitySerializer(city,many=True)
    content=JSONRenderer().render(serialized.data)
    return HttpResponse(content)

# 県レベルの避難所をフィルターして返す
def serialize_pref_evacuation(request,pref_id):
    pref=Pref.objects.get(id=pref_id)
    city=City.objects.filter(prefecture=pref)
    zipcode=Zipcode.objects.filter(city__in=city)
    evacuation=Evacuation.objects.filter(zipcode__in=zipcode)
    serialized=EvacuationSerializer(evacuation,many=True)
    content=JSONRenderer().render(serialized.data)
    return HttpResponse(content)

# 市レベルの避難所をフィルターして返す
def serialize_city_evacuation(request,city_id):
    city=City.objects.filter(id=city_id)
    zipcode=Zipcode.objects.filter(city__in=city)
    evacuation=Evacuation.objects.filter(zipcode__in=zipcode)
    serialized=EvacuationSerializer(evacuation,many=True)
    content=JSONRenderer().render(serialized.data)
    return HttpResponse(content)

# 施設情報を返す
def serialize_facility_detail(request,id):
    evacuation=Evacuation.objects.filter(pk=id)
    serialized=EvacuationDetailSerializer(evacuation,many=True)
    content=JSONRenderer().render(serialized.data)
    return HttpResponse(content)

def serialize_form_detail(request,id):
    posts=Post.objects.filter(evacuation_pk=id)
    serialized=FormSerializer(posts,many=True)
    content=JSONRenderer().render(serialized.data)
    return HttpResponse(content)



# formを返す
def formfunc(request,form_id):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
            return redirect('world:index')
    else:
        default_data={'evacuation_pk':Evacuation.objects.get(pk=form_id)}
        form=PostForm(default_data)
    return render(request,'world/form.html',{'form':form})

def listfunc(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def detailfunc(request,pk):
    post=Post.objects.get(pk=pk)
    return render(request,'detail.html',{'post':post})





def return_pref2(request):
    prefs=Pref.objects.all()
    serialized=PrefSerializer(prefs,many=True)
    content=JSONRenderer().render(serialized.data)
    return HttpResponse(content)


# class GeojsonAPIView(APIView):
#     def get(self,request,*args,**kwargs):
#         encjson=serialize('geojson',Evacuation.objects.filter(location__contains='徳島市'))
#         #print(type(encjson)) str
#         #encjson=serialize('geojson',Evacuation.objects.get(pk=2))
#         result=json.loads(encjson)
#         #print(type(result))dict
#         response=Response(result)
#         #print(response)
#         #print(type(response)) rest_framework.response.Response
#         return response


# def upload(request):
#     if 'csv' in request.FILES:
#         form_data=TextIOWrapper(request.FILES['csv'].file,encoding='shift_jis')
#         csv_file=csv.reader(form_data)
#         for line in csv_file:
#             pref,created=Pref.objects.get_or_create(code=line[0])
#             pref.code=line[0]
#             pref.name=line[1]
#             pref.save()
        
#         return render(request,'pref/upload.html')
    
#     else:
#         return render(request,'pref/upload.html')

# def return_city(request,pref_id):
#     cities=City.objects.filter(prefecture=pref_id)
#     # print(cities)
#     context={
#         'cities':cities
#     }
#     return render(request,'world/index.html',context)

# def return_pref_eva(request,pref_id):
#     pref_name=
#     evacuation=Evacuation.objects.filter()

# def index_serialized(request):
#     evacuation=Evacuation.objects.filter(location__contains='徳島市')
#     serialized=EvacuationSerializer(evacuation,many=True)
#     content=JSONRenderer().render(serialized.data)
#     return HttpResponse(content)


# def return_facility_detail(request,pk):
#     evacuation=Evacuation.objects.filter(pk=pk)
#     serialized=EvacuationDetailSerializer(evacuation,many=True)
#     content=JSONRenderer().render(serialized.data)
#     return HttpResponse(content)

# def return_evacuation(request,pref_id):
#     evacuation=Evacuation.objects.filter(pk=pref_id)
#     serialized=EvacuationDetailSerializer(evacuation,many=True)
#     content=JSONRenderer().render(serialized.data)
# #     return HttpResponse(content)

# def return_city(request,pref_id):
#     cities=City.objects.filter(prefecture=pref_id)
#     # print(cities.count())正常
#     serialized=CitySerializer(cities,many=True)
#     # print(serialized)
#     content=JSONRenderer().render(serialized.data)
#     return HttpResponse(content)