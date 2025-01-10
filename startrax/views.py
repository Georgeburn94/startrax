from django.shortcuts import render
from .models import Review  

# Create your views here.
def home_page_view(request):
    user_reviews = Review.objects.filter(user=request.user)  # Filter reviews by logged-in user
    return render(request, 'homepage.html', {'reviews': user_reviews})