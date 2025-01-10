from django.urls import path
from .views import home_page_view
from .views import ReviewListView, ReviewDetailView, ReviewCreateView, ReviewUpdateView, ReviewDeleteView

urlpatterns = [
    path('', home_page_view, name='homepage'),  # Homepage URL
    path('reviews/', ReviewListView.as_view(), name='review_list'),  # Add this line
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),
    path('review/new/', ReviewCreateView.as_view(), name='review_create'),
    path('review/<int:pk>/edit/', ReviewUpdateView.as_view(), name='review_update'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='review_delete'),
]