/**
 * Input Component
 * Props:
 * - placeholder: input placeholder text
 * - type: input type
 * - value: input value
 * - onChange: change function
 */

function Input({ placeholder, type = "text", value, onChange }) {
  return (
    <input
      className="ui-input"
      type={type}
      placeholder={placeholder}
      value={value}
      onChange={onChange}
    />
  );
}

export default Input;