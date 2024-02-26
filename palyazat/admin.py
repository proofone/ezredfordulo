from django.contrib import admin
from palyazat.models import User


class UserAdmin(admin.ModelAdmin):
    exclude =  []
    search_fields = ['email']


admin.site.register(User, UserAdmin)
