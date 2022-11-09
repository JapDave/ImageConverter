from django.urls import path
from .views import *

urlpatterns = [
    path('',ImageConveterView.as_view(),name='image-converter'),
]
