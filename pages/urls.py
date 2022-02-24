from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('graph/lustre/<str:fs>/mdt.json', views.graph_lustre_mdt),
    path('graph/lustre/<str:fs>/ost.json', views.graph_lustre_ost),
]
