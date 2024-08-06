from extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=False)
  price = db.Column(db.Float, nullable=False)
  product_image_url = db.Column(db.String(255), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False, default=1)
  inventory = db.relationship('Inventory', back_populates='product', uselist=False)

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'price': self.price,
      'product_image_url': self.product_image_url,
      'category_id': self.category_id,
      'stock': self.inventory.stock if self.inventory else 0
    }

class Category(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  description = db.Column(db.Text, nullable=True)

class Order(db.Model):
  id = db.Column(db.String(36), primary_key=True)
  email = db.Column(db.String(150), nullable=False)
  status = db.Column(db.String(50), default='Pending')
  items = db.Column(db.JSON, nullable=False)
  payment_id = db.Column(db.String(100), nullable=True)

  def to_dict(self):
    return {
      'id': self.id,
      'email': self.email,
      'status': self.status,
      'items': self.items,
      'payment_id': self.payment_id
    }

class Inventory(db.Model):
  product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
  stock = db.Column(db.Integer, nullable=False)
  product = db.relationship('Product', back_populates='inventory')

  def to_dict(self):
    return {
      'product_id': self.product_id,
      'stock': self.stock,
      'product': self.product.to_dict() if self.product else None
    }

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(150), unique=True, nullable=False)
  password_hash = db.Column(db.String(128), nullable=False)

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
