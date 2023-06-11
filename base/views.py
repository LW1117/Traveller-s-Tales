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
        public_reviews = context['review'].filter(public=True)
        context['review'] = public_reviews

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['review'] = context['review'].filter(
                title__contains=search_input)

        context['search_input'] = search_input
        return context

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
    fields = ['title','description','public','location','linktolocation']
    success_url = reverse_lazy('userreviewlist')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ReviewCreate,self).form_valid(form)
    
class ReviewUpdate(LoginRequiredMixin,UpdateView):
    model = Review
    fields = ['title','description','public','location','linktolocation','rating']
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