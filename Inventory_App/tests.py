from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Product, Order, OrderItem
from decimal import Decimal


class CategoryModelTest(TestCase):
    def test_create_category(self):
        category = Category.objects.create(name="Electronics", description="Gadgets")
        self.assertEqual(category.name, "Electronics")
        self.assertEqual(category.description, "Gadgets")


class ProductModelTest(TestCase):
    def test_create_product(self):
        category = Category.objects.create(name="Electronics", description="Gadgets")
        product = Product.objects.create(
            name="Smartphone", price=699.99, stock=50, category=category
        )
        self.assertEqual(product.name, "Smartphone")
        self.assertEqual(product.price, 699.99)
        self.assertEqual(product.stock, 50)


class OrderModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics", description="Gadgets")
        self.product_1 = Product.objects.create(name="Smartphone", price=Decimal('699.99'), stock=50,
                                                category=self.category)
        self.product_2 = Product.objects.create(name="Laptop", price=Decimal('999.99'), stock=30,
                                                category=self.category)

    def test_create_order(self):
        order = Order.objects.create()
        OrderItem.objects.create(order=order, product=self.product_1, quantity=2)
        OrderItem.objects.create(order=order, product=self.product_2, quantity=3)
        order.calculate_total_price()

        expected_total_price = (Decimal('2') * self.product_1.price) + (Decimal('3') * self.product_2.price)
        self.assertEqual(order.total_price, expected_total_price)

        self.assertEqual(order.order_items.count(), 2)


class CategoryApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Books", description="All kinds of books")

    def test_create_category_api(self):
        url = '/api/categories/'
        data = {'name': 'Furniture', 'description': 'Furniture items'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_category_api(self):
        url = f'/api/categories/{self.category.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_categories_api(self):
        url = '/api/categories/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProductApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(name="Electronics", description="Gadgets")
        self.product = Product.objects.create(name="Smartphone", price=699.99, stock=50, category=self.category)

    def test_create_product_api(self):
        url = '/api/products/'
        data = {
            'name': 'Laptop',
            'description': 'Electronics item',
            'price': 39999.99,
            'stock': 20,
            'category': self.category.name
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_api(self):
        url = f'/api/products/{self.product.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_products_api(self):
        url = '/api/products/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
