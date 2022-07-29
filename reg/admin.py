from django.contrib import admin
from .models import Customer, Employee


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display=('id','name', 'email', 'city')



@admin.register(Employee)
class UserAdmin2(admin.ModelAdmin):
    list_display=('id','name', 'email', 'city')    