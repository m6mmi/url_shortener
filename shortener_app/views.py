from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.views.generic import CreateView
from django.urls import reverse
from .models import AliasedUrl
from django import forms

from django.apps import apps

def redirect_view(request, alias):
    aliased_url = AliasedUrl.objects.get(alias=alias)
    return redirect(aliased_url.url)


def url_list_view(request):
    model_fields = [field.name for field in AliasedUrl._meta.fields]
    urls = AliasedUrl.objects.all()
    context = {
        'model_name': AliasedUrl._meta.verbose_name_plural.title(),
        'model_fields': model_fields,
        'urls': urls
    }
    return render(request, 'url_list.html', context)


class AliasedUrlForm(ModelForm):
    class Meta:
        model = AliasedUrl
        fields = ['url']
        widgets = {'url': forms.TextInput(attrs={'placeholder': 'Enter URL to shorten',
                                                'id': 'url-input'})}

class AliasCreateView(CreateView):
    form_class = AliasedUrlForm
    template_name = 'create_alias.html'

    def get_success_url(self):
        return f'{reverse("create")}?created_alias={self.object.alias}'
    

def base_page(request):
    return render(request, 'base.html')
