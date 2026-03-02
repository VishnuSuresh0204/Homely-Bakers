from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Login(AbstractUser):
    usertype=models.CharField(max_length=20)
    viewPassword=models.CharField(max_length=200,null=True)
    
class User(models.Model):
    logid= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Email=models.EmailField()
    Phonenumber=models.IntegerField()
    Password=models.CharField(max_length=20)
    ProfilePicture=models.ImageField(upload_to="Image",null=True)
    Address=models.CharField(max_length=200)
    ustatus=models.CharField(max_length=20,default='pending')
    
class Baker(models.Model):
    logid= models.ForeignKey(Login,on_delete=models.CASCADE,null=True)
    Username1=models.CharField(max_length=20)
    Email1=models.EmailField()
    Phonenumber1=models.IntegerField()
    Password1=models.CharField(max_length=20)
    Experience=models.CharField(max_length=20)
    ProfilePicture1=models.ImageField(upload_to="Image",null=True)
    Certificate=models.ImageField(upload_to="Image",null=True)
    Address1=models.CharField(max_length=200)
    bstatus=models.CharField(max_length=20,default='pending')
    
class CakeDetails(models.Model):
    bakerid= models.ForeignKey(Baker,on_delete=models.CASCADE,null=True)
    CakeName=models.CharField(max_length=100)
    CakeDescri=models.CharField(max_length=500)
    CakeImage=models.ImageField(upload_to="Image",null=True)
    CakeCategory=models.CharField(max_length=100)
    CakePrice=models.IntegerField(null=True)
    CakeWeight=models.CharField(max_length=200)
    CakeFlavor=models.CharField(max_length=200)
    CakeIngredients=models.CharField(max_length=500)
    CustomizableOptions=models.CharField(max_length=500)
    StockQuantity=models.CharField(max_length=500)
    EarliestDelivery=models.CharField(max_length=40,default='Today')
    cstatus=models.CharField(max_length=40,default='Available')
    
class Booking(models.Model):
    cakeid= models.ForeignKey(CakeDetails,on_delete=models.CASCADE,null=True)
    uid= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    qty=models.CharField(max_length=50)
    total=models.CharField(max_length=500)
    desc=models.CharField(max_length=500)
    status=models.CharField(max_length=20,default='pending')
    date=models.DateField(auto_now_add=True)
    deltime=models.CharField(max_length=500)
    weight=models.CharField(max_length=100,null=True)
    customization=models.CharField(max_length=500,null=True)
    
class Feedback(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cakeid= models.ForeignKey(CakeDetails,on_delete=models.CASCADE,null=True)
    Message=models.CharField(max_length=200,null=True)
    Rating=models.CharField(max_length=200,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    fstatus=models.CharField(max_length=20,default='pending')
    bookingid=models.ForeignKey(Booking,on_delete=models.CASCADE,null=True)
    
    