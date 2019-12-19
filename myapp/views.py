from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from . import urls
from .forms import ItemForm
from .models import Item

# Create your views here.
@login_required(login_url='/contas/login/')
def index(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.autor = request.user
            item.created = timezone.now()
            item.save()
            return redirect('index')
    else:
        form = ItemForm()

    items = Item.objects.all()
    count = items.count()

    context = {
        'form': form,
        'items': items,
        'count': count,
    }
    return render(request, 'index.html', context)

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms

from django.forms.models import modelform_factory
class ModelFormWidgetMixin(object):
    def get_form_class(self):
        return modelform_factory(self.model, fields=self.fields, widgets=self.widgets)


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = '__all__'

class ItemUpdate(LoginRequiredMixin, ModelFormWidgetMixin, UpdateView):
    model = Item
    fields = ['nome']
    widgets = {
        'nome': forms.TextInput(
            attrs = {
                'class':'input',
                'placeholder':'Atualizar nome do item',
                'value':'{{ item }}',
                'autocomplete': 'off',
            },
        ),
    }
    success_url = reverse_lazy('index')

class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')