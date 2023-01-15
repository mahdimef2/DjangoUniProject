from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from mainapp.forms import RegisterForm
from mainapp.models import SocialNetwork


class Index(TemplateView):
    template_name = "mainapp/index.html"

    def get(self, request, *args, **kwargs):
        _contex = {
            "register_form": RegisterForm
        }
        return self.render_to_response(context=_contex)

    def post(self, request, *args, **kwargs):
        _form = RegisterForm(data=request.POST)
        if _form.is_valid():
            _user = _form.save(commit=False)
            _user.set_password(_form.cleaned_data["password"])
            _user.save()
            if not _user:
                messages.error(request, "Unsuccessful registration. User exists")
                return redirect("signup")

            messages.success(request, "regiser successsss")
            return redirect("login")

        else:
            messages.error(request, _form.errors)
            return redirect("index")


class Auth(TemplateView):
    template_name = "mainapp/login.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        _username = request.POST["username"]
        _password = request.POST["password"]
        _user = authenticate(request, username=_username, password=_password)
        if _user is not None:
            login(request, _user)
            messages.success(request, "you are logggged in ")
            return redirect("login")


@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect('login')


class aboutus(TemplateView):
    template_name = "mainapp/aboutus.html"

    def get(self, request, *args, **kwargs):
        return self.render_to_response({})


# @login_required(login_url='login')
class AddSocial(TemplateView):
    template_name = "mainapp/profile.html"

    def get(self, request, *args, **kwargs):
        social_network_links = SocialNetwork.objects.filter(user_name=request.user.username)
        if social_network_links is not None:
            return render(request, 'mainapp/profile.html', {'social_network_links': social_network_links})
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        social_name = request.POST["social_name"]
        data = SocialNetwork.objects.create(
            user_name=request.user.username,
            social_network_link=social_name)
        data.save()

        if data is not None:
            messages.success(request, "added ")
            return redirect("addsocial")
