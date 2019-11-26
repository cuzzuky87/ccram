from django.urls import path
from .views import Top,Login,Logout

appname = 'accounts'

urlpatterns = [
    path('top/', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(),name='logout'),
]