from django.contrib import admin

# Register your models here.
from .models import User, UserOtp

admin.site.register(User)
admin.site.register(UserOtp)
