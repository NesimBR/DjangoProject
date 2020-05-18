from django.urls import path

from . import views

urlpatterns = [
    # ex: /note/
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('comments/',views.comments, name='comments'),
    path('deletecomment/<int:id>', views.deletecomment, name='deletecomment'),
    path('addnote/', views.addnote, name='addnote'),
    path('notes/', views.notes, name='notes'),
    path('notedelete/<int:id>', views.notedelete, name='notedelete'),
    path('noteEdit/<int:id>', views.noteEdit, name='noteEdit'),
    path('noteaddimage/<int:id>', views.noteaddimage, name='noteaddimage'),

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),

]