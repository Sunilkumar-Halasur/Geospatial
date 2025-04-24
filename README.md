TaskApp – Geospatial Django Application
📋 Prerequisites
Ensure the following are installed on your system:

Python 3.8 or higher

pip (Python package manager)

virtualenv (optional, but recommended)

Git (if cloning from a repository)

🚀 Setup Instructions

1. Clone the Repository
git clone git remote add origin https://github.com/Sunilkumar-Halasur/Geospatial.git
cd Spatial

2. Create and Activate Virtual Environment
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Settings
In settings.py, update the following paths:
GEOS_LIBRARY_PATH = 'C:/OSGeo4W/bin/geos_c.dll'
GDAL_LIBRARY_PATH = 'C:/OSGeo4W/bin/gdal310.dll'
Also, make sure to add the above paths to your System Environment Variables.

Update the database configuration in settings.py to match your PostgreSQL/PostGIS setup.

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser (Optional)
python manage.py createsuperuser

7. Start the Development Server
python manage.py runserver

🌐 Access the Application
Main Site: http://127.0.0.1:8000/

API Root: http://127.0.0.1:8000/api/

Point Data: http://127.0.0.1:8000/api/points/

Polygon Data: http://127.0.0.1:8000/api/polygons/

🔁 Perform CRUD Operations via Postman
Use Postman to send HTTP requests to the API endpoints. You can perform the following:

Create: POST JSON data to /api/points/ or /api/polygons/

Read: GET requests to list or retrieve specific items

Update: PATCH or PUT to update existing features

Delete: DELETE to remove a record