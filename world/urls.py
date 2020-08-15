from django.urls import path
from world import views
from django.conf.urls import include, url

app_name='world'

urlpatterns=[
    path('',views.index,name='index'),
    path('world/geojson/get_pref',views.serialize_pref),
    path('world/geojson/get_city/<int:pref_id>',views.serialize_city),
    path('world/geojson/<int:id>',views.serialize_facility_detail),
    path('world/geojson/form/<int:id>',views.serialize_form_detail),
    path('world/geojson/pref/<int:pref_id>',views.serialize_pref_evacuation),
    path('world/geojson/city/<int:city_id>',views.serialize_city_evacuation),
    path('world/form/<int:form_id>',views.formfunc,name='form'),
    path('detail/<int:pk>',views.detailfunc,name='detail'),
    
    # ------------------------------------------------------------------------
#     path('world/geojson/',views.index_serialized,name='geojson_view'),
#     path('world/geojson/<int:pk>/',views.return_facility_detail,name='aaa'),
#     url(r'^world/(?P<pk>\d+)$', views.return_facility_detail, name='detail_facility'),
#     path('world/city/<int:pref_id>/',views.return_city),
#     path('world/pref/<int:pref_id>',views.return_pref),
#     path('world/split/<int:pref_id>',views.return_evacuation),
#     path('world/pref/',views.return_pref2),
#     path('world/eva/<int:pref_id>',views.return_pref_eva),
 ]