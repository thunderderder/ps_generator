import os
import sys
from pathlib import Path

# Add the frontend directory to Python path
frontend_dir = Path(__file__).parent / "frontend"
sys.path.append(str(frontend_dir))

# Import and run the Streamlit app
from app import *

# Set environment variables for deployment
os.environ.setdefault("API_BASE_URL", "https://your-backend-api-url.com")  # Replace with your actual backend API URL 