from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('', views.index,name='index'),
        
    path('create_post/', views.create_post,name='create_post'),
    path('udash/', views.dashboard,name='dashboard'),
    path('edit/<rid>/', views.edit,name='edit'),
    path('delete/<rid>/', views.delete,name='delete'),
    path('catfilter/<catid>/', views.catfilter,name='catfilter'),
    path('actfilter/<actid>/', views.actfilter,name='actfilter'),
    path('register/', views.user_register,name='register'),
    path('login/', views.user_login,name='login'),
    path('logout/', views.user_logout,name='logout'),
    path('readmore/<rid>', views.readMore,name='readmore'),
    
    # path('category/', views.category,name='category'),
    # # path('search_result/', views.search_result,name='search_result'),
    # path('single_post/', views.single_post,name='single_post'),
]
