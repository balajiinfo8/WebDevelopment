from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
# from .views import TODOViews

# router = DefaultRouter()
# router.register(r'todo', TODOViews, basename='todo')
#
# urlpatterns = [
#     path('', include(router.urls))
# ]
#
# todolist = TODOViews.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# todo_details = TODOViews.as_view({
#     'get': 'list',
#     'put': 'update',
#     'delete': 'destroy',
# })
#
# urlpatterns = [
#     path('todo/', todolist, name='todolist'),
#     path('todo/<int:pk>', todo_details, name='todo_details')
# ]
# urlpatterns = [
#     path('list/', TODOViews.as_view(), name='list'),
#     path('create/', TODOViews.as_view(), name='create'),
#     path('update/<int:pk>', TODOViews.as_view(), name='update'),
#     path('delete/<int:pk>', TODOViews.as_view(), name='delete')
# ]

# router = DefaultRouter()
# router.register(r'todo',TODOViews,basename='todo')
#
# urlpatterns = [
#     path('',include(router.urls))
# ]

# function views url
from .views import todoviews

urlpatterns = [
    path('todo/', todoviews, name='list'),
    path('todo/<int:pk>', todoviews, name='todo')
]
