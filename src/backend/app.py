from flask import Flask, request, jsonify
from awsConfig import SessionLocal, engine, Base, upload_file_to_s3
from models import Product, Order, OrderProduct, OrderStatus
from utils import send_email
from datetime import datetime

app = Flask(__name__)

# Ensure all tables are created
Base.metadata.create_all(bind=engine)

# Product Management
@app.route('/products', methods=['GET', 'POST'])
def handle_products():
    session = SessionLocal()
    if request.method == 'POST':
        new_product = Product(
            name=request.json['name'],
            category=request.json['category'],
            price=request.json['price'],
            stock=request.json['stock']
        )
        session.add(new_product)
        session.commit()
        return jsonify({"message": "Product added"}), 201
    elif request.method == 'GET':
        products = session.query(Product).all()
        return jsonify([product.__dict__ for product in products])

@app.route('/products/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_product(id):
    session = SessionLocal()
    product = session.query(Product).get(id)
    if not product:
        return jsonify({"message": "Product not found"}), 404

    if request.method == 'GET':
        return jsonify(product.__dict__)

    if request.method == 'PUT':
        product.name = request.json['name']
        product.category = request.json['category']
        product.price = request.json['price']
        product.stock = request.json['stock']
        session.commit()
        return jsonify({"message": "Product updated"}), 200

    if request.method == 'DELETE':
        session.delete(product)
        session.commit()
        return jsonify({"message": "Product deleted"}), 200

# Order Management
@app.route('/orders', methods=['GET', 'POST'])
def handle_orders():
    session = SessionLocal()
    if request.method == 'POST':
        new_order = Order(
            status=OrderStatus.PENDING,
            payment_method=request.json['payment_method'],
            amount=request.json['amount'],
            created_at=datetime.utcnow()
        )
        session.add(new_order)
        session.commit()
        for item in request.json['products']:
            order_product = OrderProduct(
                order_id=new_order.id,
                product_id=item['product_id'],
                quantity=item['quantity']
            )
            session.add(order_product)
        session.commit()
        send_email(
            "Order Confirmation",
            f"Your order #{new_order.id} has been placed successfully.",
            "customer@example.com"
        )
        return jsonify({"message": "Order created"}), 201
    elif request.method == 'GET':
        orders = session.query(Order).all()
        return jsonify([order.__dict__ for order in orders])

@app.route('/orders/<int:id>', methods=['GET', 'PUT'])
def handle_order(id):
    session = SessionLocal()
    order = session.query(Order).get(id)
    if not order:
        return jsonify({"message": "Order not found"}), 404

    if request.method == 'GET':
        return jsonify(order.__dict__)

    if request.method == 'PUT':
        order.status = request.json['status']
        session.commit()
        if order.status == OrderStatus.SHIPPED:
            send_email(
                "Order Shipped",
                f"Your order #{order.id} has been shipped.",
                "customer@example.com"
            )
        return jsonify({"message": "Order updated"}), 200

# Inventory Management
@app.route('/inventory', methods=['GET'])
def handle_inventory():
    session = SessionLocal()
    products = session.query(Product).filter(Product.stock < 10).all()
    if products:
        send_email(
            "Low Stock Alert",
            "Some products are running low on stock.",
            "admin@example.com"
        )
    return jsonify([product.__dict__ for product in products])

# File Upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    if file:
        upload_file_to_s3(file.filename)
        return "File uploaded successfully"

if __name__ == '__main__':
    app.run(debug=True)
