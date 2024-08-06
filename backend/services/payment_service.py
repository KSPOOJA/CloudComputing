from extensions import db
from models import Order
from services.email_service import send_email
import uuid

def process_payment(order_id, amount, currency='EUR', description=None):
  try:
    # Simulate payment processing
    print(f"Processing payment of {amount} {currency} for order {order_id} with description '{description}'")

    # Assume the payment is successful and generate a mock payment ID
    payment_status = 'succeeded'
    payment_id = str(uuid.uuid4())

    if payment_status != 'succeeded':
      return {"status": "failure", "error": "Payment not confirmed"}

    # Find the order
    order = Order.query.get(order_id)
    if not order:
      return {"status": "failure", "error": "Order not found"}

    # Update order status and payment ID
    order.status = 'Paid'
    order.payment_id = payment_id
    db.session.commit()

    # Send confirmation email
    email_response = send_email(
      'Order Confirmation',
      [order.email],
      f'Your payment for order {order.id} has been successfully processed. Payment ID: {payment_id}'
    )

    if email_response and email_response.get('status_code') == 200:
      return {"status": "success", "orderId": order.id, "paymentId": payment_id}
    else:
      return {"status": "failure", "error": "Failed to send email"}

  except Exception as e:
    print(f"Exception during payment processing: {e}")
    return {"status": "failure", "error": str(e)}
