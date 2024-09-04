import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faChevronLeft,
  faMessage,
  faPerson,
  faVoicemail,
} from "@fortawesome/free-solid-svg-icons";
import "./EnterOtp.css";

const EnterOtp = () => {
  return (
    <div className="Otpcontanier">
      <div className="Otpheader">
        <div className="Otpheadercontent2">
          <div className="Otpicon2">
            <button className="backbut">
              <FontAwesomeIcon icon={faChevronLeft} />
            </button>
            <div className="back">back</div>
          </div>
        </div>
        <div className="enterotp">Enter OTP</div>
        <p className="emailnotice">
          We have shared a code of your registered email address
          somebody@gmail.com
        </p>
      </div>
      <div className="Otp">
        <div className="inp1">
          <input type="text" />
        </div>
        <div className="inp2">
          <input type="text" />
        </div>
        <div className="inp3">
          <input type="text" />
        </div>
        <div className="inp4">
          <input type="text" />
        </div>
        <div className="inp5">
          <input type="text" />
        </div>
      </div>

      <div className="submit2">
        <button> verify</button>
      </div>
    </div>
  );
};

export default EnterOtp;
