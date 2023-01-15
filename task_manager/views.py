from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.
def index(request):
    text = _("this is some random text")
    return render(request, 'index.html', {'text': text})