from django.contrib import admin
from palyazat.models import User


class UserAdmin(admin.ModelAdmin):
    exclude =  []


admin.site.register(User, UserAdmin)
