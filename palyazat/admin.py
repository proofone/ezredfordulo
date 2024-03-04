from django.contrib import admin
from palyazat.models import User, Kiiras


class UserAdmin(admin.ModelAdmin):
    exclude =  []
    search_fields = ['email']


class KiirasAdmin(admin.ModelAdmin):
    exclude =  []


admin.site.register(User, UserAdmin)
admin.site.register(Kiiras, KiirasAdmin)
