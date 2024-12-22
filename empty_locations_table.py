import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vrp_project.settings')
django.setup()

from vrp_app.models import Location, Vehicle

def empty_tables():
    Location.objects.all().delete()
    print("Successfully emptied the Location table.")

if __name__ == "__main__":
    empty_tables() 