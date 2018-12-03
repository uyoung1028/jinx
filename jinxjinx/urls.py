from django.urls import path
from . import views

app_name = 'jinxjinx'

urlpatterns = [
    # path('', views.PostList.as_view(), name='list'),
    path('jinxbox/', views.jinxbox_view.as_view(), name='jinxbox_list'),
    path('data_list/', views.DataList.as_view(), name="data_list"),
    
    path('category/', views.CategoryList.as_view(), name="category"),
    path('category_noun/', views.category_noun, name="category_noun"),
    path('noun/', views.NounList.as_view(), name="noun"),
    path('noun_verb/', views.noun_verb, name="noun_verb"),
    
    path('sentence_create/', views.SentenceCreate.as_view(), name="sentence_create"),
    path('sentence/', views.SentenceList.as_view(), name='sentence_list'),
    
    path('<pk>/',views.SentenceDetail.as_view(),name='detail'),
    path('<int:pk>/comments/',views.CommentCreate.as_view(),name="comment_create"),
    path('<int:pk>/usersentence/',views.UserSentenceDetail.as_view(),name="usersentence_detail"),
    

    
    # path('/', views..as_view(), name='list'),




]



    # path('/', views.List.as_view(), name ='list'),
    # path('new/', views.Create.as_view(), name='create'),
    # path('<int:pk>/', views.Detail.as_view(), name='detail'),
    # path('<int:pk>/delete/', views.Delete.as_view(), name='delete'),
    # path('<int:pk>/edit/', views.Update.as_view(), name='edit'),
    
    # path('<int:question_id>/answer_create/', views.Answer_Create.as_view(), name='answer_create'),
    # path('<int:question_id>/answer_delete/', views.Answer_Delete.as_view(), name='answer_delete'), 
    # path('<int:question_id>/answer_update/', views.Answer_Update.as_view(), name='answer_update'), 