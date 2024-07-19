import React, { useState, useEffect } from 'react';
import './styles/Orders.css';
import { useStateValue } from "../StateProvider";
import Order from './Order';
import axios from "../axios";

function Orders() {
  const [{ basket, user }, dispatch] = useStateValue();
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    if (user) {
      const fetchOrders = async () => {
        const response = await axios.get(`/orders?userId=${user.sub}`);
        setOrders(response.data);
      };
      fetchOrders();
    } else {
      setOrders([]);
    }
  }, [user]);

  return (
    <div className='orders'>
      <h1>Your Orders</h1>
      <div className='orders__order'>
        {orders.map(order => (
          <Order key={order.id} order={order} />
        ))}
      </div>
    </div>
  );
}

export default Orders;
