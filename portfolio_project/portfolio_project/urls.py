from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # <-- Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
]

# Add this block to serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
