from django.urls import path
from . import views

app_name = 'jinxjinx'

urlpatterns = [
    # path('', views.PostList.as_view(), name='list'),
    path('tellme/', views.PostCreate.as_view(), name='create'),
    path('jinxbook/', views.PostList.as_view(), name='list'),
    path('sentence/',views.SentenceList.as_view(),name='sentence'),
    

]