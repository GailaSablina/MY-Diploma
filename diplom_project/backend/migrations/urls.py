from django.urls import path
from .views import PersonAPIViews
from .import views

urlpatterns = [
   path('', views.index, name='index'),
   path('names', PersonAPIViews.as_view()),
]