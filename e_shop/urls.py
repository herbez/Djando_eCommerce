from . import views
from django.urls import path


urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login_user, name='login'),
    path('register/',views.register_user, name='register'),
    path('logout/',views.logout_user, name='logout'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('product/<int:pk>', views.product, name='product'),
    
]