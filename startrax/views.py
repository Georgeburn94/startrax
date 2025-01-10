from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review  
from .forms import ReviewForm


# Create your views here.
def home_page_view(request):
    user_reviews = Review.objects.filter(user=request.user)  # Filter reviews by logged-in user
    return render(request, 'homepage.html', {'reviews': user_reviews})

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('review_list')

class ReviewDeleteView(DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = reverse_lazy('review_list')