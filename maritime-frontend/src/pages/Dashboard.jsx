function Dashboard() {
  return (
    <main className="page">
      <h1>Dashboard</h1>
      <p>
        This dashboard will display voyage analytics, weather risk, route
        diversion suggestions, and fuel cost insights.
      </p>

      <section className="cards">
        <div className="card">
          <h3>Total Voyage Cost</h3>
          <p>$801,127</p>
        </div>

        <div className="card">
          <h3>Weather Risk</h3>
          <p>High</p>
        </div>
      </section>
    </main>
  );
}

export default Dashboard;