import React, { useState } from "react";
import api, { setToken } from "./api";
import { useNavigate } from "react-router-dom";
import "./register.css";

export default function Login() {
  const [form, setForm] = useState({ username: "", password: "" });
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const res = await api.post("/token", form);  // adjust if needed
      setToken(res.data.access_token);
      navigate("/dashboard");
    } catch (err) {
      setError("Invalid username or password");
    }
  };

  return (
     <div className="auth-container">
      <div className="auth-box">   {/* floating box same as register */}

        <h2 className="auth-title">Login</h2>

        {error && <p className="error">{error}</p>}

        <form onSubmit={handleSubmit} className="auth-form">
          <input
            type="text"
            placeholder="Username"
            name="username"
            value={form.username}
            onChange={handleChange}
            required
          />

          <input
            type="password"
            placeholder="Password"
            name="password"
            value={form.password}
            onChange={handleChange}
            required
          />

          <button className="btn" style={{marginTop:"100px"}}>Login</button>

          {/* 🔥 Navigation link to Register page */}
          <div className="abc-link">
          Don't have an account? <a href="/register">Register</a>
          </div>
        </form>

      </div>
    </div>
  );
}