from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.register_user, name='signup'),
    path('profile/', views.profile_view, name='profile_view'),
    path('logout/', views.logout_user, name='logout'),
    path('create_blog/',views.create_blog, name = 'create_blog'),
    path('my_blogs/',views.my_blogs, name = 'my_blogs'),
    path('all_blogs/',views.all_blogs, name = 'all_blogs'),
    path('edit_blog/<int:id>',views.edit_blog,name='edit_blog'),
    path('delete_blog/<int:id>',views.delete_blog,name='delete_blog'),
    path('blog_detail/<int:id>',views.blog_detail,name='blog_detail'),
]
