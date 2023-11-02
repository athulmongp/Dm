from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
   
    #  Admin Module --------------------------------

    path('Admin-Dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('Admin-Logout',views.admin_logout,name='admin_logout'),

    #Approve ----------------------------

    path('Admin-Login-Approve\<int:pk>',views.admin_login_approve,name='admin_login_approve'),
    path('Admin-Login-Reject\<int:pk>',views.admin_login_reject,name='admin_login_reject'),

    # Departmet ---------------------------------
    
    path('Admin-Department',views.admin_department,name='admin_department'),

    # Designation -------------------------------

    path('Admin-Designations',views.admin_designation,name='admin_designation'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)