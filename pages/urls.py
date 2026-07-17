from django.urls import path
from . import urls

urlpatterns=[
    path('<slug:slug>/', views.page_detail, name = 'page_detail')
]