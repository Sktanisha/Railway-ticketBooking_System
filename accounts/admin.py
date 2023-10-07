from django.contrib import admin
from .models import accounts,train,route,reservation,purchase,msgs

# Register your models here.

@admin.register(accounts)
class accountsAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','username','email','contact')
    search_fields = ('username','email')

@admin.register(train)
class trainAdmin(admin.ModelAdmin):
    list_display = ('train_name','seats','fare')
    search_fields = ('train_name','seats','fare')

@admin.register(route)
class routeAdmin(admin.ModelAdmin):
    list_display = ('source','destination','train_name','arrivetime')
    search_fields = ('source','destination','train_name','arrivetime')

@admin.register(reservation)
class reservationAdmin(admin.ModelAdmin):
    list_display = ('person_email','train_name','nofperson','doj')
    search_fields = ('person_email','train_name')

@admin.register(purchase)
class purchaseAdmin(admin.ModelAdmin):
    list_display = ('train_name','purchaser_name','purchaser_email','source','destination','seats','availableseats','arrivetime','nofperson','doj','totalfare')
    search_fields = ('train_name','source','destination','seats','availableseats','arrivetime')

@admin.register(msgs)
class msgsAdmin(admin.ModelAdmin):
    list_display = ('person_name','person_email','person_contact','msg')
    search_fields = ('person_name','person_email','person_contact','msg')
