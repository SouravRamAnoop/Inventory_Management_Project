from rest_framework import serializers

from .models import Category, Product, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'category']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be a positive value")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative")
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def validate_quantity(self, value):
        if value <= 0:
            raise serializers.ValidationError("Quantity must be a positive integer.")
        return value


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'order_items', 'total_price']

    def validate(self, data):
        for item in data['order_items']:
            product = item['product']
            quantity = item['quantity']
            if product.stock < quantity:
                raise serializers.ValidationError(f"Not enough stock for product {product.name}.")
        return data

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            product.reduce_stock(quantity)
            order_item = OrderItem.objects.create(order=order, product=product, quantity=quantity)

        order.calculate_total_price()
        return order
