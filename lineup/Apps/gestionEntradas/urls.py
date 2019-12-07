from django.urls import path
from . import views

urlpatterns=[
	path('',views.ArtistaList.as_view(),name='index'),
    path('lineup/',views.EventNumbers.as_view(),name='lineup'),
	path('stages/',views.stages,name='stages'),
]
