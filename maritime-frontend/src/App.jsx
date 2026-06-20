import { useState } from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Card from "./components/Card";
import Footer from "./components/Footer";
import About from "./pages/About";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import "./index.css";

function App() {
  const [page, setPage] = useState("home");

  return (
    <>
      <Navbar setPage={setPage} />

      {page === "home" && (
        <>
          <Hero setPage={setPage} />
          <section className="cards">
            <Card title="Route Optimization" text="Plan safer maritime routes using weather and voyage data." />
            <Card title="Fuel Cost Analysis" text="Estimate fuel usage, voyage duration, and total voyage cost." />
          </section>
        </>
      )}

      {page === "about" && <About />}
      {page === "dashboard" && <Dashboard />}
      {page === "login" && <Login />}

      <Footer />
    </>
  );
}

export default App;