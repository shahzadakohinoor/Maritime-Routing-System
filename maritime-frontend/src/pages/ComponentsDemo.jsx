import { useState } from "react";
import { Button, Input, Modal, Toast, Loader } from "../components/ui";

function ComponentsDemo() {
  const [showModal, setShowModal] = useState(false);
  const [showToast, setShowToast] = useState(false);

  function handleToast() {
    setShowToast(true);

    setTimeout(() => {
      setShowToast(false);
    }, 3000);
  }

  return (
    <main className="page">
      <h1>Component Library Demo</h1>
      <p>
        This page demonstrates Button, Input, Modal, Toast, and Loader
        components.
      </p>

      <div className="card">
        <h3>Input Component</h3>
        <Input placeholder="Enter vessel name" />
      </div>

      <div className="card">
        <h3>Button Component</h3>
        <Button text="Open Modal" onClick={() => setShowModal(true)} />
        <Button text="Show Toast" onClick={handleToast} />
      </div>

      <div className="card">
        <h3>Loader Component</h3>
        <Loader text="Fetching voyage data..." />
      </div>

      {showToast && <Toast message="Route Generated Successfully" />}

      {showModal && (
        <Modal
          title="AI Route Recommendation"
          onClose={() => setShowModal(false)}
        >
          <p>
            Suggested detour route reduces gale risk and improves voyage safety.
          </p>
        </Modal>
      )}
    </main>
  );
}

export default ComponentsDemo;