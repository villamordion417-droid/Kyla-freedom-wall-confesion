from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.db.utils import OperationalError, ProgrammingError

# The "Free Tier" Superuser Creator
def create_admin_user():
    try:
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword123')
            print("Superuser created successfully!")
    except (OperationalError, ProgrammingError):
        # This prevents the site from crashing if the database isn't ready yet
        pass

create_admin_user()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wall.urls')),
]