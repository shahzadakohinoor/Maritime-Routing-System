function Navbar({ setPage }) {
  return (
    <nav className="navbar">
      <h2>Oceanova</h2>
      <div>
        <button onClick={() => setPage("home")}>Home</button>
        <button onClick={() => setPage("about")}>About</button>
        <button onClick={() => setPage("dashboard")}>Dashboard</button>
        <button onClick={() => setPage("login")}>Login</button>
      </div>
    </nav>
  );
}

export default Navbar;