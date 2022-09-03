from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse



def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        form.save()
        email_subject = f'Website contact from {form.cleaned_data["name"]}'
        email_message = f'{form.cleaned_data["email"]}:\n\n{form.cleaned_data["message"]}'
        send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS)
        data = {'name':form.cleaned_data["name"], 'email':form.cleaned_data["email"], 'message':form.cleaned_data["message"]}
        return JsonResponse(data, safe=False)

    projects = Project.objects.filter(featured=True)
    paired = []
    for i in range(len(projects)//2):
        paired.append([projects[i*2],projects[(i*2)+1]])

    form = ContactForm()
    
    return render(request, "main/index.html", {
        "projects": paired,
        "form": form,
        "message": "none",
    })


        
        



# def login_view(request):
#     if request.method == "POST":

#         # Attempt to sign user in
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)

#         # Check if authentication successful
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse("index"))
#         else:
#             return render(request, "auctions/login.html", {
#                 "message": "Invalid username and/or password."
#             })
#     else:
#         return render(request, "auctions/login.html")


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("index"))


# def register(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         email = request.POST["email"]

#         # Ensure password matches confirmation
#         password = request.POST["password"]
#         confirmation = request.POST["confirmation"]
#         if password != confirmation:
#             return render(request, "auctions/register.html", {
#                 "message": "Passwords must match."
#             })

#         # Attempt to create new user
#         try:
#             user = User.objects.create_user(username, email, password)
#             user.save()
#         except IntegrityError:
#             return render(request, "auctions/register.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("index"))
#     else:
#         return render(request, "auctions/register.html")
