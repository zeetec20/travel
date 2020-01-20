from django.urls import path

from .views import Index, DestinationDetail

app_name = 'destination'
urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('<str:country>', Index.as_view(), name="index_country"),
    path('<str:country>/<str:name>', DestinationDetail.as_view(), name='destination_detail')
]
