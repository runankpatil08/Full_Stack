from django.urls import path

from .views import add_view,show_view,update_view,delete_view


urlpatterns=[
    path("add/",add_view,name='add'),
    path("show/",show_view,name='show'),
    path("update/<int:id>/",update_view,name='update'),
    path("delete/<int:id>/",delete_view,name='delete')
]