import "./App.css";
import React, { useState, useEffect } from "react";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTableCells } from "@fortawesome/free-solid-svg-icons";

export default function App() {
  const [tipApi, setTipApi] = useState("waiting");

  useEffect(() => {
    const buttonGenerate = () =>
      axios
        .get("https://api.adviceslip.com/advice", {})
        .then((res) => setTipApi(res.data.slip));
    const button = document.querySelector(".card-footer-button");

    button.addEventListener("click", buttonGenerate);
  }, []);

  return (
    <div className="container">
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">ADVICE #{tipApi.id}</h5>
          <p className="card-text">"{tipApi.advice || "waiting"}"</p>
          <div className="card-footer">
            <div className="card-footer-item">
              <hr className="card-footer-item-line" />
              <div className="card-footer-item-stick"></div>
              <div className="card-footer-item-stick"></div>
              <hr className="card-footer-item-line2" />
            </div>
            <button className="card-footer-button">
              <FontAwesomeIcon icon={faTableCells} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
