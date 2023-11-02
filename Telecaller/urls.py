from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   
    path('TC_dashbord',views.TC_dashbord,name='TC_dashbord'),
    path('TC_current_clients',views.TC_current_clients,name='TC_current_clients'),
    path('TC_current_clients_details',views.TC_current_clients_details,name='TC_current_clients_details'),
    

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)