from django.contrib import admin
from profiles.models import Profile, Address
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
   list_display = ('user', "first_name", "last_name", "age", "created_at")
   fields = ('user', "first_name", "last_name", "age", "created_at")
   readonly_fields = ("created_at",)
   search_fields = ("first_name", "last_name")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
   list_display = ('user', 'city', 'address')
   fields = ('user', 'city', 'address')
   search_fields = ('user',)