from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .forms import UserCreationForm, LoginForm


class Index(TemplateView):
    template_name = "index.html"


class CreateAccount(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("program:index")
        return render(request, "create.html", {"form": form})

    def get(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        return render(request, "create.html", {"form": form})


class AccountLogin(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('program:index')
        return render(request, 'login.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})


class MainLesson(TemplateView):
    template_name = "main.html"

