from django.urls import path
from mainapp.views import *


urlpatterns = [
    path('',index, name='index_url' ),
    path('word',word, name='word_url' ),
]
