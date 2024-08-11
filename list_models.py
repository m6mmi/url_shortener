import os
import django
from django.apps import apps
from django.conf import settings

# Ensure settings are configured
if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'url_shortener.settings')
    django.setup()

# Get the model by name
model_name = 'AliasedUrl'
app_label = 'shortener_app'  # Replace with the actual app label where the model is defined

model = apps.get_model(app_label, model_name)

if model:
    # print(model._meta.__dict__.keys())
    print()
    print(model.__dict__.keys())
    print(model._meta.verbose_name_plural.title())
    for instance in model.objects.all():
        print(' ', instance.pk, instance)
else:
    print(f'Model {model_name} not found in app {app_label}')

print()