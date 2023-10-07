from django import forms
from django.db.models import fields
from .models import accounts, purchase, reservation, route, train,msgs
from django.contrib.auth.models import User

class accountsForm(forms.ModelForm):
    class Meta:
        model = accounts
        fields = ['fname','lname','username','password','confpassword','email','contact']


class trainForm(forms.ModelForm):
    class Meta:
        model = train
        fields = ['train_name','seats','fare']

class routeForm(forms.ModelForm):
    class Meta:
        model = route
        fields = ['source','destination','train_name','arrivetime']

class reservationForm(forms.ModelForm):
    class Meta:
        model = reservation
        fields = ['person_email','train_name','nofperson','doj']

class purchaseForm(forms.ModelForm):
    class Meta:
        model = purchase
        fields = ['train_name','purchaser_name','purchaser_email','source','destination','seats','availableseats','arrivetime','nofperson','doj','totalfare']

class msgsForm(forms.ModelForm):
    class Meta:
        model = msgs
        fields = ['person_name','person_email','person_contact','msg']