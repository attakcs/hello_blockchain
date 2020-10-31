import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";
import Transaction from "./Transaction";
import { API_BASE_URL, SECOND_JS } from "../config";
import history from "../history";

const POLL_INTERVAL = 10 * SECOND_JS;

function TransactionPool() {
  const [transactions, setTransactions] = useState([]);

  const fetchTransactions = () => {
    fetch(`${API_BASE_URL}/transactions`)
      .then((response) => response.json())
      .then((json) => {
        console.log("Transaction json", json);
        setTransactions(json);
      });
  };

  useEffect(() => {
    fetchTransactions();

    const intervalId = setInterval(fetchTransactions(), POLL_INTERVAL);

    return () => clearInterval(intervalId);
  }, []);

  const fetchMineBlock = () => {
    fetch(`${API_BASE_URL}/blockchain/mine`).then(() => {
      alert("Success!");
      history.push("/blockchain");
    });
  };

  return (
    <div className="TransactionPool">
      <Link to="/">Home</Link>
      <hr />
      <h3>Transaction Pool</h3>
      <div>
        {transactions.map((transaction) => (
          <div key={transaction.id}>
            <hr />
            <Transaction transaction={transaction} />
          </div>
        ))}
      </div>
      <hr />
      <Button variant="danger" onClick={fetchMineBlock}>
        Mine a block of transactions
      </Button>
    </div>
  );
}

export default TransactionPool;
