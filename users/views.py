from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group, User
from .forms import SignUpForm


def home(request):
    if is_manager(request.user):
        return render(request, "users/fortest.html")
    elif is_member(request.user):
        return redirect('contact_form')
    else:
        return render(request, "users/home.html")


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def post(self, request, *args, **kwargs):
        pass
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user_group = Group.objects.get(name='Members')
            user.groups.add(user_group)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


def is_manager(user):
    return user.groups.filter(name='Managers').exists()


def is_member(user):
    return user.groups.filter(name='Members').exists()
