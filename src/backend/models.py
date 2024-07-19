from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from awsConfig import Base
import enum

class OrderStatus(enum.Enum):
    PENDING = "PENDING"
    SHIPPED = "SHIPPED"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    price = Column(Float)
    stock = Column(Integer)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(OrderStatus))
    payment_method = Column(String)
    amount = Column(Float)
    created_at = Column(DateTime)
    products = relationship("OrderProduct", back_populates="order")

class OrderProduct(Base):
    __tablename__ = "order_products"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    order = relationship("Order", back_populates="products")
    product = relationship("Product")
