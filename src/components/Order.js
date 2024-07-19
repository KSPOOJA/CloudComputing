import React from 'react';
import './styles/Order.css';
import moment from "moment";
import CheckoutProduct from "./CheckoutProduct";
import CurrencyFormat from "react-currency-format";

function Order({ order }) {
  return (
    <div className='order'>
      <h2>Order</h2>
      <p>{moment.unix(order.created_at).format("MMMM Do YYYY, h:mma")}</p>
      <p className="order__id">
        <small>{order.id}</small>
      </p>
      {order.products.map(item => (
        <CheckoutProduct
          key={item.id}
          id={item.product_id}
          title={item.product.name}
          image={item.product.image}
          price={item.product.price}
          rating={item.product.rating}
          hideButton
        />
      ))}
      <CurrencyFormat
        renderText={(value) => (
          <h3 className="order__total">Order Total: {value}</h3>
        )}
        decimalScale={2}
        value={order.amount}
        displayType={"text"}
        thousandSeparator={true}
        prefix={"$"}
      />   
    </div>
  );
}

export default Order;
