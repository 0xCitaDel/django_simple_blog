from django.urls import path
from .views import (
        ListBlogView,
        SingleBlogView, 
        # edit_article,
        # update_article,
        delete_article,
        MyView,
        EditBlogView,
        UpdateBlogView,
        BlogViewAuth,
        BlogViewRegister,
        BlogViewLogOut,
        )

urlpatterns = [
    path('', ListBlogView.as_view(), name='main'),
    path('post/<int:pk>', SingleBlogView.as_view(), name='single_post'),
    path('edit/', EditBlogView.as_view(), name='edit_article'),
    path('update/<int:pk>', UpdateBlogView.as_view(), name='update_article'),
    path('delete/<int:pk>', delete_article, name='delete_article'),
    path('test/<str:get>', MyView.as_view(), name='test'),
    path('login', BlogViewAuth.as_view(), name='login_page'),
    path('register', BlogViewRegister.as_view(), name='register_page'),
    path('logout', BlogViewLogOut.as_view(), name='logout_page'),
]