from django.contrib import admin
# 현재폴더에 있는 models.py 에서 Post를 추가
from .models import Jinx, Data, Sentence
# 관리자 페이지에 Post 추가
admin.site.register(Jinx)
admin.site.register(Data)
admin.site.register(Sentence)