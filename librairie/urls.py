from django.urls import path

from . import views

app_name ='store'
urlpatterns = [
    path('listing/', views.listing, name='listing'),
    path('<int:book_id>/', views.detail, name='detail'),
    path('search', views.search, name='search'),
    path('', views.index, name="index"),
]
