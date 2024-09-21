from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rolepermissions.roles import assign_role
from django.contrib import messages
from django.contrib.messages import constants 
from .utils.utils import is_valid_email
from .models import UserPhone
from django.contrib import auth
# Create your views here.

def login(request):
    method = request.method 
    if method == "GET":
        return render(request=request, template_name='users/logar.html')
    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = auth.authenticate(request,username=email,password=password)
        if not user:
            messages.add_message(request,constants.ERROR, "Usuario ou senha incorretos")
            return redirect('/users/logar')
        auth.login(request=request,user=user)
        return redirect('/home')
        
        

def register_user(request):
    method = request.method 
    if method == "GET":
        return render(request=request, template_name='users/cadastro.html')
    else:
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        confirmpw =request.POST.get("confirmpw")
        if not name:
            messages.add_message(request,constants.WARNING, "Nome não pode ser nulo")
            return redirect('/users/register')
        if password != confirmpw:
            messages.add_message(request,constants.WARNING, "As senhas não coincidem")
            return redirect('/users/register')
        if not is_valid_email(email):
            messages.add_message(request,constants.WARNING, "Email invalido")
            return redirect('/users/register')
        if not (str.isdigit(phone) or len(phone) == 11):
            messages.add_message(request,constants.WARNING, "Numero invalido digite no formato: 79999999999")
        names = name.split(" ")
        first_name = names[0]
        last_name = names[-1]

        user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password, username=email)
        try:
            user.save()
        except Exception as e:
            print(e)
            messages.add_message(request,constants.WARNING, "Error interno do servidor contate o administrador do sistema")
            return redirect('/users/register')
        user_phone = UserPhone(user=user,phone_number=phone)
        user_phone.save()
        messages.add_message(request,constants.SUCCESS, "Conta Criada com sucesso !!")
        assign_role(user=user, role="component")
        return redirect('/users/logar')
        
        

