from flask import Blueprint, request, jsonify
from extensions import db
from models import Inventory, Product

bp = Blueprint('inventory_routes', __name__, url_prefix='/inventory')

@bp.route('/', methods=['GET'])
def get_inventory():
    inventory = Inventory.query.all()
    return jsonify([item.to_dict() for item in inventory]), 200

@bp.route('/<int:product_id>', methods=['GET'])
def get_inventory_item(product_id):
    inventory = Inventory.query.get(product_id)
    if inventory:
        return jsonify(inventory.to_dict()), 200
    return jsonify({'error': 'Inventory item not found'}), 404

# Helper method to convert Inventory instance to dictionary
def inventory_to_dict(inventory):
    return {
        'product_id': inventory.product_id,
        'stock': inventory.stock,
        'product': inventory.product.to_dict()
    }

Inventory.to_dict = inventory_to_dict
