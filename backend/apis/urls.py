from django.urls import path
from .views import *

urlpatterns = [
    path('', DM.as_view(), name='dm')
]
