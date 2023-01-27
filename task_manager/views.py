from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator
from django.contrib.auth import logout, login
from django.views.generic import FormView
from django.views.generic import TemplateView


class IndexView(SuccessMessageMixin, TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('User'), 'btn': _('Create')}


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('Successfully login')
    # success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    logout(request)
    return redirect('home')