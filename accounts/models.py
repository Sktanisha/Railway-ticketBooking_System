from django.db import models
from django.db.models.fields import EmailField

# Create your models here.
class accounts(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    username = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20)
    confpassword = models.CharField(max_length = 20)
    email=models.EmailField(max_length=30)
    contact = models.IntegerField(max_length=11)
    
class train(models.Model):
    train_name= models.CharField(max_length=20)
    seats=models.IntegerField()
    fare=models.IntegerField()
    

class route(models.Model):
    source=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    train_name=models.CharField(max_length=20)
    arrivetime=models.TimeField()
    doj = models.DateField()


class reservation(models.Model):
    person_email=models.CharField(max_length=20)
    train_name=models.CharField(max_length=20)
    nofperson = models.IntegerField()
    doj = models.DateField()

class purchase(models.Model):
    train_name=models.CharField(max_length=20)
    purchaser_name=models.CharField(max_length=20)
    purchaser_email=models.CharField(max_length=20)
    purchaser_contact = models.IntegerField(max_length=11)
    source=models.CharField(max_length=20)
    destination=models.CharField(max_length=20)
    seats=models.IntegerField()
    availableseats=models.IntegerField()
    arrivetime=models.TimeField()
    nofperson = models.IntegerField()
    doj = models.DateField()
    totalfare=models.IntegerField()

class msgs(models.Model):
    person_name = models.CharField(max_length=20)
    person_email = models.CharField(max_length=20)
    person_contact = models.IntegerField(max_length=11)
    msg = models.CharField(max_length=1000)

class Profile(models.Model):
    user = models.OneToOneField(accounts, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'profile_tokens'

    def __str__(self):
        return self.user.email


