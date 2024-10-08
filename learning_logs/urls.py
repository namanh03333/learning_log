'''Define URLpattern for learning_logs'''
from django.urls import path 
from . import views

app_name = 'learning_logs'
urlpatterns = [
    #homepage
    path('',views.index,name='index'),
    path('topic/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
]