from django.urls import path, include

urlpatterns = [
    path('', include('vrp_app.urls')),  # Include app URLs
]
