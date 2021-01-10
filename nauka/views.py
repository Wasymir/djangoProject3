from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView,DetailView, CreateView, UpdateView
from .models import *
from .forms import *
#
# def test1(request):
#     return render(request, 'index.html', {})
class Home(CreateView):
    model = Prod
    form_class = ProductForms
    template_name = 'tab.html'
    # fields = '__all__'

