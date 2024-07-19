import React, { useEffect } from "react";
import "./App.css";
import Header from "./components/Header";
import Home from "./components/Home";
import Checkout from "./components/Checkout";
import Login from "./components/Login";
import Payment from "./components/Payment";
import Orders from "./components/Orders";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { useStateValue } from "./StateProvider";
import { auth } from "./awsConfig";
import { loadStripe } from "@stripe/stripe-js";
import { Elements } from "@stripe/react-stripe-js";

const promise = loadStripe("your-stripe-key");

function App() {
  const [{}, dispatch] = useStateValue();

  useEffect(() => {
    // Will only run once when the app component loads...
    const checkUserSession = async () => {
      const session = await auth.getCurrentSession().catch(err => console.error(err));
      if (session) {
        dispatch({
          type: "SET_USER",
          user: session.getIdToken().payload,
        });
      } else {
        dispatch({
          type: "SET_USER",
          user: null,
        });
      }
    };
    checkUserSession();
  }, []);

  return (
    <Router>
      <div className="app">
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/orders">
            <Header />
            <Orders />
          </Route>
          <Route path="/checkout">
            <Header />
            <Checkout />
          </Route>
          <Route path="/payment">
            <Header />
            <Elements stripe={promise}>
              <Payment />
            </Elements>
          </Route>
          <Route path="/">
            <Header />
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
