import React, { useState } from "react";
import api from "./api";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [form, setForm] = useState({ username: "", email: "", password: "" });
  const [error, setError] = useState("");
  const [info, setInfo] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setInfo("");

    try {
      await api.post("/register", form);
      setInfo("Registered successfully! You can now log in.");
      setTimeout(() => navigate("/login"), 1000);
    } catch (err) {
      setError("Registration failed");
    }
  };

  return (
    <div className="auth-container">
      <h2>Create Account</h2>
      {info && <p className="success">{info}</p>}
      {error && <p className="error">{error}</p>}
      <form onSubmit={handleSubmit} className="auth-form">
        <input name="username" placeholder="Username" onChange={handleChange} required />
        <input name="email" placeholder="Email" onChange={handleChange} required />
        <input type="password" name="password" placeholder="Password" onChange={handleChange} required />
        <button className="btn">Register</button>
      </form>
    </div>
  );
}
