import { useState } from "react";

import Navbar from "./components/Navbar";
import Hero from "./components/Hero";
import Card from "./components/Card";
import Footer from "./components/Footer";

import About from "./pages/About";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";
import ComponentsDemo from "./pages/ComponentsDemo";

import "./index.css";

function App() {
  const [page, setPage] = useState("home");
  const [darkMode, setDarkMode] = useState(true);

  return (
    <div className={darkMode ? "app dark" : "app light"}>
      <Navbar
        setPage={setPage}
        darkMode={darkMode}
        setDarkMode={setDarkMode}
      />

      {page === "home" && (
        <>
          <Hero setPage={setPage} />

          <section className="cards">
            <Card
              title="Route Optimization"
              text="Plan safer maritime routes using weather and voyage data."
            />

            <Card
              title="Fuel Cost Analysis"
              text="Estimate fuel usage, voyage duration, and total voyage cost."
            />
          </section>
        </>
      )}

      {page === "about" && <About />}
      {page === "dashboard" && <Dashboard />}
      {page === "login" && <Login />}
      {page === "components" && <ComponentsDemo />}

      <Footer />
    </div>
  );
}

export default App;