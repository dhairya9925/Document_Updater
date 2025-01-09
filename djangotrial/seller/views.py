from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
import hashlib
from core.models import countryCode
from .models import Seller
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin


# -------------------------------------------------------------------------------------------------------------------------

# --- Store data in sessoin ---
def get_seller_from_session(request):
    seller = Seller.objects.get(id = request.session.get("seller"))
    if seller is not None:
        return seller
    return None

def loggedin(request, seller):
    request.session['seller'] = seller
    request.seller = seller
    

def authenticate(request, email, password):
    seller1 = Seller.objects.get(id = 1) 
    print(f"-- Seller From auth {seller1.email} , {email} --")
    seller = Seller.objects.get(email = email, password = password)
    if seller is not None:
        return seller.id
    return None


# # Logic functions
# def checkPassword(password, email):
#     data = Seller.objects.all().values()
#     for usr in data:
#         # print("--in for--")
#         # print(f"\n\n--- {email} = {usr['email']} || {password} = {usr['password']} ---")
#         if usr["email"] == email and usr["password"] == password:
#             return [True, usr["name"]]
#     return [False, None]

# def insert():
#     with open('/workspaces/Document_Updater/djangotrial/seller/countryCode.json', "r+") as file:
#         data = json.load(file)
#         for val in data:
#             country = val["name"]
#             dialCodes = val["dialCodes"]
#             image = val["image"]
#             if len(dialCodes) > 1:
#                 for dialCode in dialCodes:
#                     sReg = countryCode(country = country, dialCode = dialCode,image = image)
#                     sReg.save()
#                     print(f"country = {country}, dialCode = {dialCode},image = {image}")
#                 print("--- More than 1 dialCode ---")
#             else:
#                 sReg = countryCode(country = country, dialCode = dialCodes[0],image = image)
#                 sReg.save()
#                 print(f"country = {country},\ndialCode = {dialCodes[0]},\nimage = {image}\n\n")
#     return 0

# -------------------------------------------------------------------------------------------------------------------------


# --- Create your views here --- 

temp = {
    "name":"",
    "phone":"",
    "email":"",
    "password":""
}

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        seller = authenticate(request, email, password)

        if seller is not None:
            loggedin(request, seller)
            return HttpResponseRedirect("../seller")
        else:
            return render(request, "Slogin.html", {"message": f"Worng email or password"})
    else:
        return render(request, "Slogin.html")

def register(request):
    countryCodes = countryCode.objects.all().values()
    first = countryCodes[0]
    if request.method == "POST":

        dialCode = request.POST["dialCode"]
        contact = request.POST["contact"]
        # password = password.encode()
        # password = hashlib.sha256(password)

        seller = {
            "name" : request.POST["name"],
            "email" : request.POST["email"],
            "contact" : str(dialCode + " " + contact),
            "password" : request.POST["password"],
        }
        request.session["seller"] = seller
        print(f"=== {request.session["seller"]} ===")
        if request.session["seller"] is not None:
            return HttpResponseRedirect("gstin")
        # print(type(dialCode))
        # print(type(contact))

        # country = countryCode[1]
        # print(f"-- REQUESTED \"POST\"{} METHOD --")
        # register = Seller(username = user["name"], email = user["email"], password = user["password"], contact = user["contact"])
        # register.save()
        # return render(request, "dashboard.html", {"name": name})
        return render(request, "Sregister.html")
    else:
        print("GET")
    return render(request, "Sregister.html", {'countryCodes': countryCodes, 'first': first})

def gstin(request):
    if request.method == "POST":

        seller_data = request.session.get("seller")
        print(f" --- {seller_data} --- ")

        print(f" --- {request.POST["city"]} {request.POST["district"]} {request.POST["state"]} --- ")
        
        city = request.POST["city"],
        district = request.POST["district"],
        state = request.POST["state"],


        if seller_data is not None:
            seller = Seller(
                name = seller_data["name"],
                email = seller_data["email"],
                contact = seller_data["contact"],
                password = seller_data["password"],
                address = request.POST["address"],
                city = city,
                district = district,
                state = state,
                pincode = request.POST["pincode"],
                companyName = request.POST["companyName"],
                gstin = request.POST["gstin"],
                storeName = request.POST["storeName"],
            )
            seller.save()
            return HttpResponseRedirect("../")
        else:
            return HttpResponseRedirect("register")
    else:
        seller_data = request.session.get("seller")
        if seller_data is not None:
            return render(request, "gstin.html")
        else:
            return HttpResponseRedirect("seller")
            return HttpResponseRedirect("register")
        

def main(request):
    if request.session.get("seller") is not None:
        return render(request, "main.html")
    else:
        return HttpResponseRedirect("login")

def logout(request):
    request.session.flush()
    return HttpResponseRedirect("login")

# --- DASHBOARD ---
@xframe_options_sameorigin
def sidebar(request):
    return render(request, "dashboard/sidebar.html")

@xframe_options_sameorigin
def dashboard(request):
    return render(request, "dashboard/dashboard.html")

@xframe_options_sameorigin
def products(request):
    return render(request, "dashboard/products.html")

@xframe_options_sameorigin
def orders(request):
    return render(request, "dashboard/orders.html")

@xframe_options_sameorigin
def customers(request):
    return render(request, "dashboard/customers.html")

@xframe_options_sameorigin
def profile(request):
    return render(request, "dashboard/profile.html")

