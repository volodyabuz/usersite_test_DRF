from typing import Any
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import UserListSerializer
from .forms import *
from .models import *


def index(request):
    return HttpResponse('aaa')

class IndexPage(ListView):
    template_name = 'userlist/index.html'
    model = UserList
    context_object_name = 'users'
    paginate_by = 3

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        return context

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'userlist/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'userlist/login.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')


class UserListViewSet(viewsets.ModelViewSet):
    queryset = UserList.objects.all()
    serializer_class = UserListSerializer


# class UserListAPIList(generics.ListCreateAPIView):
#     queryset = UserList.objects.all()
#     serializer_class = UserListSerializer

# class UserListAPIUpdate(generics.UpdateAPIView):
#     queryset = UserList.objects.all()
#     serializer_class = UserListSerializer


# class UserListAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = UserList.objects.all()
#     serializer_class = UserListSerializer


