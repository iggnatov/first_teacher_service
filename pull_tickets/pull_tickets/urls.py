from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tickets/', include('tickets.urls')),
    path('participants/', include('participants.urls')),
    path('admin/', admin.site.urls),
]
