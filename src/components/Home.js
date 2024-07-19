import React, { useEffect, useState } from "react";
import "./styles/Home.css";
import Product from "./Product";
import axios from "../axios";

function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    const fetchProducts = async () => {
      const response = await axios.get("/products");
      setProducts(response.data);
    };
    fetchProducts();
  }, []);

  return (
    <div className="home">
      <div className="home__container">
        <img
          className="home__image"
          src="https://images-eu.ssl-images-amazon.com/images/G/02/digital/video/merch2016/Hero/Covid19/Generic/GWBleedingHero_ENG_COVIDUPDATE__XSite_1500x600_PV_en-GB._CB428684220_.jpg"
          alt=""
        />
        <div className="home__row">
          {products.map(product => (
            <Product
              key={product.id}
              id={product.id}
              title={product.name}
              price={product.price}
              rating={5} // You can update this to get the actual rating
              image="https://via.placeholder.com/150" // Update with actual image URL
            />
          ))}
        </div>
      </div>
    </div>
  );
}

export default Home;
