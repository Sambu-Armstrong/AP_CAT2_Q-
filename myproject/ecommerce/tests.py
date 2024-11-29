from django.test import TestCase
from .models import Customer, Order
from datetime import datetime

class CustomerOrderModelTests(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(name="John Doe", email="john.doe@example.com")
        self.order = Order.objects.create(customer=self.customer, order_date=datetime.now(), total_amount=100.00)

    def test_customer_creation(self):
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(customer.email, "john.doe@example.com")

    def test_order_creation(self):
        orders = Order.objects.filter(customer=self.customer)
        self.assertEqual(orders.count(), 1)
        self.assertEqual(orders[0].total_amount, 100.00)

    def test_customer_orders(self):
        customer = Customer.objects.get(name="John Doe")
        orders = customer.order_set.all()
        self.assertEqual(orders.count(), 1)
        self.assertEqual(orders[0].total_amount, 100.00)

