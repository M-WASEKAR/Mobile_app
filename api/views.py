
from django.contrib.auth.models import User
import csv
from .forms import UserBulkUploadForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import User
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth import login, authenticate
import pandas as pd


def user_register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, 'successfully registerd')
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hello {user.username}! You have been logged in'
            else:
                message = 'Login failed!'
    return render(
        request, 'login.html', context={'form': form, 'message': message})



def user_bulk_upload(request):
    if request.method == 'POST':
        form = UserBulkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            data = pd.read_csv(csv_file)
            for index, row in data.iterrows():
                if 'username' in row and 'email' in row and 'password' in row:
                    if User.objects.filter(username=row['username']).exists() or User.objects.filter(
                            email=row['email']).exists():
                        continue
                    user = User.objects.create(username=row['username'], email=row['email'], password=row['password'])

            return redirect('dashboard')
    else:
        form = UserBulkUploadForm()
    return render(request, 'user_bulk_upload.html', {'form': form})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})


def user_list_filter(request):
    country = request.GET.get('country')
    if country:
        users = User.objects.filter(country=country)
    else:
        users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

class UserCreateView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'user_create.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'user_create.html', {'form': form})

class UserUpdateView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(instance=user)
        return render(request, 'user_update.html', {'form': form, 'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'user_update.html', {'form': form, 'user': user})

class UserDeleteView(View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        return render(request, 'user_delete.html', {'user': user})

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return redirect('user_list')


