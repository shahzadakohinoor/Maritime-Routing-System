/**
 * Button Component
 * Props:
 * - text: button label
 * - onClick: click function
 * - type: button type
 */

function Button({ text, onClick, type = "button" }) {
  return (
    <button className="ui-btn" type={type} onClick={onClick}>
      {text}
    </button>
  );
}

export default Button;