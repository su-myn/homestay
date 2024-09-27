from django.contrib import admin
from .models import RepairForm, AdhocItemForm, Tag


class RepairFormAdmin(admin.ModelAdmin):
    list_display = ("unit_number", "contractor")
    search_fields = ("unit_number", "contractor")
    list_filter = ("unit_number", "contractor")
    ordering = ("unit_number",)



admin.site.register(RepairForm, RepairFormAdmin)
admin.site.register(AdhocItemForm)
admin.site.register(Tag)

