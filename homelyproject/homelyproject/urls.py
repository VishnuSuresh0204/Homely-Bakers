"""
URL configuration for homelyproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cakeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("", views.index),
    path("login/", views.login),
    path("userRegister/", views.userRegister),
    path("bakerRegister/", views.bakerRegister),
    
    # ================ ADMIN =================
    
    path("adminHome/", views.adminHome),
    path("viewUsers/", views.viewUsers),
    path("viewBakers/", views.viewBakers),
    path("ApproveBaker/", views.ApproveBaker),
    path("DeleteBaker/", views.DeleteBaker),
    path("viewBookings/", views.viewBookings),
    path("viewFeedbacks/", views.viewFeedbacks),
    
    # ================ BAKER =================
    
    path("bakerHome/", views.bakerHome),
    path("addCake/", views.addCake),
    path("viewCakes/", views.viewCakes),
    path("updateCake/", views.updateCake),
    path("deleteCake/", views.deleteCake),
    path("viewBooking/", views.viewBooking),
    path("actionbooking/", views.actionbooking),
    path("rejectbooking/", views.rejectbooking),
    path("viewFeedback/", views.viewFeedback),
    
    # ================ USER =================
    
    path("userHome/", views.userHome),
    path("userViewBakers/", views.userViewBakers),
    path("userViewCakes/", views.userViewCakes),
    path("cakeDetail/", views.cakeDetail),
    path("viewbooking/", views.viewbooking),
    path("addPayment/", views.addPayment),
    path("addFeedback/", views.addFeedback),
    path("viewfeedback/", views.viewfeedback),
]
