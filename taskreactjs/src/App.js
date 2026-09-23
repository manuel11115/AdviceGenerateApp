import "./App.css";
import React, { useState, useEffect, useCallback } from "react";
import axios from "axios";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTableCells } from "@fortawesome/free-solid-svg-icons";

export default function App() {
  const [tip, setTip] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const generateAdvice = useCallback(() => {
    setLoading(true);
    setError(null);
    axios
      .get("https://api.adviceslip.com/advice")
      .then((res) => setTip(res.data.slip))
      .catch(() => setError("Could not fetch advice. Try again."))
      .finally(() => setLoading(false));
  }, []);

  useEffect(() => {
    generateAdvice();
  }, [generateAdvice]);

  return (
    <div className="container">
      <div className="card">
        <div className="card-body">
          <h5 className="card-title">ADVICE #{tip?.id ?? ""}</h5>
          <p className="card-text">
            {error
              ? error
              : `"${loading && !tip ? "waiting..." : tip?.advice ?? "waiting"}"`}
          </p>
          <div className="card-footer">
            <div className="card-footer-item">
              <hr className="card-footer-item-line" />
              <div className="card-footer-item-stick"></div>
              <div className="card-footer-item-stick"></div>
              <hr className="card-footer-item-line2" />
            </div>
            <button
              className="card-footer-button"
              onClick={generateAdvice}
              disabled={loading}
            >
              <FontAwesomeIcon icon={faTableCells} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
