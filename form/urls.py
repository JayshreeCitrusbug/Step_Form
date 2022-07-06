from django.urls import path
from . import views   

urlpatterns = [
    path('form/',views.FormView.as_view(),name='main-form'),
    path('form/state',views.SatetData.as_view(), name="state"),
]