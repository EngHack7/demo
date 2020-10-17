from django.urls import path
from .views import (Home , Contact , About , Stars)

from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
    path('' , Home ,  name = 'home' ),
    path('contact/' , Contact , name = 'contact'),
    path('about/' , About , name = 'about'),
    path('stars/' , Stars , name='stars')
    
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
