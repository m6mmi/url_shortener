from django.contrib import admin

# Register your models here.
from shortener_app.models import AliasedUrl

admin.site.register(AliasedUrl)