from django.contrib import admin
from .models import UserComents

# Registrar o modelo UserComents no admin
admin.site.register(UserComents)
