from django.contrib import admin
from django.urls import path

from .views import (
    EnglishWordDetail,
    EnglishWordList, 
    EnglishWordCreate, 
    EnglishWordDelete,
    EnglishWordUpdate,
    check_count_func,)


urlpatterns = [
    path("list/", EnglishWordList.as_view(), name='list'),
    path('detail/<int:pk>', EnglishWordDetail.as_view(), name='detail'),
    path('create/', EnglishWordCreate.as_view(), name='create'),
    path('delete/<int:pk>', EnglishWordDelete.as_view(), name='delete'),
    path('update/<int:pk>', EnglishWordUpdate.as_view(), name='update'),
    path('count/<int:pk>', check_count_func, name='count'),
]