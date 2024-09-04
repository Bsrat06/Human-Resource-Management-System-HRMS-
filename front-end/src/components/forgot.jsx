import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChevronLeft,
  faMessage,
  faPerson,
  faVoicemail,
} from "@fortawesome/free-solid-svg-icons";
import "./forgot.css";
import email_icon from "./Assets/email.png";


const sendOTP = () => {
  // call function to send OTP
};

const back = () => {
  // call function to go back
};

const Forgot = () => {
  return (
    <div className="container2">
      <div className="header2">
        <div className="headercontent2">
          <div className="icon2">
            <FontAwesomeIcon onClick={back} icon={faChevronLeft} />
          </div>
          <div className="back">back</div>
        </div>
        <div className="forgot">
          Forgot password
          <span>
            Enter your registered email address. we’ll send you a code to reset
            your password.
          </span>
        </div>
      </div>
      <div className="inputs1">
        <div className="input2">
                <img src={email_icon} alt="" />
          <input type="email"  className="maininp" placeholder="Email" />
        </div>
      </div>
      <div className="submit2">
        <button onClick={sendOTP}>Send OTP</button>
      </div>
    </div>
  );
};

export default Forgot;
