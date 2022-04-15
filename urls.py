from django.urls import path
from . import views
from .views import CreateFolderView

app_name = 'guide'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', CreateFolderView.as_view(), name='create')
]
