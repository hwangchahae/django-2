from django.contrib import admin
from .models import Post  # Import your models here
# Register your models here.
admin.site.register([Post])  # Register your models here, e.g., admin.site.register(MyModel)