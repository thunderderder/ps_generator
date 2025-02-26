import os
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

# Add frontend and backend directories to Python path
frontend_dir = project_root / "frontend"
backend_dir = project_root / "backend"
sys.path.append(str(frontend_dir))
sys.path.append(str(backend_dir))

# Set environment variables from Streamlit secrets
import streamlit as st

if "OPENAI_API_KEY" in st.secrets:
    os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
if "DEEPSEEK_API_KEY" in st.secrets:
    os.environ["DEEPSEEK_API_KEY"] = st.secrets["DEEPSEEK_API_KEY"]
    
# Set API base URL from secrets or use default
api_base_url = st.secrets.get("API_BASE_URL", "http://localhost:8000")
os.environ["API_BASE_URL"] = api_base_url

# Import and run the frontend app
from frontend.app import *

# Note: The backend server (main.py) should be running separately
# You can start it with: uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 