import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Login from "./login";
import Register from "./register";
import Dashboard from "./Dashboard";
import Authentication from "./Authentication";

function App() {
  return (
    <BrowserRouter>
      <Routes>
                <Route path="/register" element={<Register />} />

        <Route path="/login" element={<Login />} />

        <Route
          path="/dashboard"
          element={
           <Authentication>
                <Dashboard />
           </Authentication>
           
          }
        />

        <Route path="*" element={<Navigate to="/register" />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
