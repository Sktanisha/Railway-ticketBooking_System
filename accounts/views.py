import uuid
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from rail_booking.accounts.models import train

from rail_booking.helpers import send_forget_password_mail

# from rail_booking.accounts.models import route
from .forms import accountsForm, purchaseForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.models import Profile, accounts, route, purchase,reservation,msgs,train
from django.db import connection

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.
def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def contact_form(request):
    return render(request, 'contact_form.html')


def ratings(request):
    return render(request, 'ratings.html')


def newsfeed(request):
    return render(request, 'newsfeed.html')


def seatbook(request):
    return render(request, 'seatbook.html')


def ticket(request):
    return render(request, 'ticket.html')


def pur(request):
    return render(request, 'pur.html')

def discount(request):
    return render(request, 'discount.html')

def covidloss(request):
    return render(request, 'covidloss.html')

def news3(request):
    return render(request, 'news3.html')

def new4(request):
    return render(request, 'new4.html')

def about_us(request):
    return render(request, 'about_us.html')

# def adminpanel(request):
#     return render(request, 'adminpanel.html')

def adminpanel(request):
    try:
        user = accounts.objects.get(email=request.session['email'])

        if user.email == 'admin@admin.com':
            return render(request, 'adminpanel.html', {'user': user})
        else:
            messages.error(request, "Restricted! Only admin can access.")
            return redirect('home', {'user': user})
    except:
        messages.error(request, 'You need to login first')
        return redirect('login')

def accountslist(request):
    accountsl = accounts.objects.raw('SELECT * FROM accounts_accounts ')
    return render(request, 'accountslist.html', {'accountsl': accountsl, })


def trainslist(request):
    trainsl = train.objects.raw('SELECT * FROM accounts_train ')
    return render(request, 'trainslist.html', {'trainsl': trainsl, })

def routeslist(request):
    routesl = route.objects.raw('SELECT * FROM accounts_route ')
    return render(request, 'routeslist.html', {'routesl': routesl, })

def reservation_list(request):
    reservel = reservation.objects.raw('SELECT * FROM accounts_reservation ')
    return render(request, 'reservation_list.html', {'reservel': reservel, })

def purchaselists(request):
        purchasel = purchase.objects.raw('SELECT * FROM accounts_purchase ')
        return render(request, 'purchaselists.html', {'purchasel': purchasel, })
   

def viewprofile(request):
    user = accounts.objects.get(email=request.session['email'])
    acc = accounts.objects.raw( 'SELECT * FROM accounts_accounts WHERE email = %s', [user.email] )
    return render(request, 'viewprofile.html', {'acc': acc, 'user': user})
    
def editprofile(request):
    if request.method == 'POST':
        user = accounts.objects.get(email=request.session['email'])
        if request.POST.get('editFirstName') and request.POST.get('editLastName') and request.POST.get('editContact') and request.POST.get('editUsername'):

            user.fname = request.POST.get('editFirstName')
            user.lname = request.POST.get('editLastName')
            user.contact = request.POST.get('editContact')
            user.username = request.POST.get('editUsername')
            user.save()
            messages.success(
                request, "User details updated successfully...!")

            return redirect('editprofile')
    else:
        try:
            user = accounts.objects.get(email=request.session['email'])
            return render(request, 'editprofile.html', {'user': user})
        except:
            messages.error(request, 'You need to login first')
            return redirect('login')



def contact_form(request):
    if request.method == 'POST':
        # user = accounts.objects.get(email=request.session['email'])
        if request.POST.get('person_name') and request.POST.get('person_email') and request.POST.get('person_contact') and request.POST.get('msg'):
            user = msgs()
            user.person_name = request.POST.get('person_name')
            user.person_email = request.POST.get('person_email')
            user.person_contact = request.POST.get('person_contact')
            user.msg = request.POST.get('msg')
            user.save()
            messages.success(
                request, "User messages send successfully...!")

            return redirect('contact_form')
    else:
        return render(request, 'contact_form.html',)



# def login(request):
# 	if request.method == 'POST':
# 		email = request.POST.['email']
# 		password = request.POST.['password']

# 		user = auth.authenticate(email=email,password=password)

# 		if user is not None:
# 			auth.login(request,user)
# 			return redirect("/")
# 		else:
# 			messages.info(request,'invalid email or password')
# 			return redirect('login')


# 	return render(request, 'login.html')
def pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines = [
        "this is line 1",
        "this is line 2",
        "this is line 3",
    ]

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='ticket.pdf')

# rafe99

