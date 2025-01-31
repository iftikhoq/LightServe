from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages 
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm 
from django.contrib.auth import login, authenticate, logout,update_session_auth_hash
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

def Home(request):
    return render(request, 'index.html') 
