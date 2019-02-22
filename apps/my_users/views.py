from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager
from apps import the_wall
import bcrypt

def index(request):
    
    return render(request, "my_users/index.html")

def new_user(request):
    
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    else:
        if request.method == "POST":
            user = User.objects.filter(email = request.POST['email'])
            if user:
                print (user)
                messages.warning(request, "User already exist") 
                return redirect("/")

            hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

            new_user = User.objects.create(first_name = request.POST['f_name'], last_name = request.POST['l_name'], email = request.POST['email'], password = hash_pw, birthdate = request.POST['dob'])
            
            request.session['user_id'] = new_user.id
            request.session['user_name'] = new_user.first_name
            messages.success(request, "Successfully registered !")
            return redirect("/wall")

    return redirect("/")
    
def user_login(request):

    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    else:
        if request.method == "POST":
            this_user = User.objects.filter(email = request.POST['user_email']).values()
            print(this_user)
            if this_user:
                pw_hash = this_user[0]['password']            
                print(pw_hash)
                if bcrypt.checkpw(request.POST['user_password'].encode(), pw_hash.encode()):
                    request.session['user_name'] = this_user[0]['first_name']
                    request.session['user_id'] = this_user[0]['id']

                    messages.success(request, "Successfully logged in !")
                    return redirect("/wall")
                
            messages.info(request, "You cannot be logged in")
            return redirect("/")

    return redirect("/")

def user_logout(request):
    
    request.session.clear()

    return redirect("/")