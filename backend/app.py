from flask import Flask
from extensions import db, mail, login_manager, init_app
from config import Config
from routes import product_routes, order_routes, payment_routes, inventory_routes, auth_routes

def create_app():
  app = Flask(__name__)
  app.config.from_object(Config)

  init_app(app)

  with app.app_context():
    db.create_all()

  app.register_blueprint(product_routes.bp)
  app.register_blueprint(order_routes.bp)
  app.register_blueprint(payment_routes.bp)
  app.register_blueprint(inventory_routes.bp)
  app.register_blueprint(auth_routes.bp)

  return app

if __name__ == '__main__':
  app = create_app()
  app.run(debug=True)
