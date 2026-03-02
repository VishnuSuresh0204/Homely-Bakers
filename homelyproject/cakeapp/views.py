from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    if request.POST:
        Email=request.POST['email']
        Password=request.POST['pass']
        user=authenticate(username=Email,password=Password)
        if user is not None:
            if user.usertype=="admin":
                messages.info(request,"Welcome To The Admin Page")
                return redirect("/adminHome")
            elif user.usertype=="user":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The User Page")
                return redirect("/userHome")
            elif user.usertype=="baker":
                request.session['uid']=user.id
                messages.info(request,"Welcome To The Baker Page")
                return redirect("/bakerHome")
            else:
                messages.info(request,"Invalid Username Or Password")
                return redirect("/login")
        else:
            messages.info(request,"Invalid Username Or Password")
            return redirect("/login")
    return render(request,"login.html")

def userRegister(request):
    if request.POST:
        username1=request.POST['username']
        email1=request.POST['email']
        phonenumber1=request.POST['phone']
        password1=request.POST['password']
        image1=request.FILES['profile_picture']
        address1=request.POST['address']
        if User.objects.filter(Email=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            user=Login.objects.create_user(
                username=email1,password=password1,usertype='user',viewPassword=password1)
            user.save()
            register=User.objects.create(
                Username=username1,Email=email1,Phonenumber=phonenumber1,Password=password1,ProfilePicture=image1,Address=address1,logid=user)
            register.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"userReg.html")

def bakerRegister(request):
    if request.POST:
        username1=request.POST['username']
        email1=request.POST['email']
        phonenumber1=request.POST['phone']
        password1=request.POST['password']
        experience1=request.POST['experience']
        image1=request.FILES['profile_picture']
        cert1=request.FILES['certi']
        address1=request.POST['address']
        if Baker.objects.filter(Email1=email1).exists():
            messages.info(request,"Already Have Registered")
        else:
            baker=Login.objects.create_user(
                username=email1,password=password1,usertype='baker',viewPassword=password1,is_active=0)
            baker.save()
            register=Baker.objects.create(
                Username1=username1,Email1=email1,Phonenumber1=phonenumber1,Password1=password1,ProfilePicture1=image1,Address1=address1,Certificate=cert1,Experience=experience1,logid=baker)
            register.save()
            messages.info(request,"Registered Successfully")
            return redirect("/login")
    return render(request,"bakerReg.html")


## ==============================   ADMIN   ================================

def adminHome(request):
    return render(request,"ADMIN/adminHome.html")

def viewUsers(request):
    user=User.objects.all()
    return render(request,"ADMIN/viewUsers.html",{'data':user})

def viewBakers(request):
    baker=Baker.objects.all()
    return render(request,"ADMIN/viewBakers.html",{'data':baker})

def ApproveBaker(request):
    status=request.GET['status']
    id=request.GET['id']
    bak=Login.objects.get(id=id)
    bak.is_active=int(status)
    bak.save()
    if status == '1':
        messages.info(request," Approved successfully")
    else:
        Login.objects.filter(id=id).delete()
        messages.info(request," Rejected successfully")
    return redirect("/viewBakers")

def DeleteBaker(request):
    id=request.GET['id']
    b=Baker.objects.filter(id=id)
    b.delete()
    messages.info(request,"Deleted Successfully")
    return redirect("/viewBakers")


## ==============================   BAKER   ================================

def bakerHome(request):
    return render(request,"BAKER/bakerHome.html")

def addCake(request):
    uid = request.session['uid']
    baker = Baker.objects.get(logid=uid)
    if request.method == 'POST':
        cake_name = request.POST['CakeName']
        cake_descri = request.POST['CakeDescri']
        cake_image = request.FILES['CakeImage']
        cake_category = request.POST['CakeCategory']
        cake_price = request.POST['CakePrice']
        cake_weight = request.POST['CakeWeight']
        cake_flavor = request.POST['CakeFlavor']
        cake_ingredients = request.POST['CakeIngredients']
        customizable_options = ', '.join(request.POST.getlist('CustomizableOptions[]')) 
        preparation_time = request.POST['PreparationTime']
        special_notes = request.POST['SpecialNotes']
        discount = request.POST['Discount'] 
        stock_quantity = request.POST['StockQuantity']
        earliest_delivery = request.POST['EarliestDelivery']
        cake=CakeDetails.objects.create(CakeName=cake_name,CakeDescri=cake_descri,
            CakeImage=cake_image,CakeCategory=cake_category,CakePrice=cake_price,
            CakeWeight=cake_weight,CakeFlavor=cake_flavor,CakeIngredients=cake_ingredients,
            CustomizableOptions=customizable_options,PreparationTime=preparation_time,SpecialNotes=special_notes,
            Discount=discount,StockQuantity=stock_quantity,EarliestDelivery=earliest_delivery,bakerid=baker)
        cake.save()
        messages.info(request,"Cake Added Successfully")
        return redirect('/viewCakes')
    return render(request, 'BAKER/addCakes.html')


def viewCakes(request):
    cake=CakeDetails.objects.all()
    return render(request,"BAKER/viewCakes.html",{'data':cake})

