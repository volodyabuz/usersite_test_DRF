from django.contrib import admin
from .models import *


class UserListAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'sex_id')

class MaleFemaleAdmin(admin.ModelAdmin):
    list_display = ('sex',)

admin.site.register(UserList, UserListAdmin)
admin.site.register(MaleFemale, MaleFemaleAdmin)
