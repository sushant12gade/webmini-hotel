from django.db import models

# Create your models here.
class Feedback(models.Model):
   email = models.CharField(max_length=50,null=True)
   phone = models.CharField(max_length=50,null=True)
   name = models.CharField(max_length=50,null=True)
   place = models.CharField(max_length=50,null=True)
   date = models.DateField(null=True)

   def __str__(self):
            return self.name

class Book(models.Model):
   email2= models.CharField(max_length=50,null=True)
   phone2= models.CharField(max_length=50,null=True)
   name2= models.CharField(max_length=50,null=True)
   place2= models.CharField(max_length=50,null=True)
   come= models.CharField(max_length=50,null=True)
   end= models.CharField(max_length=50,null=True)
   days= models.CharField(max_length=50,null=True)
   select1= models.CharField(max_length=50,null=True)
   select2= models.CharField(max_length=50,null=True)
   cometime= models.CharField(max_length=50,null=True)
   endtime= models.CharField(max_length=50,null=True)

   def __str__(self):
           return self.email2