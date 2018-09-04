from . import views
from django.urls import path



urlpatterns = [
    path('create',views.post_create, name='post_create'),
    path('post/<int:pk>/',views.post_detail,name='post_details'),
    path('',views.post_list,name='post_list'),
    path('update',views.post_update),
    path('delete',views.post_delete),
]