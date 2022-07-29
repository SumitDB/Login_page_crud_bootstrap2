from django.db import models

# Create your models here.
class User(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField()
    Mobile_no=models.IntegerField()
    Password=models.CharField(max_length=10)

class Customer(models.Model):
    name=models.CharField(max_length=70)
    email=models.EmailField(max_length=100)
    city=models.CharField(max_length=10)



class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length = 100)
    email=models.EmailField()
    city = models.CharField(max_length=15)

    def __str__(self):
        return '%s' % (self.name)
    
    class Meta:
        db_table="employee"
        