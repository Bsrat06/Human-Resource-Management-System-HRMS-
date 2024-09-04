import React from "react";
import "./passSuc.css";
const PassSuc = () => {
  return (
    <div className="containerPass">
      <div className="tada">🎉</div>

      <p className="mainsuc">Password updated successfully.</p>
      <p className="suc">your password updated successfully.</p>

      <button className="bcbt">back to Login</button>
    </div>
  );
};

export default PassSuc;
