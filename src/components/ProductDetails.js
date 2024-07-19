import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import axios from "../axios";
import "./styles/ProductDetails.css";

function ProductDetail() {
    const { id } = useParams();
    const [product, setProduct] = useState(null);
  
    useEffect(() => {
      const fetchProduct = async () => {
        const response = await axios.get(`/products/${id}`);
        setProduct(response.data);
      };
      fetchProduct();
    }, [id]);
  
    if (!product) return <div>Loading...</div>;
  
    return (
      <div className="productDetail">
        <img src="https://via.placeholder.com/150" alt={product.name} />
        <div className="productDetail__info">
          <h2>{product.name}</h2>
          <p>{product.description}</p>
          <p className="productDetail__price">
            <small>$</small>
            <strong>{product.price}</strong>
          </p>
          <div className="productDetail__rating">
            {Array(5) // Assuming a fixed rating for demonstration
              .fill()
              .map((_, i) => (
                <p key={i}>🌟</p>
              ))}
          </div>
          <button>Add to Basket</button>
        </div>
      </div>
    );
  }
  
  export default ProductDetail;