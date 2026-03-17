# Import Flask framework to create the web application
from flask import Flask

# Import os module to read environment variables
import os

# Create Flask application instance
app = Flask(__name__)

# Define API endpoint for the root URL "/"
@app.route("/")
def home():
    """
    This function reads environment variables and returns them as JSON.
    
    In K8s:
    - APP_ENV and APP_COLOR will come from a ConfigMap
    - DB_USER and DB_PASSWORD will come from a Secret
    """
    
    return {
        # Read application environment (e.g., dev, prod) from ConfigMap
        "APP_ENV": os.getenv("APP_ENV"),

        # Read application color configuration from ConfigMap
        "APP_COLOR": os.getenv("APP_COLOR"),

        # Read database username from K8s Secret
        "DB_USER": os.getenv("DB_USER"),

        # Read database password from K8s Secret
        "DB_PASSWORD": os.getenv("DB_PASSWORD")
    }

# Start the Flask application
# host="0.0.0.0" allows the app to accept external connections (needed for Docker/K8s)
# port=5000 is the port where the application will run
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)