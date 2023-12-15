from django.contrib import admin
from users.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    ordering = ("-date_joined", )
    list_display = ("__str__", "email", "full_name", "age", "sex", "is_active")
    list_filter = ("date_joined", "last_login", "sex", "is_active")
    search_fields = ("email", "full_name", "address")
