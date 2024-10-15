# chatbot/urls.py
from django.urls import path
from .views import chatbot_response,chat_page

urlpatterns = [
    path('', chat_page, name='chat_page'),  
    path('chat/', chatbot_response, name='chatbot_response'),
]

