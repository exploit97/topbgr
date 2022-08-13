
from distutils.command.upload import upload
from django.db import models
from PIL import Image
from memberships.models import UserMembership,Membership


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
   
    
    def __str__(self):
        return self.name

 





    
class Country(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Etablissement(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.DateField(blank=True,null=True)
    
    def __str__(self):
        return str(self.year.year)
   

class Evaluation(models.Model):
    name = models.CharField('Nom',max_length=100)
    image= models.ImageField(upload_to='image')
    description = models.TextField('Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank= True,null= True)
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, blank=True,null=True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height >100 or img.width>100:
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Level(models.Model):
    name = models.CharField(max_length=255)
    evaluation = models.ManyToManyField(Evaluation)
    def __str__(self):
        return self.name

class Es(models.Model):
    title = models.CharField(max_length=100)
    es_file = models.FileField(upload_to='solutions')
    es_image = models.ImageField(upload_to='solutions', blank=True,null=True)
    allowed_memberships = models.ManyToManyField(Membership)
    

    def __str__(self):
        return self.title

class Matter(models.Model):
    name = models.CharField(max_length=100)
    level = models.ManyToManyField(Level)
    
    
    def __str__(self):
        return self.name

class Subject(models.Model):
   
    title = models.CharField('Nom',max_length=100, default='Aucun')
    subject_pdf = models.FileField(upload_to='sujects', blank=True,null=True)
    subject_image = models.ImageField(upload_to='sujects', blank=True,null=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE,default=2014)
    matter = models.ForeignKey(Matter,on_delete=models.CASCADE,blank=True,null=True)
    evaluation = models.ForeignKey(Evaluation,on_delete=models.CASCADE,blank=True,null=True)
    level = models.ForeignKey(Level,on_delete=models.CASCADE,blank=True,null=True)
   
   
    es = models.ForeignKey(Es, on_delete=models.CASCADE, blank= True,null= True)
    
    
    def __str__(self):
        return self.title





