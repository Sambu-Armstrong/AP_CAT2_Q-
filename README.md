# AP_CAT2_Q1
Sambu Armstrong
168205
BBIT 2.2C

# Django E-Commerce Project

This project demonstrates a simple e-commerce application with Django, focusing on data relationships between models (Customer and Order).


## Installation

1. Clone the Repository


2. **Create a Virtual Environment**

    python -m venv .venv
    source .venv/bin/activate    # on git bash

3. **Apply Migrations**
    
    python manage.py migrate
    


## Running the Project

1. **Start the Development Server**

   
    python manage.py runserver
    

2. **Access the Project** 
    Open your browser and navigate to [http://127.0.0.1:8000] , 



    **Models**

## Customer Model
        Fields:

            name (CharField): The name of the customer
            email (EmailField): The email address of the customer

## Order Model
        Fields:

            order_date (DateTimeField): The date and time when the order was placed
            total_amount (DecimalField): The total amount of the order
            customer (ForeignKey): Foreign key to the Customer model

In case of any  changes to the models do:

    python manage.py makemigrations  #to create migration
    python manage.py migrate # to apply the migrations

