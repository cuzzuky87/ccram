from django.urls import path
from .views import Top,Login,Logout

appname = 'accounts'

urlpatterns = [
    path('top/', Top.as_view(), name='top'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(),name='logout'),
]