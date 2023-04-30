from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('create/', KoanCreateView.as_view(success_url='/create')),
    path('api/koans/', views.get_all_koans),
    path('api/koans/<int:id>/', views.get_koan),
    path('api/koans/count/', views.koans_count),
    path('api/koans/create/', views.create_koan),
]