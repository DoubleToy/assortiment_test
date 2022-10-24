from django.contrib.admin import ModelAdmin, register
from django.contrib import admin
from .models import TypeOfWork, Salary


@register(TypeOfWork)
class TypeOfWorkAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')


@register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('name', 'wages')
    change_list_template = 'admin/model_pay_list.html'
