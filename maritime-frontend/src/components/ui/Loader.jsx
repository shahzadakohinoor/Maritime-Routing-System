/**
 * Loader Component
 * Props:
 * - text: loading message
 */

function Loader({ text = "Loading..." }) {
  return (
    <div className="ui-loader">
      <span className="spinner"></span>
      <p>{text}</p>
    </div>
  );
}

export default Loader;