def login(request):
    context = {}
    if request.method == 'POST':
        try:
            userInfo = accounts.objects.get(email=request.POST.get('email'))
            if (request.POST.get('password') == (userInfo.password)):
                request.session['email'] = userInfo.email
                return redirect('home')
            else:
                messages.error(request, 'Password incorrect...!')
        except accounts.DoesNotExist as e:
            messages.error(request, 'No user found for this email....!')

    return render(request, 'login.html', context)


# def showtrains(request):
#     context = {}
#     if request.method == 'POST':
# 	    form = purchaseForm(request.POST or None)

#         if form.is_valid():
# 		    form.save()
#             return render(request,'ticket.html',context)
#     else:
#         return render(request, 'ticket.html', context)

# def bookticket(request):
# 	try:
# 		request.session['email']
# 	except KeyError:
# 		return redirect('login')
# 	else:
# 		return render(request,'bookticket.html')


# def bookticket(request):
#     try:
#         user = accounts.objects.get(email=request.session['email'])
#         if request.method == 'POST':
#             if request.POST.get('source') and request.POST.get('destination') and request.POST.get('doj') and request.POST.get('nofperson'):
#                 src = request.POST.get('source')
#                 dstn = request.POST.get('destination')
#                 dat = request.POST.get('doj')
#                 # per = request.POST.get('nofperson')
#                 cursor = connection.cursor()
#                 cursor.execute(
#                     'SELECT * FROM accounts_train att, accounts_route ar WHERE ar.train_name = att.train_name and (ar.source = %s  and ar.destination =  %s) and ar.doj =  %s ;',
#                     [src, dstn,dat])
#                 showtrainsinfo = cursor.fetchall()
#                 cursor.close()

#                 cursor = connection.cursor()
#                 cursor.execute(
#                     'SELECT train.seats-sum(pur.nofperson) FROM accounts_train train, accounts_purchase pur WHERE train.train_name = pur.train_name ')
#                 avl = cursor.fetchall()
#                 cursor.close()

#                 # cursor = connection.cursor()
#                 # cursor.execute(
#                 #     'SELECT availableseats FROM accounts_purchase pur,accounts_reservation res WHERE pur.train_name = res.train_name and res.person_email=%s',[user.email])
#                 # avail = cursor.fetchall()
#                 # cursor.close()

#                 fdata = reservation()
#                 fdata.person_email=user.email
#                 fdata.train_name= showtrainsinfo[0][1]
#                 fdata.nofperson= request.POST.get('nofperson')
#                 fdata.doj=request.POST.get('doj')
#                 fdata.save()

#                 print(showtrainsinfo)
#                 # redirect('../showtrains')
#                 return render(
#                     request,
#                     'showtrains.html',
#                     {
#                         'showtrainsinfo': showtrainsinfo,
#                         'user': user,
#                         'avl' : avl
#                     },
#                 )
#                 # return redirect('showtrains')
#                 # redirect('showtrains/')
#                 # return redirect('../showtrains', {
#                 #     'showtrainsinfo': showtrainsinfo,
#                 #     'user': user
#                 # })
#         else:
#             return render(request, 'bookticket.html', {'user': user})
#     except:
#         messages.error(request, 'Please log in first')
#         return redirect('login')
#     #return render(request, 'bookticket.html')



# def ticket_pur(request, token):
#     try:
#         user = accounts.objects.get(email=request.session['email'])
#         cursor = connection.cursor()
#         cursor.execute(
#             'SELECT * FROM accounts_train att, accounts_route ar WHERE ar.train_name = att.train_name and att.id=%s;',
#             [token])
#         ticket = cursor.fetchall()
#         cursor.close()

#                 # cursor = connection.cursor()
#                 # cursor.execute(
#                 #     'SELECT train.fare*%s FROM accounts_train train, accounts_purchase reserve  WHERE train.train_name = reserve.train_name ',[per])
#                 # avail = cursor.fetchall()
#                 # cursor.close()

#         cursor = connection.cursor()
#         cursor.execute(
#             'SELECT train.fare*reserve.nofperson FROM accounts_train train,accounts_reservation reserve WHERE train.train_name = reserve.train_name reserve.person_email=%s',[user.email])
#         avail = cursor.fetchall()
#         cursor.close()

#         cursor = connection.cursor()
#         cursor.execute(
#             'SELECT * FROM accounts_train train, accounts_reservation reserve  WHERE train.train_name = reserve.train_name and reserve.person_email=%s',[user.email])
#         huda = cursor.fetchall()
#         cursor.close()



