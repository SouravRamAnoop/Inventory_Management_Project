#Inventory Management Project

This project uses REST API built with Django and PostgreSQL to manage an inventory system for a small e-commerce application. 
The API allows basic CRUD operations for managing products, categories, and orders. 
It uses Django REST Framework (DRF) to handle API requests, and PostgreSQL as the database.

#Features

- Add, view, update, and delete product categories.
- Add, view, update, and delete products.
- Place, view, and manage orders with multiple products.
- Calculate total price of orders based on product prices and quantities.
- Reduce product stock when an order is placed.


#Steps to Set Up

1.Clone the repository:

   Clone this repository to your local machine using the following command:

   - git clone https://github.com/SouravRamAnoop/Inventory_Management_Project.git
   - cd Inventory-Management-Project


2.Set Up Python Virtual Environment:

   set up a virtual environment to manage project dependencies. To create and activate the virtual environment, run:

   - python -m venv venv
   
   For activating virtual environment

   On Windows:
   venv\Scripts\activate

   On Linux/Macos:
   source venv/bin/activate


3.Install Project Dependencies

   Once your virtual environment is activated, install the required Python dependencies:
   
   - pip install -r requirements.txt

   Alternatively, you can install the dependencies manually:

   - Python (version 3.x)
   - Django
   - Django REST Framework
   - psycopg2 (PostgreSQL adapter for Python)
   - PostgreSQL


4.Set Up PostgreSQL Database

   You need PostgreSQL to store data for your project. You can either use the command line or pgAdmin (a GUI tool).

   Option 1: Install PostgreSQL via Command Line

   Create a database by running the following in the psql command line:
   
   - psql -U postgres
   - CREATE DATABASE database_name;

   OR
   
   Option 2: Install PostgreSQL via pgAdmin (Graphical Tool)

   Download and install pgAdmin during PostgreSQL installation.
   In pgAdmin, create a new database .


   - Update the Django settings in settings.py:
   
      DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_database_name',
           'USER': 'postgres',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }


5.Apply Database Migrations

   Create migration files for the models

   - python manage.py makemigrations
   
   Apply migrations to the database

   - python manage.py migrate


6.Create a Superuser 

   For creating superuser 

   - python manage.py createsuperuser


7.Run the Development Server

   - python manage.py runserver


8.Access the API
   
   Once the server is running, you can access the API via the following endpoints:

   API Endpoints

   Category Endpoints
   - POST /api/categories/: Create a new category
   - GET /api/categories/: List all categories
   - GET /api/categories/{id}/: Retrieve details of a specific category
   - PUT /api/categories/{id}/: Update a category
   - DELETE /api/categories/{id}/: Delete a category

   Product Endpoints
   - POST /api/products/: Add a new product
   - GET /api/products/: List all products
   - GET /api/products/{id}/: Retrieve details of a specific product
   - PUT /api/products/{id}/: Update a product
   - DELETE /api/products/{id}/: Delete a product

   Order Endpoints
   - POST /api/orders/: Place a new order (includes product IDs and quantities)
   - GET /api/orders/: List all orders
   - GET /api/orders/{id}/: Retrieve details of a specific order
   

9.Running Tests

   You can run the unit tests to ensure that everything is working correctly:

   - python manage.py test


   
