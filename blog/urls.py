from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_tag'),
]