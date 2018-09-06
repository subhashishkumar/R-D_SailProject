from django.conf import settings
from django.contrib import admin
from login.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

# Register your models here.
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User

class CustomUserAdmin(UserAdmin):   
    form = CustomUserChangeForm
    list_display = ("username", "first_name", "last_name", "is_superuser", )


class ProfileTable(admin.ModelAdmin):
    list_display = ("user", "unit",)
    list_filter = ('unit',)


admin.site.register(Profile, ProfileTable)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)