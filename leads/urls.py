from django.contrib import admin
from django.urls import path, include
from leads import views 

app_name='leads'
urlpatterns = [
    path('lead-list/', views.LeadListView.as_view(), name='lead-list'),
]
