from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


admin.site.register(Jinx)
admin.site.register(Sentence)


@admin.register(Data)
@admin.register(Category)
@admin.register(Noun)
@admin.register(Verb)
@admin.register(Comment)
@admin.register(UserSentence)
# @admin.register(Date)
# @admin.register(Weather)
# @admin.register(Feeling)
# @admin.register(Result)

class DataAdmin(ImportExportModelAdmin):
    pass