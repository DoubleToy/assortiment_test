from django.contrib.admin import ModelAdmin, register, StackedInline, TabularInline
from django.contrib import admin
from .models import Warehouse, UpFile
from storekeeper import models
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from django.http import HttpResponseRedirect
from django.urls import re_path, path
from django.shortcuts import render


class WarehouseAdmin(admin.TabularInline):
    model = Warehouse
    fields = ('name', 'quantity')
    extra = 3


# class WarehouseResource(resources.ModelResource):
#     name = fields.Field(attribute="name", column_name="наименование, характеристика, сорт, артикул товара")
#     documentNumber = fields.Field(attribute="documentNumber", column_name="Номер документа")
#
#     def get_instance(self, instance_loader, row):
#         return False
#
#     class Meta:
#         model = Warehouse
#         skip_unchanged = True
#         report_skipped = False
#         fields = ('name', 'characteristic', 'sort', 'article', 'unit', 'quantity', 'price', 'priceNDS',
#                   'documentNumber')
#         exclude = ('id', 'order')
#         import_id_fields = ["name", "documentNumber"]

# @register(Warehouse)
# class WarehouseAdminPanel(admin.ModelAdmin):
#     list_display = ('id', 'dateArrival', 'client', 'documentNumber', 'dateCompilation', 'image_tag')

    # resource_class = WarehouseResource
    # change_list_template = 'admin/model_change_list.html'

    # def get_urls(self):
    #     urls = super(WarehouseAdminPanel, self).get_urls()
    #     custom_urls = [
    #         path('post/', self.process_import, name='process_import'), ]
    #     return custom_urls + urls
    #
    # def process_import(self, request):
    #     return HttpResponseRedirect("../")


# admin.site.register(Warehouse, WarehouseAdminPanel)


# admin.site.register(models.UpFile)
