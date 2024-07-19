import React, { useState } from 'react';
import './styles/Login.css'
import { Link, useHistory } from "react-router-dom";
import { cognito } from "../awsConfig";

function Login() {
  const history = useHistory();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const signIn = async (e) => {
    e.preventDefault();
    const params = {
      AuthFlow: 'USER_PASSWORD_AUTH',
      ClientId: 'your-cognito-client-id',
      AuthParameters: {
        USERNAME: email,
        PASSWORD: password,
      },
    };

    try {
      const authData = await cognito.initiateAuth(params).promise();
      localStorage.setItem('cognitoAuthData', JSON.stringify(authData));
      history.push('/');
    } catch (error) {
      alert(error.message);
    }
  };

  const register = async (e) => {
    e.preventDefault();
    const params = {
      ClientId: 'your-cognito-client-id',
      Username: email,
      Password: password,
    };

    try {
      await cognito.signUp(params).promise();
      history.push('/');
    } catch (error) {
      alert(error.message);
    }
  };

  return (
    <div className='login'>
      <Link to='/'>
        <img
          className="login__logo"
          src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/1024px-Amazon_logo.svg.png' 
        />
      </Link>

      <div className='login__container'>
        <h1>Sign-in</h1>

        <form>
          <h5>E-mail</h5>
          <input type='text' value={email} onChange={e => setEmail(e.target.value)} />

          <h5>Password</h5>
          <input type='password' value={password} onChange={e => setPassword(e.target.value)} />

          <button type='submit' onClick={signIn} className='login__signInButton'>Sign In</button>
        </form>

        <p>
          By signing-in you agree to the AMAZON FAKE CLONE Conditions of Use & Sale. Please
          see our Privacy Notice, our Cookies Notice and our Interest-Based Ads Notice.
        </p>

        <button onClick={register} className='login__registerButton'>Create your Amazon Account</button>
      </div>
    </div>
  );
}

export default Login;
