from django.shortcuts import render
import json
import hashlib
from core.models import countryCode
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Logic functions
def checkPassword(password, email):
    data = Seller.objects.all().values()
    for usr in data:
        # print("--in for--")
        # print(f"\n\n--- {email} = {usr['email']} || {password} = {usr['password']} ---")
        if usr["email"] == email and usr["password"] == password:
            return [True, usr["name"]]
    return [False, None]


def insert():
    with open('/workspaces/Document_Updater/djangotrial/seller/countryCode.json', "r+") as file:
        data = json.load(file)
        for val in data:
            country = val["name"]
            dialCodes = val["dialCodes"]
            image = val["image"]
            if len(dialCodes) > 1:
                for dialCode in dialCodes:
                    sReg = countryCode(country = country, dialCode = dialCode,image = image)
                    sReg.save()
                    print(f"country = {country}, dialCode = {dialCode},image = {image}")
                print("--- More than 1 dialCode ---")
            else:
                sReg = countryCode(country = country, dialCode = dialCodes[0],image = image)
                sReg.save()
                print(f"country = {country},\ndialCode = {dialCodes[0]},\nimage = {image}\n\n")
    return 0



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
        res = checkPassword(password=password, email=email)[0]
        print(res)
        name = checkPassword(password=password, email=email)[1]
        print(name)
        if res == True:
            return render(request, "dashboard.html", {"name": name})
        else:
            return render(request, "Slogin.html", {"message": f"Worng email or password"})
    else:
        return render(request, "Slogin.html")

def register(request):
    data = countryCode.objects.all().values()
    first = data[0]
    if request.method == "POST":
        temp["name"] = request.POST["name"]
        temp["email"] = request.POST["email"]
        temp["phone"] = request.POST["phone"]
        password = request.POST["password"]
        password = password.encode()
        password = hashlib.sha256(password)
        temp["password"] = request.POST["password"]
        # country = countryCode[1]
        print("-- REQUESTED \"POST\" METHOD --")
        # usr = Seller(name = name, email = email, password = password)
        # usr.save()
        # return render(request, "dashboard.html", {"name": name})
        # return render(request, "dashboard.html")
    else:
        print("GET")
    return render(request, "Sregister.html", {'data': data, 'first': first})

def gstin(request):
    return render(request, "gstin.html")

def dashboard(request):
    return render(request, "dashboard.html")
