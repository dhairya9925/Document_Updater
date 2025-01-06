from django.shortcuts import render
from .models import user as users

# Logic functions
def checkPassword(password, email):
    data = users.objects.all().values()
    for usr in data:
        # print("--in for--")
        # print(f"\n\n--- {email} = {usr['email']} || {password} = {usr['password']} ---")
        if usr["email"] == email and usr["password"] == password:
            return [True, usr["name"]]
    return [False, None]


# Create your views here.
def login(request):
    if request.method == "POST":
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        email = request.POST.get('email')
        password = request.POST.get('password')
        res = checkPassword(password=password, email=email)[0]
        print(res)
        name = checkPassword(password=password, email=email)[1]
        print(name)
        if res == True:
            return render(request, "home.html", {"name": name})
        else:
            return render(request, "login.html", {"message": f"Worng email or password"})
        print("users not found")
    else:
        return render(request, "login.html")

        # print("\n\n---IN GET---")
        
        # print(f"\n\n--- {email} = {usr['email']} || {password} = {usr['password']} ---")
        # return render(request, "login.html")

def register(request):
    if request.method == "POST":
        print("POST")
        data = users.object.all().values()
        emails = []
        names = []
        for i in data:
            emails.append(i['email'])
            names.append(i['name'])
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if name in names:
            retu

        usr = users(name = name, email = email, password = password)
        usr.save()
        return render(request, "home.html", {"name": name})
    else:
        print("GET")
        return render(request, "register.html")

def home(request):
    return render(request, "home.html")
