from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('mentor/', include('mentor.urls')),
    path('mentee/', include('mentee.urls')),
    path('author/', include('author.urls')),
]
