from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .models import userProfile
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer
from .forms import Vhod, Regis
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.models import User

class UserProfileListCreateView(ListCreateAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=userProfile.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

def main(request):
    user = request.user
    return render(request, "main.html", {'user': user})

def login(request):
    auth = Vhod()
    return render(request, "login.html", {'auth': auth})

def reg(request):
    auth = Regis()
    return render(request, "reg.html", {'auth': auth})

def test1(request):
    if request.user == True:
        user = 'Выйдите с аккаунта для регистрации!'
    else:
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user1 = User.objects.create_user(username=username, email=email, password=password)
        user1.save()
        user = 'Успешно'
    return render(request, "test1.html", {'user': user})

def logout_view(request):
    logout(request)
    return render(request, "main.html")

def test(request):
    user = request.user
    return render(request, "test.html", {'user': user})