from django.urls import path

from . import views # added

urlpatterns = [
    path('', views.allblogs, name='allblogs'), # added
    path('<int:blog_id>/', views.detail, name=
    'detail'), #added, takes an id after /blog/ and saves it as blog_id
]
