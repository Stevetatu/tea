from django.urls import path
from . import views


urlpatterns = [
    path('teas/', views.tea_list, name='teas_list'),
    path('tea-blog/', views.tea_blog, name='tea_blog'),
]