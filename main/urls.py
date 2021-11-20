from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/logout', views.LogoutApiView.as_view()),
    path('api/login', views.LoginApiView.as_view()),
    path('api/register', views.UserRegisterApiView.as_view()),
    path('api/entities', views.EntitiesApiView.as_view()),
    path('api/entities/<int:id>', views.EntityApiView.as_view()),
    path('api/listing', views.ListingsApiView.as_view()),
    path('api/listing/<int:id>', views.ListingApiView.as_view()),
    path('api/giveaway', views.GiveawaysApiView.as_view()),
    path('api/giveaway/<int:id>', views.GiveawayApiView.as_view())
]