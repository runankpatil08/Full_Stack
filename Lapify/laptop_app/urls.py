from django.urls import path

from .views import add_view,show_view


urlpatterns=[
    path("add/",add_view,name='add'),
    path("show/",show_view,name='show')
]