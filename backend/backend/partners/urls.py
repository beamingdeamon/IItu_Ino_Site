from django.urls import path
from .views import createPartner
from .views import getPartners
from .views import deletePartner
from .views import updatePartner

app_name = "Partners"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('createpartner/', createPartner.as_view()),
    path('getpartners/', getPartners.as_view()),
    path('deletepartner/<int:pk>/', deletePartner.as_view()),
    path('updatepartner/<int:pk>/', updatePartner.as_view()),
]