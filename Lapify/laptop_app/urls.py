from django.urls import path

from .views import add_view, show_view, update_view, delete_view, home_view, faq_view, contact_view,privacy_view,terms_view,testimonials_view,career_view,shop_stock_user_see_view

urlpatterns=[
    path("add/",add_view,name='add'),
    path("show/",show_view,name='show'),
    path("update/<int:id>/",update_view,name='update'),
    path("delete/<int:id>/",delete_view,name='delete'),
    path("",home_view,name='home'),
    path("faq/",faq_view,name='faq'),
    path("contact/",contact_view,name='contact'),
    path("privacy/",privacy_view,name='privacy'),
    path("terms/",terms_view,name='terms'),
    path("testimonials/",testimonials_view, name="testimonials"),
    path("career/",career_view,name='career'),
    path('usersee/',shop_stock_user_see_view,name='usersee')


]