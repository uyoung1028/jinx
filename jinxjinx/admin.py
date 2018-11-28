from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Jinx, Data, Sentence, Category, Noun, Verb


admin.site.register(Jinx)
admin.site.register(Sentence)


@admin.register(Data)
@admin.register(Category)
@admin.register(Noun)
@admin.register(Verb)
class DataAdmin(ImportExportModelAdmin):
    pass