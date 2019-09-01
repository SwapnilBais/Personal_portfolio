from django.urls import path
from .import views


urlpatterns = [
    path('', views.portfolio_page, name='portfolio'),
    path('details', views.portfolio_details, name='portfolio-details')
]