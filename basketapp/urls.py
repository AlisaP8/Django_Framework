from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket'),
    path('add/<int:pk>/', basketapp.add, name='add'),
    path('remove/<int:pk>/', basketapp.remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.edit, name='edit'),

]
