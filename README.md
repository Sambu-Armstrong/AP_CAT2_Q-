# AP_CAT2_Q1
Sambu Armstrong
168205
BBIT 2.2C

# Django E-Commerce Project

This project demonstrates a simple e-commerce application with Django, focusing on data relationships between models (Customer and Order).

## Installation

1. Clone the Repository


2. **Create a Virtual Environment**

    Run the following on git bash:

    ```sh
    python -m venv .venv
    source .venv/Scripts/Activate
    ```

3. **Install Django using pip**

    ```sh
    pip install django
    ```

4. **Navigate to `myproject` Directory**

    Run on gitbash:

    ```sh
    cd myproject
    ```

5. **Apply Migrations**

    Run on gitbash:

    ```sh
    python manage.py migrate
    ```

## Running the Project

1. **Start the Development Server**

    Run on gitbash:

    ```sh
    python manage.py runserver
    ```

2. **Access the Project**

    Open your browser and navigate to [http://127.0.0.1:8000]

## Creating a Superuser

1. **Create a Superuser**

    Run on gitbash:

    ```sh
    python manage.py createsuperuser
    ```

    Follow the prompts to set up a username, email, and password for the superuser account.

## Adding Customers and Orders via Admin Interface

1. **Access the Admin Interface**

    Open your browser and navigate to [http://127.0.0.1:8000/admin]

2. **Log In with Superuser Credentials**

    Use the superuser credentials you created.

3. **Add a New Customer**

    - In the admin dashboard, click on the `Customers` link.
    - Click on the `Add Customer` button.
    - Fill in the `Name` and `Email` fields.
    - Click on the `Save` button.

4. **Add an Order for a Customer**

    - In the admin dashboard, click on the `Orders` link.
    - Click on the `Add Order` button.
    - Fill in the `Order Date` and `Total Amount` fields.
    - In the `Customer` dropdown, select the customer you created earlier.
    - Click on the `Save` button.

5. **View customers list**
    navigate to [http://127.0.0.1:8000/] and click on the `view customer` button 

## Models

### Customer Model

- **Fields**:
    - `name` (CharField): The name of the customer
    - `email` (EmailField): The email address of the customer

### Order Model

- **Fields**:
    - `order_date` (DateTimeField): The date and time when the order was placed
    - `total_amount` (DecimalField): The total amount of the order
    - `customer` (ForeignKey): Foreign key to the Customer model
