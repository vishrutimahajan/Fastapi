import React, { useState } from "react";
import api from "./api";
import { useNavigate } from "react-router-dom";
import "./register.css";
export default function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [error, setError] = useState("");
  const [info, setInfo] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setInfo("");

    try {
      // wait for API to respond
      await api.post("/register", form);
      setInfo("Registered successfully! Redirecting to login...");
      // small delay so user sees message
      setTimeout(() => navigate("/login"), 900);
    } catch (err) {
      // show backend message if available
      const msg =
        err?.response?.data?.message ||
        err?.message ||
        "Registration failed. Try again.";
      setError(msg);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-box">
        <h2 className="auth-title">Create Account</h2>

        {info && <p className="success">{info}</p>}
        {error && <p className="error">{error}</p>}

        <form onSubmit={handleSubmit} className="auth-form" noValidate>
          <input
            name="username"
            placeholder="Username"
            onChange={handleChange}
            value={form.username}
            required
            autoComplete="username"
          />
          <input
            name="email"
            placeholder="Email"
            type="email"
            onChange={handleChange}
            value={form.email}
            required
            autoComplete="email"
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            onChange={handleChange}
            value={form.password}
            required
            autoComplete="new-password"
          />
          <div className="checkbox-row">
  <input 
    type="checkbox" 
    id="terms" 
    name="terms" 
    required 
  />
  <label htmlFor="terms">I agree to the Terms & Conditions</label>
</div>
          <button className="btn" type="submit">
            Register
          </button>
          <div className="abc-link">
            Already have an account? <a href="/login">Login</a>
          </div>
        </form>
      </div>
    </div>
  );
}
