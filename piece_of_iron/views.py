from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.models import Users


# Create your views here.
# class PieceView:
#     pass

def PieceView():
    pass


class PieceView(ListView):
    # pass
    template_name = 'users/users.html'
    model = Users
    context_object_name = 'users'
    # extra_context = {'title': _('Users'), 'btn_update': _('Update'), 'btn_delete': _('Delete')}
    redirect_field_name = 'home'
