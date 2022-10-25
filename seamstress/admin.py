from django.contrib import admin
from .models import FactOfExecution, Hours
from django.contrib.auth.models import User


@admin.register(FactOfExecution)
class FactOfExecutionAdmin(admin.ModelAdmin):
    list_display = ['completed', 'spent', 'user']
    exclude = ['user', 'wages']
    search_fields = ['username']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(request, queryset, search_term)

        if not request.user.is_superuser:
            if request.user.groups.filter(name="Швея").exists():
                queryset = queryset.filter(user=request.user)
        return queryset, may_have_duplicates


# @admin.register(Hours)
# class HoursAdmin(admin.ModelAdmin):
#     pass
