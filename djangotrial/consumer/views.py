from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import users
from core.models import orders, product
from django.template import loader

# -------------------------------------------------------------------------------------------------------------------------

# --- Store data in sessoin ---
def get_user_from_session(request):
    user_id = request.session.get('user_id')
    if user_id:
        return users.objects.get(id=user_id)
    return None

def loggedin(request, user_id):
    request.session['user_id'] = user_id
    request.user = users.objects.get(id = user_id)
    

def authenticate(request, email, password):
    user = users.objects.get(email = email, password = password)
    if user is not None:
        return user.id
    return None

# -------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------
# Create your views here.
def login(request):
    if request.method == "POST":
        print("\n\n---IN POST---")

        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email, password)
        # print(f"--- User: {user} ---")
        if user is not None:
            loggedin(request, user)
            # print(f"--- User: {user} ---")
            return HttpResponseRedirect("../")
        # save email to session
        # print(f"--- Session: {request.session.get("consumer_email")} ---")
            print(f"--- Session: {request.user.name} ---")
                    
        
        # if authenticate(request, email, password) == True:
        #     return HttpResponseRedirect("../")
        else:
            print("\n\n---IN ELSE---")
            return render(request, "login.html", {"message": f"Worng email or password"})
    else:
        print("\n\n---IN GET---")
        # print(f"--- Session: {request.session.get("consumer_email")} ---")
        
        # print(f"\n\n--- {email} = {usr['email']} || {password} = {usr['password']} ---")
        return render(request, "login.html")
        # return HttpResponseRedirect("login")



def register(request):
    if request.method == "POST":
        print("POST")
        names = users.objects.values_list("name", flat=True)
        emails = users.objects.values_list("email", flat=True)
        # emails = []
        # names = []
        # for i in data:
        #     emails.append(i['email'])
        #     names.append(i['name'])
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if name in names:
            print("\n\n -- IF -- ")
            return render(request, "register.html", {"message": "User Already Exist! Please Login"})
        elif email in emails:
            print("\n\n -- ELIF -- ")
            return render(request, "register.html", {"message": "User Already Created On this E-mail"})
        else:
            print("\n\n -- ELSE -- ")
            usr = users(name = name, email = email, password = password, contact = None)
            usr.save()

            return HttpResponseRedirect(request, "home.html")
    else:
        print("\n\n -- GET -- ")
        return render(request, "register.html")


def home(request):
    user = get_user_from_session(request)
    print(f"--- IS {user} ----")
    if user is not None:
        print("--- IS LOGGED IN ----")
        
        return render(request, "home.html", {"name": user.name})
    else:
        print("--- NOT LOGGED IN ----")
        # print(f"--- NOT LOGGED {{ user }} ----")
        return render(request, "home.html")


def cart(request):
    user = get_user_from_session(request)
    if user is not None:
        return render(request, "cart.html", {"name": user.name, "order": user.order})
        return render(request, "cart.html", {"name": user.name, "order": user.order, "products": user.order.products})
    else:
        return render(request, "cart.html")


def logout(request):
    request.session.flush()
    return HttpResponseRedirect("../login")

def profile(request):
    user = get_user_from_session(request)
    if user is not None:
        return render(request, "profile.html", {"user": user})
    else:
        return HttpResponseRedirect("../login")

def deleteAccount(request):
    user = users.objects.get(id = request.session.get("user_id"))
    print(f"--- User({user.name}) Deleted ---")
    # user.delete()
    request.session.flush()
    return HttpResponseRedirect("../")
# -------------------------------------------------------------------------------------------------------------------------
