function Navbar({ setPage, darkMode, setDarkMode }) {
  return (
    <nav className="navbar">
      <h2>Oceanova</h2>

      <div>
        <button onClick={() => setPage("home")}>Home</button>
        <button onClick={() => setPage("about")}>About</button>
        <button onClick={() => setPage("dashboard")}>Dashboard</button>
        <button onClick={() => setPage("components")}>Components</button>
        <button onClick={() => setPage("login")}>Login</button>
        <button onClick={() => setDarkMode(!darkMode)}>
          {darkMode ? "Light Mode" : "Dark Mode"}
        </button>
      </div>
    </nav>
  );
}

export default Navbar;