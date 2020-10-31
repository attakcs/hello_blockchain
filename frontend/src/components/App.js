import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import logo from "../assets/logo.png";
import { API_BASE_URL } from "../config";

function App() {
  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch(`${API_BASE_URL}/wallet/info`)
      .then((response) => response.json())
      .then((json) => setWalletInfo(json));
  }, []);

  const { address, balance } = walletInfo;

  return (
    <div className="App">
      <img className="logo" src={logo} alt="app-logo" />
      <br />
      <Link to='/blockchain'>Blockchain</Link>
      <Link to='/conduct-transaction'>Conduct-transaction</Link>
      <br />
      <div className="WalletInfo">
        <h3>Wallet info :</h3>
        <div>Address: {address}</div>
        <div>Balance: {balance}</div>
      </div>
    </div>
  );
}

export default App;
