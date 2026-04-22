from django.urls import path
from . import views

app_name = 'festival'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('dias/', views.dias_view, name='dias'), 
    path('palcos/', views.palcos_view, name='palcos'),
    path('concertos/<int:id>/', views.concerto_view, name='concerto'),
]
