from django.contrib.admin import ModelAdmin, register, TabularInline
from django.contrib import admin
from .models import TypeProduct, Operation, TechnicalProcess, SelectionOperation, Expenses, Order, OrderAny, Workload
from seamstress.models import Hours
from django import forms
from django.db import models


@register(TypeProduct)
class TypeProductAdmin(ModelAdmin):
    list_display = ['type_products', 'type_work', 'quantity', 'period']
    autocomplete_fields = ['user']
    # exclude = ['hour']

    def save_model(self, request, obj, form, change):
        field_name = 'hours'
        hour = Hours.objects.first()
        field_object = Hours._meta.get_field(field_name)
        field_value = field_object.value_from_object(hour)
        obj.period = obj.time / field_value
        super().save_model(request, obj, form, change)


@register(Operation)
class OperationAdmin(ModelAdmin):
    list_display = ('name', 'time', 'spent')


class SelectionOperationAdmin(admin.TabularInline):
    model = SelectionOperation
    fields = ('number', 'operation', 'time', 'seamstress')
    extra = 3


@register(TechnicalProcess)
class TechnicalProcessAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [SelectionOperationAdmin]

    class Media:
        js = ("technologist/js/controller1.js",)


class ExpensesTabular(admin.TabularInline):
    model = Expenses
    fields = ('name', 'waste', 'unit', 'total')
    extra = 3


class OrderAnyTabular(admin.TabularInline):
    model = OrderAny
    fields = ('body', 'quantity', 'price', 'cost', 'totalQ', 'totalC')


@register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [OrderAnyTabular, ExpensesTabular]
    # form = OrderFormAdmin


@register(Workload)
class WorkLoadAdmin(admin.ModelAdmin):
    list_display = ('ser', 'load')
