from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Jinx, Data, Sentence


admin.site.register(Jinx)
admin.site.register(Sentence)

@admin.register(Data)
class DataAdmin(ImportExportModelAdmin):
    pass