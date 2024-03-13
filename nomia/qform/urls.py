from django.urls import path

from . import views


urlpatterns = [
    path('', views.first_form_view, name='first_form_view'),
    path('second_form', views.second_form_view, name='second_form_view'),
    path('success', views.success_view, name='success_view')
]
