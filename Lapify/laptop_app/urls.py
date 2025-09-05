from django.urls import path

from .views import add_view, show_view, update_view, delete_view, home_view, faq_view, contact_view

urlpatterns=[
    path("add/",add_view,name='add'),
    path("show/",show_view,name='show'),
    path("update/<int:id>/",update_view,name='update'),
    path("delete/<int:id>/",delete_view,name='delete'),
    path("",home_view,name='home'),
    path("faq/",faq_view,name='faq'),
    path("contact/",contact_view,name='contact'),

]