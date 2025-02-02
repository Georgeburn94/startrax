from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Review, Album  
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('review_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def home_page_view(request):
    if request.user.is_authenticated:
        user_reviews = Review.objects.filter(user=request.user)  # Filter reviews by logged-in user
    else:
        user_reviews = None
    return render(request, 'base.html', {'user_reviews': user_reviews})

class ReviewListView(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'user_reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['albums'] = Album.objects.filter(user=self.request.user)
        else:
            context['albums'] = Album.objects.none()
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Review.objects.filter(user=self.request.user)
        return Review.objects.none()

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'review_detail.html'

class ReviewCreateView(PermissionRequiredMixin, CreateView):
    model = Review
    fields = ['album', 'star_rating', 'note']
    template_name = 'review_form.html'
    success_url = reverse_lazy('review_list')
    permission_required = 'startrax.add_review'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Review created successfully.')
        return super().form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'review_form.html'
    success_url = reverse_lazy('review_list')

    def form_valid(self, form):
        messages.success(self.request, 'Review updated successfully.')
        return super().form_valid(form)

class ReviewDeleteView(PermissionRequiredMixin, DeleteView):
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = reverse_lazy('review_list')
    permission_required = 'startrax.delete_review'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Review deleted successfully.')
        return super().delete(request, *args, **kwargs)

class AlbumCreateView(PermissionRequiredMixin, CreateView):
    model = Album
    fields = ['name', 'year', 'artist']
    template_name = 'album_form.html'
    success_url = reverse_lazy('review_list')
    permission_required = 'startrax.add_album'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Album created successfully.')
        return super().form_valid(form)

class AlbumListView(ListView):
    model = Album
    template_name = 'album_list.html'
    context_object_name = 'albums'

class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('review_list')
    permission_required = 'startrax.delete_album'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Album deleted successfully.')
        return super().delete(request, *args, **kwargs)