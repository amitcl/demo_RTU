from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from crmapp.models import Customer,Enquiry,Login
from . models import Product
from customerapp.models import Response

# Create your views here.c
def adminhome(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            return render (request,"adminhome.html",locals())
    except KeyError:
        return redirect("crmapp:login")
def logout(request):
    try:
        del request.session["adminid"]
        return redirect ("crmapp:/login")  
    except KeyError:
        return redirect("crmapp:logout")
    
def viewcustomers(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            cust=Customer.objects.all()
            return render (request,"viewcustomers.html",locals())
    except KeyError:
        return redirect("crmapp:login")
def logout(request):
    try:
        del request.session["adminid"]
        return redirect ("crmapp:/login")  
    except KeyError:
        return redirect("crmapp:logout") 
def viewenquiries(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            enq=Enquiry.objects.all()
            return render (request,"viewenquiries.html",locals())
    except KeyError:
        return redirect("crmapp:login")

def logout(request):
    try:
        del request.session["adminid"]
        return redirect ("crmapp:/login")  
    except KeyError:
        return redirect("crmapp:logout") 
def delenq(request,id):
    Enquiry.objects.get(id=id).delete()
    return redirect("adminapp:viewenquiries") 
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def product(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            if request.method=="POST":
                productname=request.POST["productname"]
                mfgdate=request.POST["mfgdate"]
                expdate=request.POST["expdate"]
                price=request.POST["price"]
                productpic=request.FILES["productpic"]
                prd=Product(productname=productname, mfgdate=mfgdate, expdate=expdate, price=price, productpic=productpic)
                prd.save()
                msg='Product is added'
                return render(request,"product.html",locals())
            return render(request,"product.html",locals())
    except KeyError:
        return redirect("crmapp:login")  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def viewcomplaints(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            comp=Response.objects.filter(responsetype='complaint')
            return render (request,"viewcomplaints.html",locals())
    except KeyError:
        return redirect("crmapp:login")    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def viewfeedbacks(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            feed=Response.objects.filter(responsetype='Feedback')
            return render (request,"viewfeedbacks.html",locals())
    except KeyError:
        return redirect("crmapp:login")  
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def delres(request,id):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            Response.objects.get(id=id).delete()
            return render (request,"adminhome.html",locals())
    except KeyError:
        return redirect("crmapp:login")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def changepassword(request):
    try:
        if request.session["adminid"]!=None:
            adminid=request.session["adminid"]
            return render (request,"changepassword.html",locals())
    except KeyError:
        return redirect("crmapp:login")         