from django.contrib import admin
from django.contrib.auth.models import User
from .models import Settings
from django.contrib.auth.admin import UserAdmin


class UserAdminCustom(UserAdmin):
    list_display = ('username', 'is_staff', 'is_superuser')
    search_fields = ['username']

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(request, queryset, search_term)
        if not request.user.is_superuser:
            if request.user.groups.filter(name="Технолог").exists():
                queryset = queryset.filter(groups__name="Швея")
        return queryset, may_have_duplicates


admin.site.unregister(User)
admin.site.register(User, UserAdminCustom)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']
    search_fields = ['username']

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(request, queryset, search_term)
        if not request.user.is_superuser:
            if request.user.groups.filter(name="Бухгалтер").exists():
                queryset = queryset.filter(name='Стоймость одной секунды')
        return queryset, may_have_duplicates