#         datas = purchase()
#         datas.train_name = ticket[0][1]
#         datas.purchaser_name = user.fname + ' ' + user.lname    
#         datas.purchaser_email = user.email
#         datas.purchaser_contact = user.contact
#         datas.source = ticket[0][5]
#         datas.destination = ticket[0][6]
#         datas.seats = ticket[0][2]
#         datas.availableseats = ticket[0][2]
#         datas.arrivetime = ticket[0][8]
#         datas.totalfare = avail[0][1]
#         datas.nofperson = huda[0][7]
#         datas.doj = ticket[0][9]
#         datas.save()
#         # return render(request, 'pur.html', {'ticket': ticket, 'user': user})
#         messages.success(request, 'submitted')
#         return redirect('show_pur_ticket')
#     except:
#         messages.error(request, 'Please log in first')
#         return redirect('login')



def bookticket(request):
    try:
        user = accounts.objects.get(email=request.session['email'])
        if request.method == 'POST':
            if request.POST.get('source') and request.POST.get('destination') and request.POST.get('doj') and request.POST.get('nofperson'):
                src = request.POST.get('source')
                dstn = request.POST.get('destination')
                # dat = request.POST.get('doj')
                # per = request.POST.get('nofperson')
                cursor = connection.cursor()
                cursor.execute(
                    'SELECT * FROM accounts_train att, accounts_route ar WHERE ar.train_name = att.train_name and ar.source = %s  and ar.destination =  %s;',
                    [src, dstn])
                showtrainsinfo = cursor.fetchall()
                cursor.close()

                cursor = connection.cursor()
                cursor.execute(
                    'SELECT train.seats-sum(pur.nofperson) FROM accounts_train train, accounts_purchase pur WHERE train.train_name = pur.train_name ')
                avl = cursor.fetchall()
                cursor.close()

                # cursor = connection.cursor()
                # cursor.execute(
                #     'SELECT availableseats FROM accounts_purchase pur,accounts_reservation res WHERE pur.train_name = res.train_name and res.person_email=%s',[user.email])
                # avail = cursor.fetchall()
                # cursor.close()

                fdata = reservation()
                fdata.person_email=user.email
                fdata.train_name= showtrainsinfo[0][1]
                fdata.nofperson= request.POST.get('nofperson')
                fdata.doj=request.POST.get('doj')
                fdata.save()

                print(showtrainsinfo)
                # redirect('../showtrains')
                return render(
                    request,
                    'showtrains.html',
                    {
                        'showtrainsinfo': showtrainsinfo,
                        'user': user,
                        'avl' : avl
                    },
                )
                # return redirect('showtrains')
                # redirect('showtrains/')
                # return redirect('../showtrains', {
                #     'showtrainsinfo': showtrainsinfo,
                #     'user': user
                # })
        else:
            return render(request, 'bookticket.html', {'user': user})
    except:
        messages.error(request, 'Please log in first')
        return redirect('login')
    #return render(request, 'bookticket.html')


def ticket_pur(request, token):
    try:
        user = accounts.objects.get(email=request.session['email'])
        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM accounts_train att, accounts_route ar WHERE ar.train_name = att.train_name and att.id=%s;',
            [token])
        ticket = cursor.fetchall()
        cursor.close()

        cursor = connection.cursor()
        cursor.execute(
            'SELECT train.seats-reserve.nofperson,train.fare*reserve.nofperson FROM accounts_train train, accounts_reservation reserve  WHERE train.train_name = reserve.train_name ')
        avail = cursor.fetchall()
        cursor.close()

        cursor = connection.cursor()
        cursor.execute(
            'SELECT * FROM accounts_train train, accounts_reservation reserve  WHERE train.train_name = reserve.train_name and reserve.person_email=%s',[user.email])
        huda = cursor.fetchall()
        cursor.close()



        datas = purchase()
        datas.train_name = ticket[0][1]
        datas.purchaser_name = user.fname + ' ' + user.lname    
        datas.purchaser_email = user.email
        datas.purchaser_contact = user.contact
        datas.source = ticket[0][5]
        datas.destination = ticket[0][6]
        datas.seats = ticket[0][2]
        datas.availableseats = avail[0][0]
        datas.arrivetime = ticket[0][8]
        datas.totalfare = avail[0][1]
        datas.nofperson = huda[0][7]
        datas.doj = huda[0][8]
        datas.save()
        # return render(request, 'pur.html', {'ticket': ticket, 'user': user})
        messages.success(request, 'submitted')
        return redirect('show_pur_ticket')
    except:
        messages.error(request, 'Please log in first')
        return redirect('login')


