from django.contrib import admin
from formapi.models import users

class usersAdmin(admin.ModelAdmin):
    list_display=('uid','datatest')
admin.site.register(users, usersAdmin)
