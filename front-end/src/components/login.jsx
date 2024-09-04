// import React, { useState } from "react";
import "./login.css";
import user_icon from "./Assets/person.png";
import email_icon from "./Assets/email.png";
import password_icon from "./Assets/password.png";
const LoginPage = () => {
  return (
    <div className="container">
      <div className="header">
        <div className="header">
          <div className="text">Welcome 👋 </div>
          <div className="underline"></div>
          <p className="p"> please <span className="login">LOGIN</span> here </p>
        </div>
        <div className="inputs">
          <div className="input">
            <img src={email_icon} alt="" />
            <input type="email" placeholder="Email" />
          </div>

          <div className="input">
            <img src={password_icon} alt="" />
            <input type="password" placeholder="Password" />
          </div>
          <div className="submit">
            <button>Login</button>

            <div className="forgotpass">
              forgot password ? <a href="">click here</a>
            </div>
            <div className="noacc">
                 don't you have an account ? register <a href="">here</a>
              </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;