def show_pur_ticket(request):
    # try:
        user = accounts.objects.get(email=request.session['email'])

        mytickets = purchase.objects.raw('SELECT * FROM accounts_purchase WHERE purchaser_email = %s', [user.email])
        return render(request, 'show_pur_ticket.html', {'mytickets': mytickets, 'user': user})
    # except:
    #     messages.error(request, 'Please log in first')
    #     return redirect('login')

def pdf_download(request,token):
    user = accounts.objects.get(email=request.session['email'])
    # try:
    tikk = purchase.objects.raw(
                'SELECT * FROM  accounts_purchase WHERE purchaser_email = %s and accounts_purchase.id = %s;', [user.email, token])
        # showUser = UserModel.objects.get(email=tikk.postPunlisherEmail)
        # pur_tikk = PostModel.objects.get(id=tikk.postId)
    print(tikk)
    template_path = 'pdf_download.html'
    context = {'user': user, 'tikk': tikk }
    response = HttpResponse(content_type='application/pdf')
        # response['Content-Disposition'] = 'attachment; filename="lost-and-found.pdf"' # for download
    response['Content-Disposition'] = 'filename="ticket.pdf"'
    template = get_template(template_path)
    html = template.render(context)
        # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
        # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    # except:
    #     messages.error(request, 'You have no pdf to show.')
    #     return redirect('home')


def changepassword(request):
    return render(request, 'changepassword.html')

def signup(request):
    context = {}
    if request.method == 'POST':
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('username') and request.POST.get('password') and request.POST.get('email') and request.POST.get('contact'):
            saveRecord = accounts()
            saveToken = Profile()

            saveRecord.fname = request.POST.get('fname')
            saveRecord.lname = request.POST.get('lname')
            saveRecord.username = request.POST.get('username')
            saveRecord.password = request.POST.get('password')
            saveRecord.email = request.POST.get('email')
            saveRecord.contact = request.POST.get('contact')

            saveRecord.save()
            saveToken.user = saveRecord
            saveToken.save()
            return HttpResponse("added successfully !!")

    else:
        return render(request, 'signup.html', context)

def logout(request):
    try:
        del request.session['email']
        messages.success(request, "Successfully logged out.")
    except:
        messages.error(request, "An error occurred. Try again.")
        return redirect('/')
    return redirect('/')

# def showtrains(request):
#     try:

#         user = accounts.objects.get(email=request.session['email'])
#         if request.method == 'POST':
#             if request.POST.get('source') and request.POST.get('destination'):
#                 rte = route()
#                 rte.source = request.POST.get('source')
#                 rte.destination = request.POST.get('destination')
#                 cursor = connection.cursor()
#                 cursor.execute(
#                     'SELECT * FROM accounts_train , accounts_route WHERE (accounts_route.source= %s  and accounts_route.destination =  %s) and accounts_route.train_name = accounts_train.train_name' ,[rte.source, rte.destination])
#                 showtrainsinfo = cursor.fetchall()
#                 cursor.close()
#                 return render(request, 'showtrains.html', {'showtrainsinfo': showtrainsinfo, 'user': user})
#         else:
#             return render(request, 'showtrains.html', { 'user': user})
#     except:
#         messages.error(request,'Please log in first')
#         return redirect('login')
def reset_password(request):
    try:
        if request.method == 'POST' and request.POST.get('resetEmail'):
            email = request.POST.get('resetEmail')

        if not accounts.objects.filter(email=email).first():
            # messages.error(request, 'No user found with this email.')
            return HttpResponse("No user found with this email.")

        user_obj = accounts.objects.get(email=email)
        token = str(uuid.uuid4())
        profile_obj = Profile.objects.get(user=user_obj.id)
        profile_obj.forget_password_token = token
        profile_obj.save()
        send_forget_password_mail(user_obj.email, token)
        return HttpResponse("An email is sent.")

    except Exception as e:
        print(e)
        return render(request, 'reset_password/forget-password.html')



def change_password(request, token):
    context = {}

    try:
        profile_obj = Profile.objects.filter(
            forget_password_token=token).first()
        context = {'user_id': profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                return HttpResponse("No user id found.")

            if new_password != confirm_password:
                return HttpResponse("Booth password should be equal")

            user_obj = accounts.objects.filter(id=user_id).first()
            user_obj.password = new_password
            user_obj.save()
            return HttpResponse("Password updated successfully!!")
        else:
            return render(request, 'reset_password/change-password.html', context)

    except Exception as e:
        print(e)
        return HttpResponse("url has already been used.")