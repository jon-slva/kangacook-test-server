from django.urls import path
from . import views

urlpatterns = [
    path('apitypes/', views.get_api_types, name='api_types'),
	path('tabledata/', views.get_table_data, name='table_data')
]