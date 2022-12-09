from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='myhome'),
    path('about/', AboutPage.as_view(), name='myabout'),
    path('blog/', BlogPage.as_view(), name='myblog'),
    path('new/', CreatePage.as_view(), name='mynew'),
    path('anyname/<int:pk>/', DetailPage.as_view(), name='mydetail'),
    path('anyname/<int:pk>/edit', EditPage.as_view(), name='myedit'),
    path('anyname/<int:pk>/delete', DeletePage.as_view(), name='mydelete'),


]