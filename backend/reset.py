# reset_db.py

from app import app, db
from models import User, Category, Product, Supplier, Inventory, Order

# Push an application context
with app.app_context():
    # Drop all tables
    db.drop_all()

    # Recreate all tables
    db.create_all()

    print("Database has been reset.")
