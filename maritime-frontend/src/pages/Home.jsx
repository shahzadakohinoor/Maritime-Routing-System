import Hero from "../components/Hero";
import Card from "../components/Card";

function Home() {
  return (
    <>
      <Hero />

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
  );
}

export default Home;