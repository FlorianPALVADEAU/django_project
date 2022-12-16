from django.urls import path
from . import views
 
app_name = 'app1'
urlpatterns = [
    path('', views.all_images, name='index'),
    path('create', views.create_view, name='create'),
    path('show/<id>', views.show_single, name="show"),
    path('update/<id>', views.update_view, name="update"),
    path('delete/<id>', views.delete, name="delete"),
]