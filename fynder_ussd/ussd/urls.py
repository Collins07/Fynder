from django.urls import path
from . import views

urlpatterns = [
    path('callback/', views.ussd_callback, name='ussd_callback'),  # Existing URL pattern
    path('', views.ussd_home, name='ussd_home'),  # New URL pattern for `ussd/`
]
