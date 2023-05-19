from django.urls import path

from . import views

urlpatterns = [

    path('', views.list_all_notes, name='notes'),
    path('get_note/<str:pk>/', views.get_note, name='get-note'),
    path('create-notes', views.create_notes, name='create-notes'),
    path('update-notes/<str:pk>/', views.update_notes, name='update-notes'),
    path('delete-notes/<str:pk>/', views.delete_notes, name='delete-notes'),
]