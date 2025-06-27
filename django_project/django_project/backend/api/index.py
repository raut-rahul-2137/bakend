import os
import sys
from pathlib import Path

# Set up Django environment
sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings_prod')

from django.core.asgi import get_asgi_application

app = get_asgi_application() 