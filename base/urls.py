from django.urls import path, include
from .import views

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',views.HomeView, name= 'home'),
    path('reviewlist/',views.PublicReviewList.as_view(), name= 'reviewlist'),
    path('userreviewlist/',views.ReviewList.as_view(), name= 'userreviewlist'),
    path('detail/<int:pk>/',views.ReviewDetail.as_view(), name= 'detail'),
    path('reviewcreate/',views.ReviewCreate.as_view(), name= 'reviewcreate'),
    path('update/<int:pk>/',views.ReviewUpdate.as_view(), name= 'update'),
    path('delete/<int:pk>/',views.ReviewDelete.as_view(), name= 'delete'),
    path('login/',views.CustomLogin.as_view(), name= 'login'),
    path('logout/',views.LogoutView.as_view(next_page='login'), name= 'logout'),
    path('register/',views.RegisterPage.as_view(),name='register'),
    path('create-location/',views.create_location,name='create_location'),
]