def updateCake(request):
    id = request.GET.get('id')
    edit = CakeDetails.objects.filter(id=id)
    if request.method == "POST":
        cake_name = request.POST.get('CakeName')
        cake_descri = request.POST.get('CakeDescri')
        cake_category = request.POST.get('CakeCategory')
        cake_price = request.POST.get('CakePrice')
        cake_weight = request.POST.get('CakeWeight')
        cake_flavor = request.POST.get('CakeFlavor')
        cake_ingredients = request.POST.get('CakeIngredients')
        preparation_time = request.POST.get('PreparationTime')
        special_notes = request.POST.get('SpecialNotes', '')
        discount = request.POST.get('Discount', '')
        stock_quantity = request.POST.get('StockQuantity')
        customizable_options_toggle = request.POST.get('CustomizableOptionsToggle')
        if customizable_options_toggle == 'Yes':
            customizable_options = request.POST.getlist('CustomizableOptions[]')
            customizable_options_str = ', '.join(customizable_options)
        else:
            customizable_options_str = 'None'
        cake_image = request.FILES.get('CakeImage')
        cake = CakeDetails.objects.get(id=id)
        cake.CakeName = cake_name
        cake.CakeDescri = cake_descri
        cake.CakeCategory = cake_category
        cake.CakePrice = cake_price
        cake.CakeWeight = cake_weight
        cake.CakeFlavor = cake_flavor
        cake.CakeIngredients = cake_ingredients
        cake.PreparationTime = preparation_time
        cake.SpecialNotes = special_notes
        cake.Discount = discount
        cake.StockQuantity = stock_quantity
        cake.CustomizableOptions = customizable_options_str
        if cake_image:  
            cake.CakeImage = cake_image
        cake.save()
        messages.info(request, "Cake Details Updated Successfully")
        return redirect('/viewCakes')
    return render(request, 'BAKER/updateCake.html', {'edit': edit})

def deleteCake(request):
    id=request.GET['id']
    c=CakeDetails.objects.filter(id=id)
    c.delete()
    messages.info(request,"Cake Deleted Successfully")
    return redirect("/viewCakes")


## ==============================   USER   ================================

def userHome(request):
    return render(request,"USER/userHome.html")

def userViewBakers(request):
    data=Baker.objects.all()
    return render(request,"USER/viewBakers.html",{'baker':data})

def userViewCakes(request):
    id=request.GET['id']
    data=CakeDetails.objects.filter(bakerid=id)
    return render(request,"USER/viewCakes.html",{'data':data})


def cakeDetail(request):
    id = request.GET.get('id') 
    uid=request.session['uid']
    if not id:
        return render(request, "USER/CakeDetail.html", {'error': "Invalid cake ID."})
    try:
        cake = CakeDetails.objects.get(id=id)  
    except CakeDetails.DoesNotExist:
        return render(request, "USER/CakeDetail.html", {'error': "Cake not found."})
    weight_options = cake.CakeWeight.split(',') if cake.CakeWeight else []
    customizable_options = cake.CustomizableOptions.split(',') if cake.CustomizableOptions else []
    if request.POST:
        qty=request.POST.get("quantity")
        desc=request.POST.get("desc")
        deltime=request.POST.get("deltime")
        id=request.POST.get("id")
        cid=CakeDetails.objects.get(id=id)
        pri=CakeDetails.objects.filter(id=id)
        amt=pri[0].CakePrice
        print(type(amt))
        total=amt*int(qty)
        print(total)
        uid=User.objects.get(id=id)
        obj=Booking.objects.create(cakeid=cid, uid=uid,qty=qty,total=total,desc=desc,deltime=deltime)
        obj.save()
        messages.info(request, "Booking Successfully")
    return render(request, "USER/CakeDetail.html", {
        'detail': [cake],
        'weight_options': weight_options,
        'customizable_options': customizable_options
    })
    

def viewbooking(request):
    uid=request.session['uid']
    user=User.objects.get(logid=uid)
    data=Booking.objects.filter(uid=user)
    return render(request,"USER/viewBooking.html",{"data":data})

def viewfeedback(request):
    uid=request.session['uid']
    user=User.objects.get(logid=uid)
    data=Feedback.objects.filter(uid=user)
    return render(request,"USER/viewFeedback.html",{"data":data})

def viewFeedback(request):
    uid=request.session['uid']
    baker=Baker.objects.get(logid=uid)
    data=Feedback.objects.filter(cakeid__bakerid=baker)
    return render(request,"BAKER/viewFeedback.html",{"data":data})


def viewFeedbacks(request):
    data=Feedback.objects.all()
    return render(request,"ADMIN/viewFeedback.html",{"data":data})

def viewBookings(request):
    data=Booking.objects.all()
    return render(request,"ADMIN/viewBooking.html",{"data":data})


def viewBooking(request):
    uid=request.session['uid']
    baker=Baker.objects.get(logid=uid)
    data=Booking.objects.filter(cakeid__bakerid=baker)
    return render(request,"BAKER/viewBooking.html",{"data":data})

def actionbooking(request):
    id=request.GET['id']
    i=Booking.objects.filter(id=id).update(status='Accepted')
    messages.info(request,"Accepted Successfully")
    return redirect("/viewBooking")

def rejectbooking(request):
    id=request.GET.get('id')
    j=Booking.objects.filter(id=id).delete()
    messages.info(request,"Rejected successfully")
    return redirect("/viewBooking")

def addPayment(request):
    uid = request.session['uid']
    id= request.GET.get("id")  
    total = request.GET.get("total")  
    print(total)
    if request.method == 'POST':
        booking = Booking.objects.filter(id=id).first() 
        if booking:
            booking.status = 'Paid'
            booking.save()
            messages.success(request, 'Payment successfully')
        return redirect('/viewbooking/')
    return render(request, "USER/addPayment.html",{'total':total})

def addFeedback(request):
    uid = request.session['uid']
    id= request.GET.get("id")  
    user = User.objects.get(logid=uid)
    cake = CakeDetails.objects.get(id=uid)  
    if request.POST:
        rating=request.POST['rating']  
        message1=request.POST['msg']  
        data=Feedback.objects.create(Message=message1,uid=user,cakeid=cake,Rating=rating)
        data.save()
        messages.success(request, 'Payment successfully')
    return render(request,"USER/addFeedback.html")



