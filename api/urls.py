from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
	path('key-list/', views.keyList, name="key-list"),
	path('key-detail/<str:pk>/', views.keyDetail, name="key-detail"),
	path('key-create/', views.keyCreate, name="key-create"),
	#path('key-update/<str:pk>/', views.keyUpdate, name="key-update"),
	path('key-delete/<str:pk>/', views.keyDelete, name="key-delete"),
]