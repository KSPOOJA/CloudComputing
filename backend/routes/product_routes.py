from flask import Blueprint, request, jsonify
from extensions import db
from models import Product, Inventory

bp = Blueprint('product_routes', __name__, url_prefix='/products')

@bp.route('/', methods=['GET'])
def get_products():
  products = Product.query.all()
  return jsonify([product.to_dict() for product in products]), 200

@bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
  product = Product.query.get(product_id)
  if product:
    return jsonify(product.to_dict()), 200
  return jsonify({'error': 'Product not found'}), 404

@bp.route('/', methods=['POST'])
def create_product():
  product_data = request.json
  if not product_data or 'name' not in product_data or 'price' not in product_data or 'description' not in product_data or 'product_image_url' not in product_data:
    return jsonify({'error': 'Invalid product data'}), 400

  product = Product(
    name=product_data['name'],
    description=product_data['description'],
    price=product_data['price'],
    product_image_url=product_data['product_image_url'],
    category_id=product_data.get('category_id', 1)
  )
  db.session.add(product)
  db.session.commit()

  inventory = Inventory(product_id=product.id, stock=product_data.get('stock', 0))
  db.session.add(inventory)
  db.session.commit()

  return jsonify(product.to_dict()), 201

@bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
  product_data = request.json
  product = Product.query.get(product_id)
  if not product:
    return jsonify({'error': 'Product not found'}), 404

  product.name = product_data.get('name', product.name)
  product.description = product_data.get('description', product.description)
  product.price = product_data.get('price', product.price)
  product.product_image_url = product_data.get('product_image_url', product.product_image_url)
  product.category_id = product_data.get('category_id', product.category_id)

  inventory = Inventory.query.get(product_id)
  if inventory:
    inventory.stock = product_data.get('stock', inventory.stock)
  else:
    inventory = Inventory(product_id=product.id, stock=product_data.get('stock', 0))
    db.session.add(inventory)

  db.session.commit()
  return jsonify(product.to_dict()), 200

@bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
  product = Product.query.get(product_id)
  if not product:
    return jsonify({'error': 'Product not found'}), 404

  inventory = Inventory.query.get(product_id)
  if inventory:
    db.session.delete(inventory)

  db.session.delete(product)
  db.session.commit()
  return jsonify({'message': 'Product deleted successfully'}), 200
