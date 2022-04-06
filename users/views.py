from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import Group, User
from .forms import SignUpForm


# Создаем здесь представления.
#user = User.objects.get()
def is_member(user):
    return user.groups.filter(name='Manager').exists()


def home(request):
    if is_member(request.user):
        return render(request, "users/fortest.html")
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
