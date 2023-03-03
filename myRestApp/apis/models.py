from django.db import models

# Create your models here.
# create restaurant models

class Restaurant(models.Model):
    Restaurant_id =models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)   
    Address= models.CharField(max_length=100)   
    vegOnly=models.BooleanField(default=False,choices=[(True,True),(False,False)])
    
    Cost=models.CharField(max_length=1000,choices=[('Low', 'Low'),('Medium','Medium'), ('High', 'High'),])             
    cuisineTypes=models.CharField(max_length=1000,choices=[('South Indian','South Indian'),('Korean','Korean'),('Italian','Italian'),('Japanese','Japanese'),('French','French'),('north indian','north indian'),('East indian','East indian')])
    createdAt= models.DateTimeField(auto_now_add=True)
    updatedAt= models.DateTimeField(auto_now_add=True)
    isOpen= models.BooleanField(default=True,choices=[(True,True),(False,False)])      