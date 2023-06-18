from collections import defaultdict
from django.shortcuts import render, redirect

from .models import Location, Review

from django.contrib.auth import login

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.forms import UserCreationForm

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def HomeView(request):
    context = { Review.user: 'user' }
    return render(request, 'base/home.html', context) # type: ignore

    

class PublicReviewList(ListView):
    model = Review
    context_object_name = 'review'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        reviews = Review.objects.filter(public=True)
        distinct_locations = reviews.order_by().values_list('location', flat=True).distinct()
        
        # Perform case-insensitive distinct filtering in Python
        distinct_locations = [location.upper() for location in distinct_locations]
        distinct_locations = list(set(distinct_locations))
        
        context['locations'] = distinct_locations
        
        return context

class ListOfPublicReviews(ListView):
    model = Review
    template_name = 'base/public_review_list.html'
    context_object_name = 'reviews'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        location = self.kwargs['location']
        context['location'] = location
        return context

    def get_queryset(self):
        location = self.kwargs['location']  # Assumes the URL pattern captures the location
        return Review.objects.filter(location__iexact=location)


class ReviewList(LoginRequiredMixin,ListView):
    model = Review
    template_name = 'base/user_review_list.html'
    context_object_name = 'review'
    user = Review.user
    def superuser_check(self, user):
        return user.is_superuser
    
    def get_context_data(self, **kwargs):
        user=self.request.user
        context = super().get_context_data(**kwargs)
        user_reviews = context['review'].filter(user=self.request.user)
        context['review'] = user_reviews
        context['count'] = user_reviews.filter(public=True).count()
        return context
        
class ReviewDetail(DetailView):
    model = Review
    context_object_name = 'review'
  
    
class ReviewCreate(LoginRequiredMixin,CreateView):
    model = Review
    fields = ['title','description','public','location','image','rating']
    success_url = reverse_lazy('userreviewlist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreate,self).form_valid(form)
    
class ReviewUpdate(LoginRequiredMixin,UpdateView):
    model = Review
    fields = ['title','description','public','location','rating','image']
    success_url = reverse_lazy('userreviewlist')
    
class ReviewDelete(LoginRequiredMixin,DeleteView):
    model = Review
    context_object_name = 'review'
    success_url = reverse_lazy('userreviewlist')

class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    
class CustomLogout(LoginRequiredMixin,LogoutView):
   # template_name = 'base/logout.html'
   # model = Review
   # context_object_name = 'review'
    next_page = ('login')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save() # type: ignore
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)