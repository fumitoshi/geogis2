from django.contrib.gis.db import models


# Create your models here.


class Pref(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=10)

    def __str__(self):
        return self.name

class City(models.Model):
    code=models.CharField(max_length=10)
    prefecture=models.ForeignKey(Pref,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Zipcode(models.Model):
    code=models.CharField(max_length=100)
    city=models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Evacuation(models.Model):
   evacuation_site = models.CharField(max_length=255)
   zipcode=models.ForeignKey(Zipcode,on_delete=models.CASCADE,null=True,blank=True,related_name="evacuation_zipcode")
   location = models.CharField(max_length=255)
   flood = models.CharField(max_length=255)
   landslides = models.CharField(max_length=255)
   storm_surge = models.CharField(max_length=255)
   earthquake = models.CharField(max_length=255)
   tsunami = models.CharField(max_length=255)
   massive_fire = models.CharField(max_length=255)
   inland_flooding = models.CharField(max_length=255)
   volcanic_phenomena = models.CharField(max_length=255)
   geom = models.PointField(srid=4326)

   def __str__(self):
       return self.evacuation_site


class Post(models.Model):
    evacuation_pk=models.ForeignKey(Evacuation,on_delete=models.CASCADE,null=True,blank=True)
    memo=models.TextField()

    def __str__(self):
        return self.memo