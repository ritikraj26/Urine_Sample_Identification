from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='image_upload'),
    #   path('results/', views.view_results, name='view_results')
]