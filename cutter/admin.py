from django.contrib.admin import ModelAdmin, register
from django.contrib.admin.templatetags import admin_modify

from .models import DailyProductionPlan, WorkPerformed, Order, TecOperation, TypeMaterials, WorkPerformedCost

from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget
from storekeeper.admin import WarehouseAdmin


@register(DailyProductionPlan)
class DailyProductAdmin(ImportExportActionModelAdmin):
    list_display = (
        'date', 'number', 'name', 'metric', 'flooring', 'remains', 'defects', 'quantity', 'spent')

    class Meta:
        model = DailyProductionPlan
        skip_unchanged = True
        report_skipped = False
        fields = (
            'date', 'number', 'cloth', 'metric', 'flooring', 'remains', 'visible_defects', 'defects', 'quantity',
            'spent',
            'image_tag')


@register(TypeMaterials)
class TypeMaterialsAdmin(ModelAdmin):
    list_display = ['feedstock']


@register(WorkPerformed)
class WorkPerformedAdmin(ModelAdmin):
    list_display = ('size', 'spent', 'image_tag')
    readonly_fields = ("image_tag",)
    change_form_template = 'admin/model_change_form.html'


@register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('name', 'quantity')
    inlines = [WarehouseAdmin, ]


@register(TecOperation)
class TecOperationAdmin(ModelAdmin):
    list_display = ('name', 'time')


@register(WorkPerformedCost)
class WorkPerformedCostAdmin(ModelAdmin):
    list_display = ('size', 'cost')
