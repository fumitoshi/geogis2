from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# class PrefAdmin(ImportMixin,admin.ModelAdmin):
#     class PrefResource(resources.ModelResource):
#         class Meta:
#             model=Pref
#             fields=("id","name",)
#     resource_class=PrefResource

admin.site.register(Evacuation)
admin.site.register(Pref)
admin.site.register(City)
admin.site.register(Zipcode)
admin.site.register(Post)
# admin.site.register(Fumi)


# class CityResource(resources.ModelResource):
#     class Meta:
#         model=City

# @admin.register(City)
# class CityAdmin(ImportExportModelAdmin):
#     list_display=('code','prefecture','city')
#     resource_class=CityResource