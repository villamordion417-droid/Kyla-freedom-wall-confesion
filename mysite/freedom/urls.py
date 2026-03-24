from django.urls import path
from django.contrib import admin
from django.contrib.auth.models import User # Add this

# This tiny function creates the admin automatically
def create_admin():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword123')

create_admin() # Run it immediately

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... keep your other paths here ...
]