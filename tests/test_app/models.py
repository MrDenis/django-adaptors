from django.db import models

# Create your models here.
class MyModel(models.Model):
    nom = models.CharField(max_length=15)
    age = models.IntegerField()
    taille = models.FloatField()
    
class MyModel2(models.Model):
    other_pk = models.PositiveSmallIntegerField()
    
class MyModelWithForeign(models.Model):
    foreign = models.ForeignKey(MyModel)
    
class OtherForeign(models.Model):
    foreign = models.ForeignKey(MyModel)
    
class MultipleModel(models.Model):
    nom = models.CharField(max_length=100)
    note = models.IntegerField()
    
class ComposedKeyForeign(models.Model):
    key_1 = models.PositiveIntegerField()
    key_2 = models.PositiveIntegerField()

class ComposedKey(models.Model):
    composed_key_foreign = models.ForeignKey(ComposedKeyForeign)
    
class MyModelBis(models.Model):
    nom = models.CharField(max_length=15)
    age = models.IntegerField()
    taille = models.FloatField()
    poids = models.FloatField()

class MyModelTer(models.Model):
    nom = models.CharField(max_length=15)
    age = models.IntegerField()
    taille = models.FloatField()
    poids = models.FloatField()
    bool = models.BooleanField()

class MyDualModel(models.Model): 
    text_1 = models.CharField(max_length=10)
    text_2 = models.CharField(max_length=10)   


class FirstNameModel(models.Model):
    first_name = models.CharField(max_length=10)
    
class LastNameModel(models.Model):
    last_name = models.CharField(max_length=10)
    
class LastNameModelWithForeign(models.Model):
    foreign = models.ForeignKey(FirstNameModel)
    last_name = models.CharField(max_length=10)


class ZipCodeModel(models.Model):
    code = models.CharField(max_length=5, unique=True)

class CityModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

class PersonModelWithForeign(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    zip_code = models.ForeignKey(ZipCodeModel)
    city = models.ForeignKey(CityModel)



