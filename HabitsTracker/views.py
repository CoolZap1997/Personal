from http.client import HTTPResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import UserForm
from .models import User

# Create your views here.
def addPerson(request):
    return HTTPResponse("<h3>Add Person</h3>")

def index(request):
    return render(request, "HabitsTracker/index.html")

def sayHello(request):
    return HTTPResponse("<h3>Say Hello</h3>")

def sayHello(request, name):
    return HttpResponse(f"<h3>Hello {name}</h3>")

@csrf_protect
def addPerson(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if(form.is_valid()):
            try:
                user = User()
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.gender = form.cleaned_data['gender']
                user.country_code = form.cleaned_data['country_code']
                user.phone = form.cleaned_data['phone']
                user.email = form.cleaned_data['email']
                print(form.cleaned_data['password'])
                print(form.cleaned_data['confirm_password'])
                if form.cleaned_data['password'].strip() == form.cleaned_data['confirm_password'].strip():
                    user.password = form.cleaned_data['password'].strip()
                    print("It's here")
                else:
                    print("How the fuck is it here also?")
                    raise Exception('Password do not match')
                user.save()
                return render(request, "HabitsTracker/add_success.html")
            except Exception as e:
                return render(request, "HabitsTracker/add_failed.html", {'msg':e})
            except:
                return render(request, "HabitsTracker/add_failed.html", {'msg':'Some Random Issue'})
        else:
            return render(request, "HabitsTracker/add_failed.html")
    else:
        form = UserForm()
        return render(request, "HabitsTracker/add_person.html", {'form':form})
