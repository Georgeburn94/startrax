from django.urls import path
from .views import home_page_view, register, AlbumCreateView
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', ReviewListView.as_view(), name='review_list'),  # Add this line
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
    path('register/', register, name='register'),  # Add this line
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Add this line
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Add this line
    path('album/new/', AlbumCreateView.as_view(), name='album_create'),  # Add this line
    
]