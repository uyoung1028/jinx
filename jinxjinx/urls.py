from django.urls import path
from . import views

app_name = 'jinxjinx'

urlpatterns = [
    # path('', views.PostList.as_view(), name='list'),
    path('jinxbox/', views.jinxbox_view.as_view(), name='list'),
    path('data_list/',views.DataList.as_view(),name="data_list"),
    
    path('category/',views.CategoryList.as_view(),name="category"),
    path('category_noun/',views.category_noun,name="category_noun"),
    path('noun/',views.NounList.as_view(),name="noun"),
    path('noun_verb/',views.noun_verb,name="noun_verb"),
    
    path('sentence_create/',views.SentenceCreate.as_view(),name="sentence_create"),
    path('sentence/', views.SentenceList.as_view(),name='sentence_list'),
]